# 📚 Doküman Yönetim Sistemi

FastAPI backend ve React frontend ile geliştirilmiş modern doküman yönetim sistemi. AI destekli özetleme ve gelişmiş doküman yönetimi özellikleri.

## 🌟 Özellikler

- ✅ **Kullanıcı Kimlik Doğrulama** - JWT tabanlı güvenli giriş
- ✅ **Doküman Yükleme** - PDF, DOCX, TXT, DOC desteği
- ✅ **Doküman Listeleme** - Filtreleme ve arama
- ✅ **AI Özetleme** - Google Gemini API ile otomatik özet
- ✅ **Responsive Tasarım** - Modern ve kullanıcı dostu arayüz
- ✅ **Docker Desteği** - Kolay kurulum ve deployment
- ✅ **Güvenlik** - Dosya türü kontrolü ve boyut sınırlaması

## 🚀 Hızlı Başlangıç

### Docker ile (Önerilen)

```bash
# Projeyi klonlayın
git clone https://github.com/yourusername/document-management-system.git
cd document-management-system

# Environment dosyalarını kopyalayın
cp backend/env.example backend/.env
cp frontend/env.example frontend/.env

# .env dosyalarını düzenleyin (API key ekleyin)
# backend/.env dosyasında GEMINI_API_KEY=your-api-key-here

# Docker ile çalıştırın
docker-compose up --build
```

### Manuel Kurulum

```bash
# Backend
cd backend
pip install -r requirements.txt
cp env.example .env
# .env dosyasını düzenleyin
python main.py

# Frontend (yeni terminal)
cd frontend
npm install
cp env.example .env
npm start
```

## 🔧 Konfigürasyon

### Environment Variables

**Backend (.env):**
```env
GEMINI_API_KEY=your-gemini-api-key-here
SECRET_KEY=your-super-secret-key
DATABASE_URL=sqlite:///./document_db.sqlite
```

**Frontend (.env):**
```env
REACT_APP_API_URL=http://localhost:5000
```

### API Key Alma

1. [Google AI Studio](https://makersuite.google.com/app/apikey) adresine gidin
2. Yeni API key oluşturun
3. `.env` dosyasına ekleyin: `GEMINI_API_KEY=your-key-here`

## 📁 Proje Yapısı

```
document-management-system/
├── backend/                 # FastAPI Backend
│   ├── api/                # API Routes
│   ├── app/                # App Config
│   ├── models/             # Database Models
│   ├── services/           # Business Logic
│   ├── uploads/            # Uploaded Files
│   ├── Dockerfile          # Backend Container
│   └── requirements.txt    # Python Dependencies
├── frontend/               # React Frontend
│   ├── src/               # Source Code
│   ├── public/            # Static Files
│   ├── Dockerfile         # Frontend Container
│   └── package.json       # Node Dependencies
├── docker-compose.yml      # Docker Orchestration
└── README.md              # Project Documentation
```

## 🐳 Docker Komutları

```bash
# Uygulamayı başlat
docker-compose up --build

# Arka planda çalıştır
docker-compose up -d

# Servisleri durdur
docker-compose down

# Logları görüntüle
docker-compose logs -f

# Belirli servisin logları
docker-compose logs -f backend
docker-compose logs -f frontend
```

## 🔗 API Endpoints

- **Authentication**: `/api/auth/`
- **Documents**: `/api/documents/`
- **Summary**: `/api/summary/`
- **API Docs**: `http://localhost:5000/docs`

## 🛠️ Teknoloji Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM ve veritabanı yönetimi
- **SQLite** - Hafif veritabanı
- **JWT** - Kimlik doğrulama
- **Google Gemini API** - AI entegrasyonu

### Frontend
- **React** - Modern UI framework
- **TypeScript** - Tip güvenliği
- **Tailwind CSS** - Styling
- **Axios** - API calls
- **Lucide React** - İkonlar

## 🔒 Güvenlik

- JWT tabanlı kimlik doğrulama
- Dosya türü kontrolü
- Dosya boyutu sınırlaması (10MB)
- CORS yapılandırması
- Environment variables ile güvenli konfigürasyon

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Commit yapın (`git commit -m 'Add amazing feature'`)
4. Push yapın (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 🔍 Sorun Giderme

### Port çakışması
```bash
# docker-compose.yml dosyasında port mapping'i değiştirin
ports:
  - "5001:5000"  # Backend için
  - "3001:3000"  # Frontend için
```

### API Key sorunu
```bash
# .env dosyasını kontrol edin
GEMINI_API_KEY=your-actual-api-key
```

### Veritabanı sıfırlama
```bash
docker-compose down
rm backend/document_db.sqlite
docker-compose up --build
```

## 📞 İletişim

- **GitHub**: [Repository Link]
- **Sorular**: [GitHub Issues]

---

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!

## 🚀 Docker ile Çalıştırma

### Gereksinimler
- Docker
- Docker Compose

### Kurulum ve Çalıştırma

1. **Projeyi klonlayın:**
```bash
git clone <repository-url>
cd document-management-system
```

2. **Docker Compose ile çalıştırın:**
```bash
docker-compose up --build
```

3. **Uygulamaya erişim:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- API Dokümantasyonu: http://localhost:5000/docs

### Servisler

- **Backend (FastAPI)**: Port 5000
- **Frontend (React)**: Port 3000

### Veritabanı
- SQLite veritabanı kullanılıyor
- Veritabanı dosyası: `backend/document_db.sqlite`

### Dosya Yükleme
- Yüklenen dosyalar: `backend/uploads/` klasöründe saklanır
- Docker volume ile kalıcı hale getirilmiştir

## 🛠️ Geliştirme

### Backend Geliştirme
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend Geliştirme
```bash
cd frontend
npm install
npm start
```

## 📁 Proje Yapısı

```
document-management-system/
├── backend/
│   ├── api/
│   ├── app/
│   ├── models/
│   ├── services/
│   ├── uploads/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
└── README.md
```

## 🔧 Özellikler

- ✅ Kullanıcı kimlik doğrulama
- ✅ Doküman yükleme (PDF, DOCX, TXT, DOC)
- ✅ Doküman listeleme ve filtreleme
- ✅ AI destekli doküman özetleme
- ✅ Responsive tasarım
- ✅ Docker desteği

## 🐳 Docker Komutları

### Servisleri başlatma
```bash
docker-compose up
```

### Arka planda çalıştırma
```bash
docker-compose up -d
```

### Servisleri durdurma
```bash
docker-compose down
```

### Logları görüntüleme
```bash
docker-compose logs -f
```

### Belirli servisin logları
```bash
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Servisleri yeniden oluşturma
```bash
docker-compose up --build
```

## 🔍 Sorun Giderme

### Port çakışması
Eğer port 3000 veya 5000 kullanımdaysa, `docker-compose.yml` dosyasında port mapping'i değiştirin.

### Veritabanı sıfırlama
```bash
docker-compose down
rm backend/document_db.sqlite
docker-compose up --build
```

### Node modules sorunu
```bash
docker-compose down
docker-compose up --build --force-recreate frontend
``` 