"""
Uygulama Konfigürasyonu
=======================
"""

from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # Uygulama ayarları
    APP_NAME: str = "Doküman Yönetim Sistemi"
    DEBUG: bool = True
    VERSION: str = "1.0.0"
    
    # Veritabanı
    DATABASE_URL: str = "postgresql://user:password@localhost/document_db"
    
    # JWT ayarları
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS ayarları
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:5000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5000",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8080",
        "http://frontend:3000",
        "http://backend:5000"
    ]
    
    # Dosya yükleme ayarları
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE: int = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS: List[str] = [".pdf", ".docx", ".txt", ".doc"]
    
    # Gemini API ayarları
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL: str = "gemini-1.5-pro"
    
    # Redis ayarları (opsiyonel)
    REDIS_URL: str = "redis://localhost:6379"
    
    # Log ayarları
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Settings instance'ı oluştur
settings = Settings()

# Gerekli dizinleri oluştur
os.makedirs(settings.UPLOAD_DIR, exist_ok=True) 