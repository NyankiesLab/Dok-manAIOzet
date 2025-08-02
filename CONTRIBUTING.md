# 🤝 Katkıda Bulunma Rehberi

Bu projeye katkıda bulunmak istediğiniz için teşekkürler! Bu rehber, katkıda bulunma sürecinizi kolaylaştırmak için hazırlanmıştır.

## 📋 İçindekiler

- [Kod Yazma Standartları](#kod-yazma-standartları)
- [Geliştirme Süreci](#geliştirme-süreci)
- [Pull Request Süreci](#pull-request-süreci)
- [Hata Bildirimi](#hata-bildirimi)
- [Özellik İsteği](#özellik-isteği)

## 🎯 Kod Yazma Standartları

### Python (Backend)
- **PEP 8** standartlarına uyun
- **Type hints** kullanın
- **Docstring** yazın
- **Black** formatter kullanın
- **Flake8** linting uygulayın

### JavaScript/TypeScript (Frontend)
- **ESLint** kurallarına uyun
- **Prettier** formatter kullanın
- **TypeScript** tip güvenliği sağlayın
- **React Hooks** kullanın

### Genel Kurallar
- Anlamlı değişken ve fonksiyon isimleri kullanın
- Yorum satırları ekleyin
- Test yazın
- README dosyalarını güncelleyin

## 🚀 Geliştirme Süreci

### 1. Fork Yapın
```bash
# GitHub'da fork butonuna tıklayın
# Yerel bilgisayarınıza klonlayın
git clone https://github.com/yourusername/document-management-system.git
cd document-management-system
```

### 2. Development Branch Oluşturun
```bash
# Ana branch'i güncelleyin
git checkout main
git pull origin main

# Yeni branch oluşturun
git checkout -b feature/amazing-feature
```

### 3. Geliştirme Ortamını Kurun
```bash
# Backend
cd backend
pip install -r requirements.txt
cp env.example .env
# .env dosyasını düzenleyin

# Frontend
cd frontend
npm install
cp env.example .env
```

### 4. Değişiklikleri Yapın
- Kodunuzu yazın
- Testleri çalıştırın
- Linting uygulayın

### 5. Commit Yapın
```bash
# Değişiklikleri staging'e ekleyin
git add .

# Commit mesajı yazın
git commit -m "feat: add amazing feature

- Yeni özellik eklendi
- Testler yazıldı
- Dokümantasyon güncellendi"
```

## 📝 Pull Request Süreci

### 1. Push Yapın
```bash
git push origin feature/amazing-feature
```

### 2. Pull Request Oluşturun
- GitHub'da "New Pull Request" butonuna tıklayın
- Base branch: `main`
- Compare branch: `feature/amazing-feature`

### 3. PR Açıklaması
```markdown
## 🎯 Değişiklik Özeti
Bu PR şu özellikleri ekler:

## 🔧 Yapılan Değişiklikler
- [ ] Yeni özellik eklendi
- [ ] Testler yazıldı
- [ ] Dokümantasyon güncellendi
- [ ] Linting uygulandı

## 🧪 Testler
- [ ] Unit testler geçiyor
- [ ] Integration testler geçiyor
- [ ] Manuel test yapıldı

## 📸 Ekran Görüntüleri
(Eğer UI değişikliği varsa)

## 🔍 Kontrol Listesi
- [ ] Kod standartlarına uygun
- [ ] Testler yazıldı
- [ ] Dokümantasyon güncellendi
- [ ] Breaking change yok
```

## 🐛 Hata Bildirimi

### Hata Raporu Şablonu
```markdown
## 🐛 Hata Açıklaması
Kısa ve net bir açıklama

## 🔄 Yeniden Üretme Adımları
1. Bu sayfaya gidin
2. Bu butona tıklayın
3. Bu hatayı görün

## 📱 Beklenen Davranış
Ne olması gerekiyordu

## 🖥️ Sistem Bilgileri
- OS: Windows 10
- Browser: Chrome 120
- Version: 1.0.0

## 📸 Ekran Görüntüleri
(Varsa)
```

## 💡 Özellik İsteği

### Özellik İsteği Şablonu
```markdown
## 💡 Özellik Açıklaması
Bu özellik ne yapacak

## 🎯 Problem
Bu özellik hangi problemi çözecek

## 💭 Önerilen Çözüm
Nasıl çalışması gerekiyor

## 🔄 Alternatif Çözümler
Varsa diğer çözümler

## 📸 Mockup/Prototip
(Varsa)
```

## 🧪 Test Yazma

### Backend Testleri
```python
# tests/test_feature.py
import pytest
from fastapi.testclient import TestClient

def test_feature():
    client = TestClient(app)
    response = client.get("/api/test")
    assert response.status_code == 200
```

### Frontend Testleri
```typescript
// src/components/__tests__/Component.test.tsx
import { render, screen } from '@testing-library/react'
import Component from '../Component'

test('renders component', () => {
  render(<Component />)
  expect(screen.getByText('Hello')).toBeInTheDocument()
})
```

## 📚 Dokümantasyon

### Kod Dokümantasyonu
```python
def process_document(file_path: str) -> dict:
    """
    Dokümanı işler ve sonuçları döndürür.
    
    Args:
        file_path (str): İşlenecek dosyanın yolu
        
    Returns:
        dict: İşleme sonuçları
        
    Raises:
        FileNotFoundError: Dosya bulunamadığında
    """
    pass
```

### API Dokümantasyonu
```python
@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    description: str = Form(None)
):
    """
    Doküman yükler.
    
    - **file**: Yüklenecek dosya
    - **description**: Dosya açıklaması (opsiyonel)
    
    Returns:
        DocumentResponse: Yüklenen doküman bilgileri
    """
    pass
```

## 🎨 Commit Mesaj Standartları

### Format
```
type(scope): description

[optional body]

[optional footer]
```

### Tipler
- `feat`: Yeni özellik
- `fix`: Hata düzeltmesi
- `docs`: Dokümantasyon
- `style`: Formatting
- `refactor`: Kod düzenleme
- `test`: Test ekleme
- `chore`: Bakım işleri

### Örnekler
```
feat(auth): add JWT authentication
fix(upload): resolve file size validation issue
docs(readme): update installation instructions
style(backend): format code with black
```

## 🤝 İletişim

- **GitHub Issues**: [Repository Issues](https://github.com/yourusername/document-management-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/document-management-system/discussions)
- **Email**: [your-email@example.com]

## 🙏 Teşekkürler

Katkıda bulunduğunuz için teşekkürler! Bu proje topluluk katkılarıyla büyüyor.

---

⭐ Bu rehberi beğendiyseniz yıldız vermeyi unutmayın! 