"""
Doküman API Route'ları
======================
"""

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from models.document import DocumentResponse
from models.user import User
from services.auth_service import AuthService
from services.document_service import DocumentService

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

@router.post("/", response_model=DocumentResponse)
async def upload_document(
    file: UploadFile = File(...),
    title: str = Form(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Doküman yükle"""
    try:
        if not file.filename:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Dosya adı gerekli"
            )
        
        document = DocumentService.create_document(db, current_user, file, title)
        return DocumentResponse.from_orm(document)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Dosya yükleme hatası: {str(e)}"
        )

@router.get("/", response_model=List[DocumentResponse])
async def get_documents(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Kullanıcının dokümanlarını getir"""
    try:
        documents = DocumentService.get_user_documents(db, current_user.id, skip, limit)
        return [DocumentResponse.from_orm(doc) for doc in documents]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Dokümanlar alınamadı: {str(e)}"
        )

@router.get("/{document_id}", response_model=DocumentResponse)
async def get_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Belirli bir dokümanı getir"""
    try:
        document = DocumentService.get_document(db, document_id, current_user.id)
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
            detail=f"Doküman alınamadı: {str(e)}"
        )

@router.delete("/{document_id}")
async def delete_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Dokümanı sil"""
    try:
        success = DocumentService.delete_document(db, document_id, current_user.id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doküman bulunamadı"
            )
        return {"message": "Doküman başarıyla silindi"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Doküman silinemedi: {str(e)}"
        )

@router.post("/{document_id}/process")
async def process_document_with_ai(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Dokümanı AI ile işle"""
    try:
        document = await DocumentService.process_document_with_ai(db, document_id, current_user.id)
        return {
            "message": "Doküman AI ile işlendi",
            "document": DocumentResponse.from_orm(document)
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"AI işleme hatası: {str(e)}"
        )

@router.get("/{document_id}/download")
async def download_document(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Dokümanı indir"""
    try:
        document = DocumentService.get_document(db, document_id, current_user.id)
        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doküman bulunamadı"
            )
        
        # Dosya yolunu döndür (gerçek uygulamada dosya stream edilir)
        return {
            "file_path": document.file_path,
            "filename": document.filename,
            "file_size": document.file_size
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Doküman indirilemedi: {str(e)}"
        ) 