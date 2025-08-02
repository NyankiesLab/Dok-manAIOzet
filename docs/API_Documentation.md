# Doküman Yönetim Sistemi API Dokümantasyonu

## Genel Bilgiler

**Base URL:** `http://localhost:8000/api`  
**Content Type:** `application/json`  
**Authentication:** Bearer Token

## Kimlik Doğrulama (Authentication)

### Kullanıcı Kaydı
```http
POST /auth/register
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "username": "username",
  "full_name": "Ad Soyad",
  "password": "password123"
}
```

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "username",
  "full_name": "Ad Soyad",
  "created_at": "2024-01-01T00:00:00"
}
```

### Kullanıcı Girişi
```http
POST /auth/login
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "username": "username",
    "full_name": "Ad Soyad"
  }
}
```

### Mevcut Kullanıcı Bilgileri
```http
GET /auth/me
```

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "username",
  "full_name": "Ad Soyad"
}
```

### Token Yenileme
```http
POST /auth/refresh
```

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer"
}
```

## Doküman Yönetimi (Documents)

### Doküman Yükleme
```http
POST /documents/
```

**Headers:**
```
Authorization: Bearer <token>
Content-Type: multipart/form-data
```

**Form Data:**
- `file`: Dosya (PDF, DOC, DOCX, TXT)
- `title`: Doküman başlığı (opsiyonel)

**Response:**
```json
{
  "id": 1,
  "title": "Doküman Başlığı",
  "filename": "document.pdf",
  "file_type": "pdf",
  "file_size": 1024,
  "created_at": "2024-01-01T00:00:00",
  "summary": null,
  "keywords": null
}
```

### Kullanıcının Dokümanlarını Listeleme
```http
GET /documents/
```

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `skip`: Atlanacak kayıt sayısı (default: 0)
- `limit`: Maksimum kayıt sayısı (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "title": "Doküman 1",
    "filename": "doc1.pdf",
    "file_type": "pdf",
    "file_size": 1024,
    "created_at": "2024-01-01T00:00:00",
    "summary": "Doküman özeti...",
    "keywords": "anahtar, kelimeler"
  }
]
```

### Belirli Dokümanı Getirme
```http
GET /documents/{document_id}
```

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "id": 1,
  "title": "Doküman Başlığı",
  "filename": "document.pdf",
  "file_type": "pdf",
  "file_size": 1024,
  "created_at": "2024-01-01T00:00:00",
  "summary": "Doküman özeti...",
  "keywords": "anahtar, kelimeler"
}
```

### Doküman Silme
```http
DELETE /documents/{document_id}
```

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "message": "Doküman başarıyla silindi"
}
```

## Arama (Search)

### Temel Arama
```http
GET /search/
```

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `query`: Arama sorgusu (zorunlu)
- `file_type`: Dosya türü filtresi (opsiyonel)
- `limit`: Sonuç sayısı (default: 20)
- `offset`: Başlangıç indeksi (default: 0)

**Response:**
```json
[
  {
    "id": 1,
    "title": "Doküman Başlığı",
    "filename": "document.pdf",
    "file_type": "pdf",
    "file_size": 1024,
    "created_at": "2024-01-01T00:00:00",
    "summary": "Doküman özeti...",
    "keywords": "anahtar, kelimeler"
  }
]
```

### AI Destekli Doğal Dil Arama
```http
GET /search/ai-search
```

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `query`: Doğal dil sorgusu (zorunlu)
- `limit`: Sonuç sayısı (default: 10)

**Response:**
```json
[
  {
    "document": {
      "id": 1,
      "title": "Doküman Başlığı",
      "filename": "document.pdf",
      "file_type": "pdf",
      "file_size": 1024,
      "created_at": "2024-01-01T00:00:00",
      "summary": "Doküman özeti...",
      "keywords": "anahtar, kelimeler"
    },
    "score": 0.95,
    "reason": "Bu doküman yapay zeka hakkında detaylı bilgi içeriyor"
  }
]
```

### Gelişmiş Arama
```http
GET /search/advanced-search
```

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `query`: Arama sorgusu (zorunlu)
- `file_type`: Dosya türü filtresi (opsiyonel)
- `date_from`: Başlangıç tarihi (opsiyonel)
- `date_to`: Bitiş tarihi (opsiyonel)
- `has_summary`: Özeti olan dokümanlar (opsiyonel)
- `limit`: Sonuç sayısı (default: 20)
- `offset`: Başlangıç indeksi (default: 0)

**Response:**
```json
{
  "documents": [
    {
      "id": 1,
      "title": "Doküman Başlığı",
      "filename": "document.pdf",
      "file_type": "pdf",
      "file_size": 1024,
      "created_at": "2024-01-01T00:00:00",
      "summary": "Doküman özeti...",
      "keywords": "anahtar, kelimeler"
    }
  ],
  "total_count": 1,
  "limit": 20,
  "offset": 0
}
```

### Arama Önerileri
```http
GET /search/suggestions
```

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `query`: Kısmi arama sorgusu (zorunlu)

**Response:**
```json
{
  "suggestions": ["Doküman 1", "Doküman 2"],
  "query": "doküman"
}
```

## Özetleme (Summary)

### AI Özet Oluşturma
```http
POST /summary/{document_id}/generate
```

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "message": "Özet başarıyla oluşturuldu",
  "summary": "Bu doküman yapay zeka ve makine öğrenmesi hakkında detaylı bilgi içeriyor...",
  "keywords": "yapay zeka, makine öğrenmesi, AI, ML",
  "document": {
    "id": 1,
    "title": "Doküman Başlığı",
    "filename": "document.pdf",
    "file_type": "pdf",
    "file_size": 1024,
    "created_at": "2024-01-01T00:00:00",
    "summary": "Bu doküman yapay zeka ve makine öğrenmesi hakkında detaylı bilgi içeriyor...",
    "keywords": "yapay zeka, makine öğrenmesi, AI, ML"
  }
}
```

### Doküman Özetini Getirme
```http
GET /summary/{document_id}/summary
```

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "document_id": 1,
  "title": "Doküman Başlığı",
  "summary": "Bu doküman yapay zeka ve makine öğrenmesi hakkında detaylı bilgi içeriyor...",
  "keywords": "yapay zeka, makine öğrenmesi, AI, ML",
  "has_summary": true
}
```

### Doküman Hakkında Soru Sorma
```http
POST /summary/{document_id}/ask
```

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- `question`: Soru (zorunlu)

**Response:**
```json
{
  "question": "Bu doküman ne hakkında?",
  "answer": "Bu doküman yapay zeka teknolojileri hakkında detaylı bilgi içeriyor...",
  "document_id": 1,
  "document_title": "Doküman Başlığı"
}
```

### Toplu Özetleme
```http
POST /summary/batch-summarize
```

**Headers:**
```
Authorization: Bearer <token>
```

**Request Body:**
```json
{
  "document_ids": [1, 2, 3]
}
```

**Response:**
```json
{
  "results": [
    {
      "document_id": 1,
      "success": true,
      "summary": "Doküman özeti...",
      "keywords": "anahtar, kelimeler"
    },
    {
      "document_id": 2,
      "success": false,
      "error": "Doküman bulunamadı"
    }
  ],
  "total_processed": 3,
  "successful": 2
}
```

### Özet İstatistikleri
```http
GET /summary/statistics
```

**Headers:**
```
Authorization: Bearer <token>
```

**Response:**
```json
{
  "total_documents": 10,
  "documents_with_summary": 7,
  "documents_without_summary": 3,
  "summary_percentage": 70.0
}
```

## Hata Kodları

| Kod | Açıklama |
|-----|----------|
| 200 | Başarılı |
| 400 | Geçersiz İstek |
| 401 | Yetkisiz Erişim |
| 404 | Bulunamadı |
| 422 | Doğrulama Hatası |
| 500 | Sunucu Hatası |

## Örnek Kullanım

### JavaScript (Axios)
```javascript
const API_BASE = 'http://localhost:8000/api';

// Giriş yap
const loginResponse = await axios.post(`${API_BASE}/auth/login`, {
  email: 'user@example.com',
  password: 'password123'
});

const token = loginResponse.data.access_token;

// Doküman yükle
const formData = new FormData();
formData.append('file', file);
formData.append('title', 'Doküman Başlığı');

const uploadResponse = await axios.post(`${API_BASE}/documents/`, formData, {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});

// Arama yap
const searchResponse = await axios.get(`${API_BASE}/search/`, {
  params: { query: 'yapay zeka' },
  headers: { 'Authorization': `Bearer ${token}` }
});

// Özet oluştur
const summaryResponse = await axios.post(`${API_BASE}/summary/1/generate`, {}, {
  headers: { 'Authorization': `Bearer ${token}` }
});
```

### Python (requests)
```python
import requests

API_BASE = 'http://localhost:8000/api'

# Giriş yap
login_response = requests.post(f'{API_BASE}/auth/login', json={
    'email': 'user@example.com',
    'password': 'password123'
})

token = login_response.json()['access_token']
headers = {'Authorization': f'Bearer {token}'}

# Doküman yükle
with open('document.pdf', 'rb') as f:
    files = {'file': f}
    data = {'title': 'Doküman Başlığı'}
    upload_response = requests.post(f'{API_BASE}/documents/', 
                                  files=files, data=data, headers=headers)

# Arama yap
search_response = requests.get(f'{API_BASE}/search/', 
                              params={'query': 'yapay zeka'}, 
                              headers=headers)

# Özet oluştur
summary_response = requests.post(f'{API_BASE}/summary/1/generate', 
                               headers=headers)
```

## Desteklenen Dosya Türleri

- **PDF** (.pdf)
- **Microsoft Word** (.doc, .docx)
- **Text** (.txt)

## Sınırlamalar

- Maksimum dosya boyutu: 10MB
- Desteklenen dosya türleri: PDF, DOC, DOCX, TXT
- Token geçerlilik süresi: 30 dakika
- Maksimum arama sonucu: 100 kayıt
- AI özetleme için minimum içerik: 50 karakter 