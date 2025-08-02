"""
Doküman Modeli
==============
"""

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class Document(Base):
    """Doküman veritabanı modeli"""
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    file_size = Column(Integer, nullable=False)  # bytes
    file_type = Column(String, nullable=False)   # pdf, docx, txt
    content = Column(Text, nullable=True)        # Çıkarılan metin
    summary = Column(Text, nullable=True)        # AI özeti
    keywords = Column(Text, nullable=True)       # Anahtar kelimeler (JSON)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # İlişkiler
    user = relationship("User", back_populates="documents")

class DocumentCreate(BaseModel):
    """Doküman oluşturma şeması"""
    title: str
    filename: str
    file_size: int
    file_type: str

class DocumentUpdate(BaseModel):
    """Doküman güncelleme şeması"""
    title: Optional[str] = None
    content: Optional[str] = None
    summary: Optional[str] = None
    keywords: Optional[str] = None

class DocumentResponse(BaseModel):
    """Doküman yanıt şeması"""
    id: int
    title: str
    filename: str
    file_size: int
    file_type: str
    content: Optional[str] = None
    summary: Optional[str] = None
    keywords: Optional[str] = None
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class DocumentSearch(BaseModel):
    """Doküman arama şeması"""
    query: str
    file_type: Optional[str] = None
    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None
    limit: int = 20
    offset: int = 0

class DocumentSummary(BaseModel):
    """Doküman özet şeması"""
    document_id: int
    summary: str
    keywords: List[str]
    confidence_score: Optional[float] = None 