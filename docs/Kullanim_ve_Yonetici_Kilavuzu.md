# 📖 Kullanım ve Yönetici Kılavuzu
## Doküman Yönetim Sistemi

---

## 👥 Kullanıcı Kılavuzu

### 🚀 Hızlı Başlangıç

#### 1. Hesap Oluşturma
1. **Ana sayfaya gidin**: `http://localhost:3000`
2. **"Kayıt Ol" butonuna tıklayın**
3. **Bilgilerinizi doldurun**:
   - E-posta adresi
   - Kullanıcı adı
   - Şifre (en az 8 karakter)
   - Tam ad (opsiyonel)
4. **"Kayıt Ol" butonuna tıklayın**

#### 2. Giriş Yapma
1. **"Giriş Yap" butonuna tıklayın**
2. **E-posta ve şifrenizi girin**
3. **"Giriş Yap" butonuna tıklayın**

#### 3. İlk Dokümanınızı Yükleme
1. **Dashboard'a gidin**
2. **"Doküman Yükle" butonuna tıklayın**
3. **Dosyanızı seçin** (PDF, DOCX, TXT, DOC)
4. **Başlık girin**
5. **"Yükle" butonuna tıklayın**

---

### 📁 Doküman Yönetimi

#### Doküman Yükleme
**Desteklenen Dosya Türleri:**
- PDF (.pdf)
- Microsoft Word (.docx, .doc)
- Metin dosyaları (.txt)

**Dosya Boyutu Limiti:** 10MB

**Yükleme Adımları:**
1. Dashboard'da "Doküman Yükle" butonuna tıklayın
2. Dosya seçiciyi açın
3. Yüklemek istediğiniz dosyayı seçin
4. Doküman başlığını girin
5. "Yükle" butonuna tıklayın
6. Yükleme tamamlanana kadar bekleyin

**Önemli Notlar:**
- Dosya adı güvenli karakterler içermelidir
- Aynı isimde dosya varsa otomatik olarak yeniden adlandırılır
- Yükleme sırasında internet bağlantınızın stabil olduğundan emin olun

#### Doküman Listeleme
**Filtreleme Seçenekleri:**
- Dosya türü (PDF, DOCX, TXT, DOC)
- Tarih aralığı
- Dosya boyutu

**Sıralama Seçenekleri:**
- Yükleme tarihi (en yeni/en eski)
- Dosya adı (A-Z/Z-A)
- Dosya boyutu (büyükten küçüğe/küçükten büyüğe)

#### Doküman Arama
**Arama Özellikleri:**
- **Tam metin arama**: Doküman içeriğinde arama
- **Başlık arama**: Sadece doküman başlıklarında arama
- **Gelişmiş filtreler**: Dosya türü, tarih, boyut

**Arama İpuçları:**
- Büyük/küçük harf duyarlı değildir
- Türkçe karakterler desteklenir
- Çoklu kelime araması yapabilirsiniz
- Tırnak işareti ile tam eşleşme arayabilirsiniz

**Örnek Aramalar:**
```
rapor → "rapor" kelimesini içeren dokümanlar
"proje analizi" → Bu tam ifadeyi içeren dokümanlar
PDF:rapor → Sadece PDF dosyalarında "rapor" araması
```

---

### 🤖 AI Özetleme Özelliği

#### Özet Oluşturma
1. **Doküman detay sayfasına gidin**
2. **"Özet Oluştur" butonuna tıklayın**
3. **İşlemin tamamlanmasını bekleyin** (3-10 saniye)
4. **Oluşturulan özeti görüntüleyin**

#### Özet Özellikleri
- **Otomatik anahtar kelime çıkarma**
- **Türkçe özetleme**
- **Akıllı içerik analizi**
- **Güvenilirlik skoru**

#### Özet Kullanım İpuçları
- Uzun dokümanlar için daha detaylı özetler
- Teknik dokümanlar için özel analiz
- Anahtar kelimeler ile hızlı içerik tarama

---

### 🔍 Gelişmiş Arama

#### Arama Filtreleri
**Dosya Türü Filtresi:**
- Tüm dosyalar
- Sadece PDF
- Sadece Word dokümanları
- Sadece metin dosyaları

**Tarih Filtresi:**
- Bugün
- Bu hafta
- Bu ay
- Özel tarih aralığı

**Boyut Filtresi:**
- 1MB'dan küçük
- 1-5MB arası
- 5MB'dan büyük

#### Arama Sonuçları
**Sonuç Bilgileri:**
- Doküman başlığı
- Dosya türü ve boyutu
- Yükleme tarihi
- Eşleşme skoru
- Özet (varsa)

**Sonuç İşlemleri:**
- Dokümanı görüntüle
- Özet oluştur
- İndir
- Paylaş

---

### 👤 Profil Yönetimi

#### Profil Bilgilerini Güncelleme
1. **Sağ üst köşedeki profil menüsüne tıklayın**
2. **"Profil" seçeneğini seçin**
3. **Bilgilerinizi güncelleyin**
4. **"Kaydet" butonuna tıklayın**

#### Şifre Değiştirme
1. **Profil sayfasına gidin**
2. **"Şifre Değiştir" bölümünü bulun**
3. **Mevcut şifrenizi girin**
4. **Yeni şifrenizi girin**
5. **Şifreyi tekrar girin**
6. **"Şifre Değiştir" butonuna tıklayın**

#### Hesap Ayarları
**Bildirim Ayarları:**
- E-posta bildirimleri
- Sistem bildirimleri
- Özetleme tamamlandığında bildirim

**Gizlilik Ayarları:**
- Profil görünürlüğü
- Doküman paylaşım ayarları
- Arama geçmişi

---

## 🔧 Yönetici Kılavuzu

### 🛠️ Sistem Kurulumu

#### Gereksinimler
**Minimum Sistem Gereksinimleri:**
- CPU: 2 çekirdek
- RAM: 4GB
- Disk: 20GB boş alan
- İşletim Sistemi: Linux, Windows, macOS

**Önerilen Sistem Gereksinimleri:**
- CPU: 4 çekirdek
- RAM: 8GB
- Disk: 100GB SSD
- İşletim Sistemi: Ubuntu 20.04 LTS

#### Docker ile Kurulum
```bash
# 1. Projeyi klonlayın
git clone https://github.com/yourusername/document-management-system.git
cd document-management-system

# 2. Environment dosyalarını kopyalayın
cp backend/env.example backend/.env
cp frontend/env.example frontend/.env

# 3. .env dosyalarını düzenleyin
# backend/.env dosyasında GEMINI_API_KEY=your-api-key-here

# 4. Docker ile çalıştırın
docker-compose up --build -d

# 5. Servisleri kontrol edin
docker-compose ps
```

#### Manuel Kurulum
```bash
# Backend Kurulumu
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp env.example .env
# .env dosyasını düzenleyin
python main.py

# Frontend Kurulumu (yeni terminal)
cd frontend
npm install
cp env.example .env
npm start
```

---

### ⚙️ Konfigürasyon

#### Environment Variables
**Backend (.env):**
```env
# API Keys
GEMINI_API_KEY=your-gemini-api-key-here
SECRET_KEY=your-super-secret-key-here

# Database
DATABASE_URL=sqlite:///./document_db.sqlite

# Security
ALLOWED_ORIGINS=["http://localhost:3000"]

# File Upload
MAX_FILE_SIZE=10485760  # 10MB in bytes
UPLOAD_DIR=uploads

# AI Service
AI_TIMEOUT=30
AI_MAX_TOKENS=30720
```

**Frontend (.env):**
```env
REACT_APP_API_URL=http://localhost:5000
REACT_APP_VERSION=1.0.0
```

#### API Key Alma
1. [Google AI Studio](https://makersuite.google.com/app/apikey) adresine gidin
2. Google hesabınızla giriş yapın
3. "Create API Key" butonuna tıklayın
4. Oluşturulan API key'i kopyalayın
5. `.env` dosyasına ekleyin: `GEMINI_API_KEY=your-key-here`

---

### 🔍 Sistem İzleme

#### Log Dosyaları
**Backend Logları:**
```bash
# Docker ile
docker-compose logs -f backend

# Manuel kurulum
tail -f backend/logs/app.log
```

**Frontend Logları:**
```bash
# Docker ile
docker-compose logs -f frontend

# Manuel kurulum
# Browser Developer Tools > Console
```

#### Sistem Metrikleri
**Performans Metrikleri:**
- CPU kullanımı
- RAM kullanımı
- Disk kullanımı
- Network trafiği

**Uygulama Metrikleri:**
- API yanıt süreleri
- Hata oranları
- Aktif kullanıcı sayısı
- Doküman yükleme sayısı

#### Monitoring Araçları
**Önerilen Araçlar:**
- **Prometheus**: Metrik toplama
- **Grafana**: Görselleştirme
- **ELK Stack**: Log analizi
- **Sentry**: Hata takibi

---

### 🔒 Güvenlik Yönetimi

#### Güvenlik Kontrolleri
**Düzenli Kontroller:**
- [ ] Güvenlik güncellemeleri
- [ ] API key rotasyonu
- [ ] Log analizi
- [ ] Dosya tarama
- [ ] Erişim kontrolü

#### Güvenlik Ayarları
**CORS Yapılandırması:**
```python
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://yourdomain.com"
]
```

**Rate Limiting:**
```python
RATE_LIMIT = "100/minute"
RATE_LIMIT_STORAGE_URL = "memory://"
```

**File Upload Güvenliği:**
```python
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".doc", ".txt"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
```

#### Güvenlik İzleme
**Güvenlik Logları:**
- Başarısız giriş denemeleri
- Şüpheli dosya yüklemeleri
- API kullanım anomalileri
- IP adresi kısıtlamaları

---

### 💾 Veritabanı Yönetimi

#### Veritabanı Bakımı
**Günlük Bakım:**
```bash
# SQLite veritabanı optimizasyonu
sqlite3 backend/document_db.sqlite "VACUUM;"

# Backup oluşturma
cp backend/document_db.sqlite backup/document_db_$(date +%Y%m%d).sqlite
```

**Aylık Bakım:**
```bash
# Veritabanı analizi
sqlite3 backend/document_db.sqlite "ANALYZE;"

# İndeks yenileme
sqlite3 backend/document_db.sqlite "REINDEX;"
```

#### Veritabanı Yedekleme
**Otomatik Yedekleme Scripti:**
```bash
#!/bin/bash
BACKUP_DIR="/backup/database"
DATE=$(date +%Y%m%d_%H%M%S)
SOURCE_DB="backend/document_db.sqlite"
BACKUP_FILE="$BACKUP_DIR/document_db_$DATE.sqlite"

# Yedekleme dizini oluştur
mkdir -p $BACKUP_DIR

# Veritabanını yedekle
cp $SOURCE_DB $BACKUP_FILE

# Eski yedekleri temizle (30 günden eski)
find $BACKUP_DIR -name "document_db_*.sqlite" -mtime +30 -delete

echo "Backup completed: $BACKUP_FILE"
```

#### Veritabanı İstatistikleri
**Tablo İstatistikleri:**
```sql
-- Kullanıcı sayısı
SELECT COUNT(*) FROM users;

-- Doküman sayısı
SELECT COUNT(*) FROM documents;

-- Dosya türü dağılımı
SELECT file_type, COUNT(*) FROM documents GROUP BY file_type;

-- En aktif kullanıcılar
SELECT u.username, COUNT(d.id) as doc_count 
FROM users u 
JOIN documents d ON u.id = d.user_id 
GROUP BY u.id 
ORDER BY doc_count DESC 
LIMIT 10;
```

---

### 📊 Raporlama

#### Sistem Raporları
**Günlük Rapor:**
```bash
# Sistem durumu
systemctl status document-management-system

# Disk kullanımı
df -h

# Memory kullanımı
free -h

# CPU kullanımı
top -bn1 | grep "Cpu(s)"
```

**Aylık Rapor:**
```sql
-- Kullanıcı istatistikleri
SELECT 
    COUNT(*) as total_users,
    COUNT(CASE WHEN created_at >= date('now', '-30 days') THEN 1 END) as new_users,
    COUNT(CASE WHEN last_login >= date('now', '-7 days') THEN 1 END) as active_users
FROM users;

-- Doküman istatistikleri
SELECT 
    COUNT(*) as total_documents,
    SUM(file_size) as total_storage,
    AVG(file_size) as avg_file_size
FROM documents;
```

#### Kullanıcı Raporları
**Kullanıcı Aktivite Raporu:**
```sql
-- En aktif kullanıcılar
SELECT 
    u.username,
    u.email,
    COUNT(d.id) as document_count,
    MAX(d.created_at) as last_upload
FROM users u
LEFT JOIN documents d ON u.id = d.user_id
GROUP BY u.id
ORDER BY document_count DESC;
```

**Dosya Türü Analizi:**
```sql
-- Dosya türü dağılımı
SELECT 
    file_type,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM documents), 2) as percentage
FROM documents
GROUP BY file_type
ORDER BY count DESC;
```

---

### 🚨 Sorun Giderme

#### Yaygın Sorunlar

**1. Uygulama Başlatılamıyor**
```bash
# Docker loglarını kontrol edin
docker-compose logs

# Port çakışmasını kontrol edin
netstat -tulpn | grep :5000
netstat -tulpn | grep :3000

# Servisleri yeniden başlatın
docker-compose down
docker-compose up --build
```

**2. API Key Hatası**
```bash
# .env dosyasını kontrol edin
cat backend/.env | grep GEMINI_API_KEY

# API key'i test edin
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://generativelanguage.googleapis.com/v1beta/models
```

**3. Dosya Yükleme Hatası**
```bash
# Disk alanını kontrol edin
df -h

# Upload dizini izinlerini kontrol edin
ls -la backend/uploads/

# Dosya boyutu limitini kontrol edin
grep MAX_FILE_SIZE backend/.env
```

**4. Veritabanı Hatası**
```bash
# Veritabanı dosyasını kontrol edin
ls -la backend/document_db.sqlite

# Veritabanı bütünlüğünü kontrol edin
sqlite3 backend/document_db.sqlite "PRAGMA integrity_check;"

# Veritabanını yeniden oluşturun (dikkatli olun!)
rm backend/document_db.sqlite
docker-compose up --build
```

#### Performans Sorunları

**1. Yavaş API Yanıtları**
```bash
# CPU kullanımını kontrol edin
htop

# Memory kullanımını kontrol edin
free -h

# Database performansını kontrol edin
sqlite3 backend/document_db.sqlite "EXPLAIN QUERY PLAN SELECT * FROM documents;"
```

**2. Yüksek Disk Kullanımı**
```bash
# Disk kullanımını analiz edin
du -sh backend/uploads/*

# Eski dosyaları temizleyin
find backend/uploads/ -mtime +90 -delete

# Veritabanı boyutunu kontrol edin
ls -lh backend/document_db.sqlite
```

---

### 🔄 Güncelleme ve Bakım

#### Sistem Güncellemeleri
**Güvenlik Güncellemeleri:**
```bash
# Sistem paketlerini güncelleyin
sudo apt update && sudo apt upgrade

# Docker imajlarını güncelleyin
docker-compose pull
docker-compose up --build -d
```

**Uygulama Güncellemeleri:**
```bash
# Kodu güncelleyin
git pull origin main

# Bağımlılıkları güncelleyin
# Backend
cd backend
pip install -r requirements.txt --upgrade

# Frontend
cd frontend
npm update
```

#### Bakım Zamanlaması
**Günlük Bakım:**
- Log dosyalarını kontrol edin
- Disk kullanımını kontrol edin
- Sistem performansını kontrol edin

**Haftalık Bakım:**
- Veritabanı yedekleme
- Güvenlik güncellemeleri
- Performans analizi

**Aylık Bakım:**
- Kapsamlı sistem kontrolü
- Raporlama
- Kullanıcı istatistikleri

---

### 📞 Destek ve İletişim

#### Teknik Destek
**E-posta:** support@yourcompany.com
**Telefon:** +90 XXX XXX XX XX
**Çalışma Saatleri:** Pazartesi-Cuma 09:00-18:00

#### Acil Durumlar
**7/24 Destek:** +90 XXX XXX XX XX
**E-posta:** emergency@yourcompany.com

#### Dokümantasyon
- **API Dokümantasyonu:** http://localhost:5000/docs
- **GitHub Repository:** https://github.com/yourusername/document-management-system
- **Wiki:** https://github.com/yourusername/document-management-system/wiki

---

*Son Güncelleme: 2024-01-XX*
*Kılavuz Versiyonu: 1.0.0*
*Sistem Versiyonu: 1.0.0* 