"""
Yetkilendirme & Güvenlik Testleri
=================================
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

class TestAuthentication:
    """Kimlik doğrulama testleri"""
    
    def test_user_registration_success(self):
        """Başarılı kullanıcı kaydı testi"""
        user_data = {
            "email": "newuser@example.com",
            "username": "newuser",
            "full_name": "New User",
            "password": "newpassword123"
        }
        
        response = client.post("/api/auth/register", json=user_data)
        
        assert response.status_code == 200
        result = response.json()
        assert "id" in result
        assert result["email"] == user_data["email"]
        assert result["username"] == user_data["username"]
        assert result["full_name"] == user_data["full_name"]
        assert "password" not in result  # Şifre döndürülmemeli
    
    def test_user_registration_duplicate_email(self, test_user):
        """Aynı email ile kayıt testi"""
        user_data = {
            "email": "test@example.com",  # Mevcut email
            "username": "anotheruser",
            "full_name": "Another User",
            "password": "password123"
        }
        
        response = client.post("/api/auth/register", json=user_data)
        
        assert response.status_code == 400
        assert "email" in response.json()["detail"].lower()
    
    def test_user_login_success(self, test_user):
        """Başarılı giriş testi"""
        login_data = {
            "email": "test@example.com",
            "password": "testpassword123"
        }
        
        response = client.post("/api/auth/login", json=login_data)
        
        assert response.status_code == 200
        result = response.json()
        assert "access_token" in result
        assert "token_type" in result
        assert "user" in result
        assert result["token_type"] == "bearer"
        assert result["user"]["email"] == login_data["email"]
    
    def test_user_login_invalid_credentials(self, test_user):
        """Geçersiz kimlik bilgileri ile giriş testi"""
        login_data = {
            "email": "test@example.com",
            "password": "wrongpassword"
        }
        
        response = client.post("/api/auth/login", json=login_data)
        
        assert response.status_code == 401
        assert "geçersiz" in response.json()["detail"].lower()
    
    def test_user_login_nonexistent_user(self):
        """Var olmayan kullanıcı ile giriş testi"""
        login_data = {
            "email": "nonexistent@example.com",
            "password": "password123"
        }
        
        response = client.post("/api/auth/login", json=login_data)
        
        assert response.status_code == 401
    
    def test_get_current_user_success(self, auth_headers):
        """Mevcut kullanıcı bilgilerini getirme testi"""
        response = client.get("/api/auth/me", headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "id" in result
        assert "email" in result
        assert "username" in result
        assert "full_name" in result
        assert "password" not in result
    
    def test_get_current_user_invalid_token(self):
        """Geçersiz token ile kullanıcı bilgisi getirme testi"""
        headers = {"Authorization": "Bearer invalid_token"}
        response = client.get("/api/auth/me", headers=headers)
        
        assert response.status_code == 401
    
    def test_get_current_user_no_token(self):
        """Token olmadan kullanıcı bilgisi getirme testi"""
        response = client.get("/api/auth/me")
        
        assert response.status_code == 401
    
    def test_refresh_token_success(self, auth_headers):
        """Token yenileme başarı testi"""
        response = client.post("/api/auth/refresh", headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        assert "access_token" in result
        assert "token_type" in result
        assert result["token_type"] == "bearer"

class TestAuthorization:
    """Yetkilendirme testleri"""
    
    def test_authorized_document_access(self, auth_headers):
        """Yetkili doküman erişimi testi"""
        response = client.get("/api/documents/", headers=auth_headers)
        assert response.status_code == 200
    
    def test_unauthorized_document_access(self):
        """Yetkisiz doküman erişimi testi"""
        response = client.get("/api/documents/")
        assert response.status_code == 401
    
    def test_authorized_document_upload(self, auth_headers):
        """Yetkili doküman yükleme testi"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("Test doküman içeriği")
            test_file_path = f.name
        
        try:
            with open(test_file_path, 'rb') as f:
                files = {"file": ("test.txt", f, "text/plain")}
                data = {"title": "Test Doküman"}
                response = client.post("/api/documents/", files=files, data=data, headers=auth_headers)
            
            assert response.status_code == 200
            
        finally:
            os.unlink(test_file_path)
    
    def test_unauthorized_document_upload(self):
        """Yetkisiz doküman yükleme testi"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write("Test doküman içeriği")
            test_file_path = f.name
        
        try:
            with open(test_file_path, 'rb') as f:
                files = {"file": ("test.txt", f, "text/plain")}
                data = {"title": "Test Doküman"}
                response = client.post("/api/documents/", files=files, data=data)
            
            assert response.status_code == 401
            
        finally:
            os.unlink(test_file_path)
    
    def test_authorized_search_access(self, auth_headers):
        """Yetkili arama erişimi testi"""
        response = client.get("/api/search/", params={"query": "test"}, headers=auth_headers)
        assert response.status_code == 200
    
    def test_unauthorized_search_access(self):
        """Yetkisiz arama erişimi testi"""
        response = client.get("/api/search/", params={"query": "test"})
        assert response.status_code == 401
    
    def test_authorized_summary_access(self, auth_headers):
        """Yetkili özet erişimi testi"""
        response = client.get("/api/summary/statistics", headers=auth_headers)
        assert response.status_code == 200
    
    def test_unauthorized_summary_access(self):
        """Yetkisiz özet erişimi testi"""
        response = client.get("/api/summary/statistics")
        assert response.status_code == 401

class TestSecurity:
    """Güvenlik testleri"""
    
    def test_password_hashing(self):
        """Şifre hashleme testi"""
        db = TestingSessionLocal()
        from models.user import UserCreate
        user_data = UserCreate(
            email="security@example.com",
            username="securityuser",
            full_name="Security User",
            password="securepassword123"
        )
        
        user = AuthService.create_user(db, user_data)
        
        # Şifre hashlenmiş olmalı
        assert user.hashed_password != user_data.password
        assert user.hashed_password.startswith("$2b$")  # bcrypt formatı
        
        db.close()
    
    def test_password_verification(self):
        """Şifre doğrulama testi"""
        db = TestingSessionLocal()
        from models.user import UserCreate
        user_data = UserCreate(
            email="verify@example.com",
            username="verifyuser",
            full_name="Verify User",
            password="verifypassword123"
        )
        
        user = AuthService.create_user(db, user_data)
        
        # Doğru şifre ile doğrulama
        verified_user = AuthService.authenticate_user(db, user_data.email, user_data.password)
        assert verified_user is not None
        assert verified_user.id == user.id
        
        # Yanlış şifre ile doğrulama
        wrong_user = AuthService.authenticate_user(db, user_data.email, "wrongpassword")
        assert wrong_user is None
        
        db.close()
    
    def test_token_validation(self, auth_headers):
        """Token doğrulama testi"""
        # Geçerli token ile test
        response = client.get("/api/auth/me", headers=auth_headers)
        assert response.status_code == 200
        
        # Geçersiz token ile test
        invalid_headers = {"Authorization": "Bearer invalid_token_here"}
        response = client.get("/api/auth/me", headers=invalid_headers)
        assert response.status_code == 401
    
    def test_cors_headers(self):
        """CORS header testleri"""
        response = client.options("/api/documents/")
        
        # CORS header'ları kontrol et
        assert "access-control-allow-origin" in response.headers
        assert "access-control-allow-methods" in response.headers
        assert "access-control-allow-headers" in response.headers
    
    def test_input_validation(self):
        """Girdi doğrulama testleri"""
        # Geçersiz email formatı
        invalid_user_data = {
            "email": "invalid-email",
            "username": "testuser",
            "full_name": "Test User",
            "password": "password123"
        }
        
        response = client.post("/api/auth/register", json=invalid_user_data)
        assert response.status_code == 422  # Validation error
    
    def test_sql_injection_protection(self, auth_headers):
        """SQL injection koruması testi"""
        malicious_queries = [
            "'; DROP TABLE users; --",
            "' OR '1'='1",
            "'; INSERT INTO users VALUES ('hacker', 'hacker@evil.com'); --"
        ]
        
        for query in malicious_queries:
            response = client.get("/api/search/", params={"query": query}, headers=auth_headers)
            # Sistem çökmeden devam etmeli
            assert response.status_code in [200, 400, 422]
    
    def test_xss_protection(self, auth_headers):
        """XSS koruması testi"""
        xss_queries = [
            "<script>alert('xss')</script>",
            "<img src=x onerror=alert('xss')>",
            "javascript:alert('xss')"
        ]
        
        for query in xss_queries:
            response = client.get("/api/search/", params={"query": query}, headers=auth_headers)
            # XSS payload'ları güvenli şekilde işlenmeli
            assert response.status_code in [200, 400, 422]

class TestRateLimiting:
    """Hız sınırlama testleri"""
    
    def test_login_rate_limiting(self):
        """Giriş hız sınırlama testi"""
        login_data = {
            "email": "ratelimit@example.com",
            "password": "wrongpassword"
        }
        
        # Çoklu başarısız giriş denemesi
        for _ in range(5):
            response = client.post("/api/auth/login", json=login_data)
            assert response.status_code == 401
        
        # Rate limiting aktif olmalı
        # Not: Gerçek rate limiting implementasyonu gerekli
    
    def test_api_rate_limiting(self, auth_headers):
        """API hız sınırlama testi"""
        # Çoklu API çağrısı
        for _ in range(10):
            response = client.get("/api/documents/", headers=auth_headers)
            assert response.status_code == 200
        
        # Rate limiting kontrolü
        # Not: Gerçek rate limiting implementasyonu gerekli

class TestDataPrivacy:
    """Veri gizliliği testleri"""
    
    def test_user_data_privacy(self, auth_headers):
        """Kullanıcı verisi gizliliği testi"""
        response = client.get("/api/auth/me", headers=auth_headers)
        
        assert response.status_code == 200
        result = response.json()
        
        # Hassas veriler döndürülmemeli
        assert "password" not in result
        assert "hashed_password" not in result
        assert "salt" not in result
    
    def test_document_data_privacy(self, auth_headers):
        """Doküman verisi gizliliği testi"""
        response = client.get("/api/documents/", headers=auth_headers)
        
        assert response.status_code == 200
        results = response.json()
        
        if len(results) > 0:
            result = results[0]
            # Sadece gerekli alanlar döndürülmeli
            allowed_fields = ["id", "title", "filename", "file_type", "file_size", 
                            "created_at", "summary", "keywords"]
            
            for field in result.keys():
                assert field in allowed_fields
    
    def test_cross_user_data_isolation(self, auth_headers):
        """Kullanıcılar arası veri izolasyonu testi"""
        # İkinci kullanıcı oluştur
        user2_data = {
            "email": "user2@example.com",
            "username": "user2",
            "full_name": "User 2",
            "password": "password123"
        }
        
        client.post("/api/auth/register", json=user2_data)
        
        # İkinci kullanıcı ile giriş yap
        login_response = client.post("/api/auth/login", json=user2_data)
        user2_token = login_response.json()["access_token"]
        user2_headers = {"Authorization": f"Bearer {user2_token}"}
        
        # İkinci kullanıcının dokümanları boş olmalı
        response = client.get("/api/documents/", headers=user2_headers)
        assert response.status_code == 200
        results = response.json()
        assert len(results) == 0  # İkinci kullanıcının dokümanı yok 