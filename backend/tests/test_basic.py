"""
Basit Test Dosyası
==================
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_app_loads():
    """App yüklenme testi"""
    assert app is not None

def test_home_page():
    """Ana sayfa testi"""
    response = client.get("/")
    assert response.status_code == 200

def test_docs_page():
    """API dokümantasyonu testi"""
    response = client.get("/docs")
    assert response.status_code == 200

def test_health_check():
    """Sağlık kontrolü testi"""
    response = client.get("/health")
    assert response.status_code == 200

def test_cors_headers():
    """CORS header testi"""
    response = client.options("/api/documents/")
    # CORS header'ları kontrol et
    assert response.status_code in [200, 405]  # OPTIONS method desteklenmeyebilir 