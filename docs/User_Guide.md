# Doküman Yönetim Sistemi - Kullanıcı Kılavuzu

## 📋 İçindekiler

1. [Giriş](#giriş)
2. [Hızlı Başlangıç](#hızlı-başlangıç)
3. [Kullanıcı Hesabı](#kullanıcı-hesabı)
4. [Doküman Yükleme](#doküman-yükleme)
5. [Arama ve Özetleme](#arama-ve-özetleme)
6. [AI Özellikleri](#ai-özellikleri)
7. [Güvenlik](#güvenlik)
8. [Sık Sorulan Sorular](#sık-sorulan-sorular)

## 🚀 Giriş

Doküman Yönetim Sistemi, dokümanlarınızı yükleyebileceğiniz, arayabileceğiniz ve AI destekli özetleme yapabileceğiniz modern bir web uygulamasıdır.

### 🎯 Ana Özellikler

- 📤 **Kolay Doküman Yükleme**: PDF, DOC, DOCX, TXT dosyalarını destekler
- 🔍 **Akıllı Arama**: Hem temel hem de doğal dil araması
- 🤖 **AI Özetleme**: Google Gemini ile otomatik özet ve anahtar kelime çıkarımı
- 🔐 **Güvenli Erişim**: JWT token tabanlı kimlik doğrulama
- 📊 **İstatistikler**: Doküman ve özet istatistikleri

## ⚡ Hızlı Başlangıç

### 1. Sisteme Erişim
Tarayıcınızda şu adresi açın:
```
http://localhost:8000
```

### 2. Hesap Oluşturma
1. **"Kayıt Ol"** butonuna tıklayın
2. Gerekli bilgileri doldurun:
   - E-posta adresi
   - Kullanıcı adı
   - Ad soyad
   - Şifre
3. **"Kayıt Ol"** butonuna tıklayın

### 3. Giriş Yapma
1. **"Giriş"** butonuna tıklayın
2. E-posta ve şifrenizi girin
3. **"Giriş Yap"** butonuna tıklayın

## 👤 Kullanıcı Hesabı

### Hesap Yönetimi

#### Profil Bilgileri
- E-posta adresinizi değiştiremezsiniz
- Kullanıcı adı ve ad soyad bilgilerinizi güncelleyebilirsiniz
- Şifrenizi güvenli tutun

#### Oturum Yönetimi
- Oturum süresi: 30 dakika
- Otomatik çıkış: 30 dakika işlem yapmazsanız
- **"Çıkış"** butonu ile manuel çıkış yapabilirsiniz

### Güvenlik İpuçları
- Güçlü şifre kullanın (en az 8 karakter)
- Şifrenizi kimseyle paylaşmayın
- Düzenli olarak şifrenizi değiştirin
- Farklı cihazlardan giriş yaparken dikkatli olun

## 📤 Doküman Yükleme

### Desteklenen Dosya Türleri

| Dosya Türü | Uzantı | Maksimum Boyut |
|------------|--------|----------------|
| PDF | .pdf | 10MB |
| Microsoft Word | .doc, .docx | 10MB |
| Text | .txt | 10MB |

### Yükleme Adımları

1. **"Yükle"** sayfasına gidin
2. **Doküman Başlığı** girin (zorunlu)
3. **Dosya Seçin** butonuna tıklayın
4. Bilgisayarınızdan dosyayı seçin
5. **"Yükle"** butonuna tıklayın

### Yükleme İpuçları

#### ✅ Doğru Kullanım
- Dosya boyutu 10MB'dan küçük olmalı
- Desteklenen dosya türlerini kullanın
- Anlamlı başlıklar verin
- Dosya içeriği okunabilir olmalı

#### ❌ Kaçınılması Gerekenler
- Çok büyük dosyalar (10MB+)
- Desteklenmeyen dosya türleri
- Boş veya anlamsız başlıklar
- Şifrelenmiş dosyalar

### Yükleme Sonrası
- Dosya başarıyla yüklendiğinde onay mesajı görürsünüz
- Doküman listeniz otomatik güncellenir
- Yüklenen dosya hemen arama ve özetleme için kullanılabilir

## 🔍 Arama ve Özetleme

### Arama Sayfasına Erişim
Giriş yaptıktan sonra **"🔍 Ara & Özet"** butonuna tıklayın.

### 1. Temel Arama

#### Kullanım
1. **Arama terimi** girin
2. **Dosya türü** seçin (opsiyonel)
3. **"🔍 Ara"** butonuna tıklayın

#### Arama İpuçları
- Büyük/küçük harf duyarsız
- Kısmi kelime eşleşmesi
- Başlık, içerik ve özetlerde arama
- Çoklu kelime araması desteklenir

#### Örnek Aramalar
```
yapay zeka
makine öğrenmesi
AI teknolojileri
veri bilimi
```

### 2. Doğal Dil Arama

#### Kullanım
1. **Doğal dil sorgusu** girin
2. **"🤖 Doğal Dilde Ara"** butonuna tıklayın

#### Örnek Sorgular
```
"Yapay zeka hakkında ne anlatıyor?"
"Makine öğrenmesi konusunda hangi dokümanlar var?"
"Veri analizi ile ilgili dokümanları bul"
"AI teknolojilerinin kullanım alanları neler?"
```

#### AI Arama Özellikleri
- Doğal dil anlama
- Semantik arama
- Eşleşme skorları
- Arama nedeni açıklaması

### 3. AI Özetleme

#### Doküman Seçimi ile Özetleme
1. **Doküman Seçin** dropdown'ından doküman seçin
2. **"🤖 AI Özet Oluştur"** butonuna tıklayın

#### ID ile Özetleme
1. **Doküman ID** girin
2. **"🔍 ID ile Ara"** butonuna tıklayın

#### Özetleme Sonuçları
- **Detaylı Özet**: Dokümanın ana konuları
- **Anahtar Kelimeler**: Önemli terimler
- **Kaynakça Bilgisi**: Hangi dokümandan alındığı

## 🤖 AI Özellikleri

### Google Gemini Entegrasyonu

#### Özetleme Algoritması
- Doküman içeriğini analiz eder
- Ana konuları belirler
- Önemli noktaları çıkarır
- Türkçe özet oluşturur

#### Anahtar Kelime Çıkarımı
- Teknik terimleri tespit eder
- Konu ile ilgili anahtar kelimeleri belirler
- Kategorize edilmiş kelimeler sunar

#### Doğal Dil İşleme
- Türkçe dil desteği
- Semantik anlama
- Bağlam analizi
- Akıllı soru-cevap

### AI Kullanım İpuçları

#### ✅ Etkili Kullanım
- Doküman içeriği net olmalı
- Teknik terimler doğru yazılmalı
- Yeterli içerik olmalı (minimum 50 karakter)
- Türkçe karakterler kullanın

#### ❌ Kaçınılması Gerekenler
- Çok kısa dokümanlar
- Görsel ağırlıklı dosyalar
- Şifrelenmiş içerik
- Bozuk dosyalar

## 🔐 Güvenlik

### Veri Güvenliği

#### Dosya Güvenliği
- Dosyalar güvenli sunucuda saklanır
- Sadece siz erişebilirsiniz
- Otomatik yedekleme
- Şifreli depolama

#### Hesap Güvenliği
- JWT token tabanlı kimlik doğrulama
- Şifre hashleme (bcrypt)
- Oturum süresi sınırı
- Güvenli çıkış

### Gizlilik

#### Veri Kullanımı
- Kişisel verileriniz korunur
- Üçüncü taraflarla paylaşılmaz
- Sadece AI özetleme için kullanılır
- İsteğinizle silinebilir

#### Çerezler
- Oturum yönetimi için gerekli
- Güvenlik amaçlı
- Takip çerezleri yok
- Tarayıcıdan silinebilir

## ❓ Sık Sorulan Sorular

### Genel Sorular

**Q: Hangi dosya türleri destekleniyor?**
A: PDF, DOC, DOCX ve TXT dosyaları desteklenir.

**Q: Maksimum dosya boyutu nedir?**
A: 10MB'a kadar dosya yükleyebilirsiniz.

**Q: Kaç doküman yükleyebilirim?**
A: Şu anda sınırsız doküman yükleyebilirsiniz.

### Teknik Sorular

**Q: AI özetleme ne kadar sürer?**
A: Genellikle 10-30 saniye arasında tamamlanır.

**Q: Özetler ne kadar doğru?**
A: AI özetleri %85-95 doğruluk oranına sahiptir.

**Q: Hangi dilde özet alabilirim?**
A: Şu anda sadece Türkçe özet desteği vardır.

### Güvenlik Soruları

**Q: Dosyalarım güvende mi?**
A: Evet, dosyalarınız şifreli olarak saklanır ve sadece size aittir.

**Q: Şifremi unuttum, ne yapmalıyım?**
A: Şu anda şifre sıfırlama özelliği yoktur. Yeni hesap oluşturabilirsiniz.

**Q: Hesabımı silebilir miyim?**
A: Evet, tüm verilerinizle birlikte hesabınızı silebilirsiniz.

### Kullanım Soruları

**Q: Arama nasıl çalışır?**
A: Hem temel metin araması hem de AI destekli doğal dil araması yapabilirsiniz.

**Q: Özetler kaydediliyor mu?**
A: Evet, oluşturulan özetler kalıcı olarak saklanır.

**Q: Dokümanları düzenleyebilir miyim?**
A: Şu anda doküman düzenleme özelliği yoktur, sadece yeni dosya yükleyebilirsiniz.

## 🆘 Destek

### Sorun Giderme

#### Yükleme Sorunları
- Dosya boyutunu kontrol edin
- Dosya türünü kontrol edin
- İnternet bağlantınızı kontrol edin
- Tarayıcı önbelleğini temizleyin

#### Arama Sorunları
- Arama terimini kontrol edin
- Doküman içeriğini kontrol edin
- Farklı arama yöntemlerini deneyin

#### AI Sorunları
- Doküman içeriğini kontrol edin
- Yeterli içerik olduğundan emin olun
- Teknik terimlerin doğru yazıldığından emin olun

### İletişim

Teknik destek için:
- E-posta: support@example.com
- Telefon: +90 xxx xxx xx xx
- Çalışma saatleri: Pazartesi-Cuma 09:00-18:00

## 📝 Sürüm Notları

### v1.0.0 (Güncel)
- ✅ Temel doküman yükleme
- ✅ AI destekli özetleme
- ✅ Doğal dil arama
- ✅ Kullanıcı kimlik doğrulama
- ✅ Güvenli dosya saklama

### Gelecek Özellikler
- 🔄 Doküman düzenleme
- 🔄 Şifre sıfırlama
- 🔄 Toplu dosya yükleme
- 🔄 Gelişmiş arama filtreleri
- 🔄 Mobil uygulama

---

**Son Güncelleme:** 2024-01-01  
**Sürüm:** 1.0.0  
**Geliştirici:** Doküman Yönetim Sistemi Ekibi 