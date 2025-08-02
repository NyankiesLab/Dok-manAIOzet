"""
Doküman Listeleme API Route'ları
================================
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from models.document import Document, DocumentResponse
from models.user import User
from services.auth_service import AuthService

router = APIRouter()
security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Mevcut kullanıcıyı al"""
    user = AuthService.get_current_user(db, credentials.credentials)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Geçersiz token"
        )
    return user

@router.get("/", response_model=List[DocumentResponse])
async def list_documents(
    limit: int = Query(20, description="Sonuç sayısı"),
    offset: int = Query(0, description="Başlangıç indeksi"),
    file_type: Optional[str] = Query(None, description="Dosya türü filtresi"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Kullanıcının dokümanlarını listele"""
    try:
        # Temel filtreler
        filters = [Document.user_id == current_user.id]
        
        # Dosya türü filtresi
        if file_type:
            filters.append(Document.file_type == file_type)
        
        # Sorguyu çalıştır
        documents = db.query(Document).filter(
            *filters
        ).offset(offset).limit(limit).all()
        
        return [DocumentResponse.from_orm(doc) for doc in documents]
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Doküman listeleme hatası: {str(e)}"
        )

@router.get("/{document_id}", response_model=DocumentResponse)
async def get_document_by_id(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """ID ile doküman getir"""
    try:
        document = db.query(Document).filter(
            Document.id == document_id,
            Document.user_id == current_user.id
        ).first()
        
        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doküman bulunamadı"
            )
        
        return DocumentResponse.from_orm(document)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Doküman getirme hatası: {str(e)}"
        )

@router.get("/count/total")
async def get_document_count(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Kullanıcının toplam doküman sayısını getir"""
    try:
        count = db.query(Document).filter(
            Document.user_id == current_user.id
        ).count()
        
        return {"total_count": count}
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Sayım hatası: {str(e)}"
        ) 