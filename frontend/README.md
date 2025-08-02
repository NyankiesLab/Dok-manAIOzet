# Doküman Forum Frontend

Modern React uygulaması ile geliştirilmiş AI destekli doküman yönetim sistemi frontend'i.

## 🚀 Özellikler

- **Modern UI/UX**: Tailwind CSS ile tasarlanmış responsive arayüz
- **TypeScript**: Tip güvenliği ile geliştirilmiş
- **React Router**: Sayfa yönlendirmeleri
- **Axios**: API entegrasyonu
- **Lucide React**: Modern ikonlar
- **Context API**: Durum yönetimi

## 🛠️ Teknoloji Stack

- **React 18**: Modern UI framework
- **TypeScript**: Tip güvenliği
- **Tailwind CSS**: Utility-first CSS framework
- **React Router**: Sayfa yönlendirmeleri
- **Axios**: HTTP client
- **Lucide React**: İkonlar

## 📋 Gereksinimler

- Node.js 16+
- npm veya yarn

## 🚀 Kurulum

### 1. Bağımlılıkları Yükleyin
```bash
cd frontend
npm install
```

### 2. Uygulamayı Çalıştırın
```bash
npm start
```

Uygulama http://localhost:3000 adresinde çalışacaktır.

## 📁 Proje Yapısı

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   └── Navbar.tsx
│   ├── contexts/
│   │   └── AuthContext.tsx
│   ├── pages/
│   │   ├── Home.tsx
│   │   ├── Login.tsx
│   │   ├── Register.tsx
│   │   ├── Dashboard.tsx
│   │   ├── DocumentUpload.tsx
│   │   ├── DocumentSearch.tsx
│   │   └── DocumentSummary.tsx
│   ├── App.tsx
│   ├── index.tsx
│   └── index.css
├── package.json
├── tailwind.config.js
└── postcss.config.js
```

## 🎨 Sayfalar

### Ana Sayfa (Home)
- Uygulama tanıtımı
- Özellikler listesi
- Hızlı erişim linkleri

### Giriş (Login)
- Email ve şifre ile giriş
- Hata yönetimi
- Başarılı giriş sonrası yönlendirme

### Kayıt (Register)
- Yeni kullanıcı kaydı
- Form validasyonu
- Başarılı kayıt sonrası yönlendirme

### Dashboard
- Kullanıcı istatistikleri
- Son dokümanlar
- Hızlı işlemler

### Doküman Yükleme (DocumentUpload)
- Drag & drop dosya yükleme
- Dosya türü kontrolü
- Boyut sınırlaması
- Progress göstergesi

### Doküman Arama (DocumentSearch)
- Doğal dilde arama
- Dosya türü filtresi
- Arama sonuçları
- Özet ve anahtar kelimeler

### Doküman Özetleme (DocumentSummary)
- AI destekli özetleme
- Doküman seçimi
- Özet sonuçları
- Anahtar kelimeler

## 🔧 API Entegrasyonu

Frontend, backend API'si ile şu endpoint'leri kullanır:

- `POST /api/auth/login` - Kullanıcı girişi
- `POST /api/auth/register` - Kullanıcı kaydı
- `GET /api/auth/me` - Kullanıcı bilgileri
- `GET /api/documents/` - Doküman listesi
- `POST /api/documents/` - Doküman yükleme
- `GET /api/search/` - Doküman arama
- `POST /api/summary/{id}/generate` - AI özetleme

## 🎨 Tasarım Sistemi

### Renkler
- Primary: `#3b82f6` (Blue)
- Success: `#22c55e` (Green)
- Error: `#ef4444` (Red)
- Warning: `#f59e0b` (Yellow)

### Bileşenler
- Modern card tasarımları
- Responsive grid sistem
- Hover efektleri
- Loading animasyonları

## 📱 Responsive Tasarım

- Mobile-first yaklaşım
- Tablet ve desktop uyumlu
- Touch-friendly arayüz
- Responsive navigation

## 🔒 Güvenlik

- JWT token yönetimi
- Protected routes
- Form validasyonu
- Error handling

## 🚀 Build

Production build için:

```bash
npm run build
```

Build dosyaları `build/` klasöründe oluşturulur.

## 🧪 Test

```bash
npm test
```

## 📦 Deployment

### Netlify
```bash
npm run build
# build/ klasörünü Netlify'a yükleyin
```

### Vercel
```bash
npm run build
# Vercel CLI ile deploy edin
```

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun
3. Değişikliklerinizi commit edin
4. Pull request oluşturun

## 📄 Lisans

MIT License 