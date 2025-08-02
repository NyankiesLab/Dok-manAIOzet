"""
Doküman Yönetim Sistemi - Ana Uygulama
========================================

FastAPI tabanlı backend uygulaması
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from contextlib import asynccontextmanager

from app.database import engine, Base
from app.config import settings
from api.routes import auth, documents, search, summary

# Veritabanı tablolarını oluştur
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Uygulama başlangıcında
    Base.metadata.create_all(bind=engine)
    yield
    # Uygulama kapanışında
    pass

# FastAPI uygulamasını oluştur
app = FastAPI(
    title="Doküman Yönetim Sistemi",
    description="Doğal dilde arama ve özetleme yapan doküman yönetim sistemi",
    version="1.0.0",
    lifespan=lifespan
)

# CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API route'larını dahil et
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(search.router, prefix="/api/search", tags=["Search"])
app.include_router(summary.router, prefix="/api/summary", tags=["Summary"])

# Statik dosyalar için
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    """Ana sayfa - static dosyayı serve et"""
    return FileResponse("static/index.html")

@app.get("/health")
async def health_check():
    """Sağlık kontrolü"""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=5000,
        reload=True
    ) 