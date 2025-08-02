# Node.js 18 image kullan
FROM node:18-alpine

# Çalışma dizinini ayarla
WORKDIR /app

# Package.json ve package-lock.json kopyala
COPY package*.json ./

# Bağımlılıkları yükle
RUN npm install

# Uygulama kodlarını kopyala
COPY . .

# Build işlemi için gerekli değişkenler
ENV REACT_APP_API_URL=http://localhost:5000

# Port 3000'i aç
EXPOSE 3000

# Uygulamayı çalıştır
CMD ["npm", "start"] 