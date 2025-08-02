"""
Veritabanı Konfigürasyonu
=========================
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Veritabanı engine oluştur
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # SQL loglarını göster
    pool_pre_ping=True,   # Bağlantı kontrolü
    pool_recycle=300      # 5 dakikada bir bağlantıyı yenile
)

# Session factory oluştur
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class oluştur
Base = declarative_base()

def get_db():
    """Veritabanı session'ı döndür"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 