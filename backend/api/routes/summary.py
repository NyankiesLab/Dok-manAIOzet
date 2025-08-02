"""
Özet API Route'ları
===================
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from models.document import Document, DocumentResponse
from models.user import User
from services.auth_service import AuthService
from services.ai_service import AIService

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

@router.post("/{document_id}/generate")
async def generate_summary(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Doküman için özet oluştur"""
    try:
        # Dokümanı kontrol et
        document = db.query(Document).filter(
            Document.id == document_id,
            Document.user_id == current_user.id
        ).first()
        
        if not document:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doküman bulunamadı"
            )
        
        if not document.content:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Doküman içeriği bulunamadı"
            )
        
        # AI ile özet oluştur
        ai_service = AIService()
        summary, keywords = await ai_service.generate_summary_and_keywords(document.content)
        
        # Dokümanı güncelle
        document.summary = summary
        document.keywords = keywords
        db.commit()
        db.refresh(document)
        
        return {
            "message": "Özet başarıyla oluşturuldu",
            "summary": summary,
            "keywords": keywords,
            "document": DocumentResponse.from_orm(document)
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Özet oluşturma hatası: {str(e)}"
        )

@router.get("/{document_id}/summary")
async def get_document_summary(
    document_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Doküman özetini getir"""
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
        
        return {
            "document_id": document_id,
            "title": document.title,
            "summary": document.summary,
            "keywords": document.keywords,
            "has_summary": document.summary is not None
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Özet getirme hatası: {str(e)}"
        )

@router.post("/{document_id}/ask")
async def ask_question(
    document_id: int,
    question: str = Query(..., description="Soru"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Doküman hakkında soru sor"""
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
        
        if not document.content:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Doküman içeriği bulunamadı"
            )
        
        # AI ile soru cevapla
        ai_service = AIService()
        answer = await ai_service.answer_question(question, document.content)
        
        return {
            "question": question,
            "answer": answer,
            "document_id": document_id,
            "document_title": document.title
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Soru cevaplama hatası: {str(e)}"
        )

@router.post("/batch-summarize")
async def batch_summarize_documents(
    document_ids: List[int],
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Birden fazla doküman için toplu özet oluştur"""
    try:
        results = []
        ai_service = AIService()
        
        for doc_id in document_ids:
            try:
                document = db.query(Document).filter(
                    Document.id == doc_id,
                    Document.user_id == current_user.id
                ).first()
                
                if not document or not document.content:
                    results.append({
                        "document_id": doc_id,
                        "success": False,
                        "error": "Doküman bulunamadı veya içerik yok"
                    })
                    continue
                
                # Özet oluştur
                summary, keywords = await ai_service.generate_summary_and_keywords(document.content)
                
                # Dokümanı güncelle
                document.summary = summary
                document.keywords = keywords
                db.commit()
                
                results.append({
                    "document_id": doc_id,
                    "success": True,
                    "summary": summary,
                    "keywords": keywords
                })
                
            except Exception as e:
                results.append({
                    "document_id": doc_id,
                    "success": False,
                    "error": str(e)
                })
        
        return {
            "results": results,
            "total_processed": len(document_ids),
            "successful": len([r for r in results if r["success"]])
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Toplu özet oluşturma hatası: {str(e)}"
        )

@router.get("/statistics")
async def get_summary_statistics(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Özet istatistikleri"""
    try:
        total_documents = db.query(Document).filter(
            Document.user_id == current_user.id
        ).count()
        
        documents_with_summary = db.query(Document).filter(
            Document.user_id == current_user.id,
            Document.summary.isnot(None)
        ).count()
        
        documents_without_summary = total_documents - documents_with_summary
        
        return {
            "total_documents": total_documents,
            "documents_with_summary": documents_with_summary,
            "documents_without_summary": documents_without_summary,
            "summary_percentage": (documents_with_summary / total_documents * 100) if total_documents > 0 else 0
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"İstatistik hatası: {str(e)}"
        ) 