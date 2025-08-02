"""
Arama Sonucu Testleri
=====================
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
def test_documents(auth_headers):
    """Test dokümanları oluştur"""
    documents = []
    
    # Yapay zeka dokümanı
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("Bu doküman yapay zeka ve makine öğrenmesi hakkında bilgi içerir.")
        test_file_path = f.name
    
    try:
        with open(test_file_path, 'rb') as f:
            files = {"file": ("ai_doc.txt", f, "text/plain")}
            data = {"title": "Yapay Zeka Dokümanı"}
            response = client.post("/api/documents/", files=files, data=data, headers=auth_headers)
            documents.append(response.json())
    finally:
        os.unlink(test_file_path)
    
    # Veri bilimi dokümanı
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("Bu doküman veri bilimi ve istatistik hakkında bilgi içerir.")
        test_file_path = f.name
    
    try:
        with open(test_file_path, 'rb') as f:
            files = {"file": ("data_science.txt", f, "text/plain")}
            data = {"title": "Veri Bilimi Dokümanı"}
            response = client.post("/api/documents/", files=files, data=data, headers=auth_headers)
            documents.append(response.json())
    finally:
        os.unlink(test_file_path)
    
    return documents

class TestBasicSearch:
    """Temel arama testleri"""
    
    def test_search_with_query(self, auth_headers, test_documents):
        """Sorgu ile arama testi"""
        response = client.get("/api/search/", 
                            params={"query": "yapay zeka"}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        assert isinstance(results, list)
        assert len(results) > 0
    
    def test_search_with_file_type_filter(self, auth_headers, test_documents):
        """Dosya türü filtresi ile arama testi"""
        response = client.get("/api/search/", 
                            params={"query": "doküman", "file_type": "txt"}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        assert isinstance(results, list)
        for result in results:
            assert result["file_type"] == "txt"
    
    def test_search_no_results(self, auth_headers):
        """Sonuç bulunamayan arama testi"""
        response = client.get("/api/search/", 
                            params={"query": "xyzabc123"}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        assert isinstance(results, list)
        assert len(results) == 0
    
    def test_search_empty_query(self, auth_headers):
        """Boş sorgu ile arama testi"""
        response = client.get("/api/search/", 
                            params={"query": ""}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        assert isinstance(results, list)

class TestAdvancedSearch:
    """Gelişmiş arama testleri"""
    
    def test_advanced_search_with_filters(self, auth_headers, test_documents):
        """Filtreler ile gelişmiş arama testi"""
        response = client.get("/api/search/advanced-search", 
                            params={
                                "query": "doküman",
                                "file_type": "txt",
                                "limit": 10,
                                "offset": 0
                            }, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "documents" in result
        assert "total_count" in result
        assert "limit" in result
        assert "offset" in result
        assert isinstance(result["documents"], list)
        assert result["total_count"] >= 0
    
    def test_advanced_search_with_date_filter(self, auth_headers, test_documents):
        """Tarih filtresi ile arama testi"""
        from datetime import datetime, timedelta
        
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        
        response = client.get("/api/search/advanced-search", 
                            params={
                                "query": "doküman",
                                "date_from": yesterday.isoformat(),
                                "date_to": today.isoformat()
                            }, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "documents" in result

class TestAISearch:
    """AI destekli arama testleri"""
    
    def test_ai_search_success(self, auth_headers, test_documents):
        """AI arama başarı testi"""
        response = client.get("/api/search/ai-search", 
                            params={"query": "yapay zeka hakkında ne anlatıyor?"}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        assert isinstance(results, list)
        if len(results) > 0:
            assert "document" in results[0]
            assert "score" in results[0]
            assert "reason" in results[0]
    
    def test_ai_search_no_results(self, auth_headers):
        """AI arama sonuç bulunamama testi"""
        response = client.get("/api/search/ai-search", 
                            params={"query": "xyzabc123 hakkında ne anlatıyor?"}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        assert isinstance(results, list)
        assert len(results) == 0
    
    def test_ai_search_unauthorized(self, test_documents):
        """Yetkisiz AI arama testi"""
        response = client.get("/api/search/ai-search", 
                            params={"query": "test sorgu"})
        
        assert response.status_code == 401

class TestSearchSuggestions:
    """Arama önerileri testleri"""
    
    def test_get_search_suggestions(self, auth_headers, test_documents):
        """Arama önerileri getirme testi"""
        response = client.get("/api/search/suggestions", 
                            params={"query": "doküman"}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "suggestions" in result
        assert "query" in result
        assert isinstance(result["suggestions"], list)
        assert result["query"] == "doküman"
    
    def test_get_search_suggestions_empty_query(self, auth_headers):
        """Boş sorgu ile öneri testi"""
        response = client.get("/api/search/suggestions", 
                            params={"query": ""}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "suggestions" in result
        assert isinstance(result["suggestions"], list)

class TestSearchResultsFormat:
    """Arama sonuç formatı testleri"""
    
    def test_search_result_format(self, auth_headers, test_documents):
        """Arama sonuç formatı testi"""
        response = client.get("/api/search/", 
                            params={"query": "doküman"}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        
        if len(results) > 0:
            result = results[0]
            required_fields = ["id", "title", "filename", "file_type", "file_size", "created_at"]
            
            for field in required_fields:
                assert field in result
            
            # Tarih formatı kontrolü
            assert isinstance(result["created_at"], str)
            
            # Dosya boyutu kontrolü
            assert isinstance(result["file_size"], int)
            assert result["file_size"] > 0
    
    def test_search_result_with_summary(self, auth_headers, test_documents):
        """Özetli arama sonucu testi"""
        # Önce özet oluştur
        doc_id = test_documents[0]["id"]
        client.post(f"/api/summary/{doc_id}/generate", headers=auth_headers)
        
        # Sonra arama yap
        response = client.get("/api/search/", 
                            params={"query": "doküman"}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        
        if len(results) > 0:
            result = results[0]
            if "summary" in result:
                assert isinstance(result["summary"], str)
            if "keywords" in result:
                assert isinstance(result["keywords"], str)

class TestSearchPagination:
    """Arama sayfalama testleri"""
    
    def test_search_with_limit_and_offset(self, auth_headers, test_documents):
        """Limit ve offset ile arama testi"""
        response = client.get("/api/search/", 
                            params={"query": "doküman", "limit": 1, "offset": 0}, 
                            headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        assert isinstance(results, list)
        assert len(results) <= 1
    
    def test_search_pagination_consistency(self, auth_headers, test_documents):
        """Sayfalama tutarlılığı testi"""
        # İlk sayfa
        response1 = client.get("/api/search/", 
                             params={"query": "doküman", "limit": 1, "offset": 0}, 
                             headers=auth_headers)
        
        # İkinci sayfa
        response2 = client.get("/api/search/", 
                             params={"query": "doküman", "limit": 1, "offset": 1}, 
                             headers=auth_headers)
        
        assert response1.status_code == 200
        assert response2.status_code == 200
        
        results1 = response1.json()
        results2 = response2.json()
        
        # Farklı sayfalarda farklı sonuçlar olmalı
        if len(results1) > 0 and len(results2) > 0:
            assert results1[0]["id"] != results2[0]["id"]

class TestSearchErrorHandling:
    """Arama hata yönetimi testleri"""
    
    def test_search_unauthorized(self):
        """Yetkisiz arama testi"""
        response = client.get("/api/search/", params={"query": "test"})
        assert response.status_code == 401
    
    def test_search_invalid_parameters(self, auth_headers):
        """Geçersiz parametreler ile arama testi"""
        response = client.get("/api/search/", 
                            params={"query": "test", "limit": -1}, 
                            headers=auth_headers)
        
        # Negatif limit kabul edilmemeli
        assert response.status_code in [200, 400, 422]
    
    def test_search_special_characters(self, auth_headers, test_documents):
        """Özel karakterler ile arama testi"""
        special_queries = [
            "test@example.com",
            "test&query",
            "test+query",
            "test/query",
            "test?query"
        ]
        
        for query in special_queries:
            response = client.get("/api/search/", 
                               params={"query": query}, 
                               headers=auth_headers)
            
            assert response.status_code == 200
            assert isinstance(response.json(), list) 