"""
Özetleme Fonksiyonu Testleri
============================
"""

import pytest
import tempfile
import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from main import app
from models.document import Document
from models.user import User
from services.auth_service import AuthService
from services.ai_service import AIService

# Test veritabanı
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def test_user():
    """Test kullanıcısı oluştur"""
    db = TestingSessionLocal()
    from models.user import UserCreate
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        full_name="Test User",
        password="testpassword123"
    )
    user = AuthService.create_user(db, user_data)
    db.close()
    return user

@pytest.fixture
def auth_headers(test_user):
    """Test kullanıcısı için auth headers"""
    login_data = {
        "email": "test@example.com",
        "password": "testpassword123"
    }
    response = client.post("/api/auth/login", json=login_data)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def test_document(auth_headers):
    """Test dokümanı oluştur"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("Bu bir test dokümanıdır. Yapay zeka ve makine öğrenmesi hakkında bilgi içerir.")
        test_file_path = f.name
    
    try:
        with open(test_file_path, 'rb') as f:
            files = {"file": ("test.txt", f, "text/plain")}
            data = {"title": "Test Doküman"}
            response = client.post("/api/documents/", files=files, data=data, headers=auth_headers)
        
        return response.json()
    finally:
        os.unlink(test_file_path)

class TestSummaryGeneration:
    """Özet oluşturma testleri"""
    
    def test_generate_summary_success(self, auth_headers, test_document):
        """Başarılı özet oluşturma testi"""
        doc_id = test_document["id"]
        response = client.post(f"/api/summary/{doc_id}/generate", headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "summary" in result
        assert "keywords" in result
        assert len(result["summary"]) > 0
        assert len(result["keywords"]) > 0
    
    def test_generate_summary_nonexistent_document(self, auth_headers):
        """Var olmayan doküman için özet oluşturma testi"""
        response = client.post("/api/summary/999/generate", headers=auth_headers)
        assert response.status_code == 404
    
    def test_generate_summary_unauthorized(self, test_document):
        """Yetkisiz özet oluşturma testi"""
        doc_id = test_document["id"]
        response = client.post(f"/api/summary/{doc_id}/generate")
        assert response.status_code == 401
    
    def test_get_document_summary(self, auth_headers, test_document):
        """Doküman özetini getirme testi"""
        doc_id = test_document["id"]
        response = client.get(f"/api/summary/{doc_id}/summary", headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "document_id" in result
        assert "title" in result
        assert "has_summary" in result

class TestAIService:
    """AI servis testleri"""
    
    async def test_generate_summary_and_keywords(self):
        """AI ile özet ve anahtar kelime oluşturma testi"""
        ai_service = AIService()
        test_content = """
        Yapay zeka (AI), bilgisayarların insan benzeri düşünme ve öğrenme yeteneklerine sahip olmasını sağlayan teknolojidir. 
        Makine öğrenmesi, derin öğrenme ve doğal dil işleme gibi alt alanları vardır. 
        Günümüzde sağlık, finans, eğitim ve ulaşım gibi birçok sektörde kullanılmaktadır.
        """
        
        summary, keywords = await ai_service.generate_summary_and_keywords(test_content)
        
        assert isinstance(summary, str)
        assert isinstance(keywords, str)
        assert len(summary) > 0
        assert len(keywords) > 0
        assert "yapay zeka" in summary.lower() or "AI" in summary
    
    async def test_answer_question(self):
        """Soru cevaplama testi"""
        ai_service = AIService()
        test_content = """
        Yapay zeka, bilgisayarların insan benzeri düşünme yeteneklerine sahip olmasını sağlayan teknolojidir.
        """
        question = "Yapay zeka nedir?"
        
        answer = await ai_service.answer_question(question, test_content)
        
        assert isinstance(answer, str)
        assert len(answer) > 0
    
    async def test_search_documents(self):
        """Doküman arama testi"""
        ai_service = AIService()
        test_documents = [
            "Bu doküman yapay zeka hakkında bilgi içerir.",
            "Bu doküman makine öğrenmesi konusunu ele alır.",
            "Bu doküman veri bilimi hakkındadır."
        ]
        query = "yapay zeka"
        
        results = await ai_service.search_documents(query, test_documents)
        
        assert isinstance(results, list)
        assert len(results) > 0
        assert "index" in results[0]
        assert "score" in results[0]
        assert "reason" in results[0]

class TestBatchSummarization:
    """Toplu özetleme testleri"""
    
    def test_batch_summarize_documents(self, auth_headers, test_document):
        """Toplu özetleme testi"""
        doc_ids = [test_document["id"]]
        response = client.post("/api/summary/batch-summarize", 
                             json={"document_ids": doc_ids}, 
                             headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "results" in result
        assert "total_processed" in result
        assert "successful" in result
        assert result["total_processed"] == 1
        assert result["successful"] == 1
    
    def test_batch_summarize_empty_list(self, auth_headers):
        """Boş liste ile toplu özetleme testi"""
        response = client.post("/api/summary/batch-summarize", 
                             json={"document_ids": []}, 
                             headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert result["total_processed"] == 0
        assert result["successful"] == 0

class TestSummaryStatistics:
    """Özet istatistikleri testleri"""
    
    def test_get_summary_statistics(self, auth_headers, test_document):
        """Özet istatistikleri getirme testi"""
        response = client.get("/api/summary/statistics", headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "total_documents" in result
        assert "documents_with_summary" in result
        assert "documents_without_summary" in result
        assert "summary_percentage" in result
        assert result["total_documents"] >= 1

class TestQuestionAnswering:
    """Soru cevaplama testleri"""
    
    def test_ask_question_success(self, auth_headers, test_document):
        """Başarılı soru sorma testi"""
        doc_id = test_document["id"]
        question = "Bu doküman ne hakkında?"
        
        response = client.post(f"/api/summary/{doc_id}/ask", 
                             params={"question": question}, 
                             headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "question" in result
        assert "answer" in result
        assert "document_id" in result
        assert "document_title" in result
        assert result["question"] == question
        assert len(result["answer"]) > 0
    
    def test_ask_question_nonexistent_document(self, auth_headers):
        """Var olmayan doküman için soru sorma testi"""
        response = client.post("/api/summary/999/ask", 
                             params={"question": "Test soru"}, 
                             headers=auth_headers)
        
        assert response.status_code == 404
    
    def test_ask_question_no_question(self, auth_headers, test_document):
        """Soru olmadan soru sorma testi"""
        doc_id = test_document["id"]
        response = client.post(f"/api/summary/{doc_id}/ask", headers=auth_headers)
        
        assert response.status_code == 422 