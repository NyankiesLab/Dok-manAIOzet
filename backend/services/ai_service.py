"""
AI Servisi - Gemini API Entegrasyonu
====================================
"""

import json
import google.generativeai as genai
from typing import Tuple, List
from app.config import settings

class AIService:
    """AI servisi - Gemini API entegrasyonu"""
    
    def __init__(self):
        """AI servisi başlat"""
        self.use_gemini = bool(settings.GEMINI_API_KEY and settings.GEMINI_API_KEY != "your-gemini-api-key-here")
        
        if self.use_gemini:
            try:
                genai.configure(api_key=settings.GEMINI_API_KEY)
                # Model adını kontrol et ve güncelle
                model_name = settings.GEMINI_MODEL
                if model_name == "gemini-pro":
                    model_name = "gemini-1.5-pro"
                
                self.model = genai.GenerativeModel(model_name)
                print(f"Gemini model başlatıldı: {model_name}")
            except Exception as e:
                print(f"Gemini API hatası: {e}")
                # Fallback olarak eski model adını dene
                try:
                    self.model = genai.GenerativeModel("gemini-pro")
                    print("Fallback model kullanılıyor: gemini-pro")
                except Exception as e2:
                    print(f"Fallback model de başarısız: {e2}")
                    self.use_gemini = False
        else:
            print("Gemini API anahtarı bulunamadı, basit özetleme kullanılacak")
    
    async def generate_summary_and_keywords(self, content: str) -> Tuple[str, str]:
        """Metin özeti ve anahtar kelimeler oluştur"""
        try:
            if self.use_gemini:
                # Gemini API ile detaylı özetleme
                summary_prompt = f"""
                Aşağıdaki metni Türkçe olarak detaylı bir şekilde özetle. 
                
                ÖNEMLİ: Sadece makale başlığı, yazar bilgileri veya kaynakça kısmını özetleme. 
                Metnin ana içeriğini, bulgularını, sonuçlarını ve önemli noktalarını özetle.
                
                Özet şu özelliklere sahip olmalı:
                1. Makalenin ana konusu ve amacı
                2. Kullanılan araştırma yöntemi
                3. Ana bulgular ve sonuçlar
                4. Önemli veriler ve istatistikler
                5. Makalenin katkısı ve önemi
                
                Özet 300-400 kelime arasında olsun ve metnin gerçek içeriğini yansıtsın:
                
                {content}
                """
                
                summary_response = await self._generate_text(summary_prompt)
                summary = summary_response.strip()
                
                # Anahtar kelimeler çıkar
                keywords_prompt = f"""
                Aşağıdaki metinden en önemli 15 anahtar kelimeyi ve kavramı Türkçe olarak çıkar. 
                
                ÖNEMLİ: Sadece makale başlığı veya kaynakça kısmından değil, metnin ana içeriğinden anahtar kelimeler çıkar.
                Teknik terimler, kavramlar, araştırma yöntemleri ve önemli bulgular dahil et.
                Sadece kelimeleri virgülle ayırarak listele:
                
                {content}
                """
                
                keywords_response = await self._generate_text(keywords_prompt)
                keywords = keywords_response.strip()
                
                return summary, keywords
            else:
                # Geliştirilmiş basit özetleme
                return self._enhanced_simple_summary_and_keywords(content)
                
        except Exception as e:
            # Hata durumunda geliştirilmiş basit özetleme kullan
            return self._enhanced_simple_summary_and_keywords(content)
    
    def _enhanced_simple_summary_and_keywords(self, content: str) -> Tuple[str, str]:
        """Geliştirilmiş basit özetleme ve anahtar kelime çıkarma"""
        # Metni paragraflara böl
        paragraphs = content.split('\n\n')
        
        # İlk 10 paragrafı al (daha fazla içerik için)
        summary_paragraphs = paragraphs[:10]
        summary = '\n\n'.join(summary_paragraphs)
        
        # Eğer çok uzunsa kısalt ama daha fazla içerik bırak
        if len(summary) > 1500:
            sentences = summary.split('.')
            summary = '. '.join(sentences[:12]) + '.'
        
        # Geliştirilmiş anahtar kelime çıkarma
        words = content.lower().split()
        word_freq = {}
        
        # Türkçe stop words genişletildi
        stop_words = {
            've', 'bir', 'bu', 'da', 'de', 'ile', 'için', 'olarak', 'gibi', 'kadar', 'daha', 'en', 'çok', 'az', 
            'bazı', 'her', 'hiç', 'yok', 'var', 'olmak', 'oldu', 'olacak', 'ise', 'ama', 'fakat', 'ancak', 
            'lakin', 'çünkü', 'zira', 'madem', 'mademki', 'şu', 'o', 'bu', 'şu', 'bunlar', 'onlar', 'biz', 
            'siz', 'onlar', 'ben', 'sen', 'o', 'bizim', 'sizin', 'onların', 'benim', 'senin', 'onun',
            'için', 'tarafından', 'hakkında', 'üzerinde', 'altında', 'yanında', 'karşısında', 'önünde',
            'arkasında', 'içinde', 'dışında', 'arasında', 'yukarıda', 'aşağıda', 'sağında', 'solunda',
            'öncesinde', 'sonrasında', 'sırasında', 'esnasında', 'zamanında', 'vaktinde', 'sırasında',
            'gibi', 'kadar', 'dolayı', 'sebebiyle', 'nedeniyle', 'yüzünden', 'sayesinde', 'beraber',
            'birlikte', 'yanında', 'karşısında', 'önünde', 'arkasında', 'içinde', 'dışında', 'arasında'
        }
        
        for word in words:
            # Kelime temizleme
            word = word.strip('.,!?;:()[]{}"\'').strip()
            if len(word) > 3 and word not in stop_words and not word.isdigit():
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # En sık geçen 15 kelimeyi al
        keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:15]
        keywords_str = ', '.join([word for word, freq in keywords])
        
        return summary, keywords_str
    
    async def search_documents(self, query: str, documents: List[str]) -> List[dict]:
        """Dokümanlarda basit metin arama yap"""
        try:
            if not self.use_gemini:
                # Gemini API yoksa basit metin arama kullan
                return self._simple_text_search(query, documents)
            
            # Gemini API varsa kullan, ama rate limit hatası durumunda basit aramaya geç
            try:
                search_prompt = f"""
                Aşağıdaki sorgu için dokümanları değerlendir ve en uygun olanları sırala.
                Her doküman için 0-10 arası puan ver (10 en uygun):
                
                Sorgu: {query}
                
                Dokümanlar:
                {chr(10).join([f"{i+1}. {doc[:500]}..." for i, doc in enumerate(documents)])}
                
                Yanıt formatı: JSON array, her eleman {{"index": 0, "score": 8, "reason": "açıklama"}}
                """
                
                response = await self._generate_text(search_prompt)
                
                # JSON parse et
                try:
                    results = json.loads(response)
                    return results
                except json.JSONDecodeError:
                    return self._simple_text_search(query, documents)
                    
            except Exception as e:
                # Rate limit veya diğer API hataları durumunda basit aramaya geç
                print(f"Gemini API hatası, basit arama kullanılıyor: {e}")
                return self._simple_text_search(query, documents)
                
        except Exception as e:
            raise Exception(f"Arama hatası: {str(e)}")
    
    def _simple_text_search(self, query: str, documents: List[str]) -> List[dict]:
        """Basit metin arama - Gemini API olmadan"""
        query_lower = query.lower()
        results = []
        
        for i, doc in enumerate(documents):
            doc_lower = doc.lower()
            # Basit kelime eşleşmesi
            score = 0
            reason = ""
            
            # Query'deki her kelimeyi kontrol et
            query_words = query_lower.split()
            matches = []
            
            for word in query_words:
                if len(word) > 2 and word in doc_lower:
                    matches.append(word)
                    score += 1
            
            if matches:
                reason = f"Eşleşen kelimeler: {', '.join(matches)}"
                # Score'u 0-10 arasına normalize et
                normalized_score = min(score / len(query_words) * 10, 10)
                results.append({
                    "index": i,
                    "score": normalized_score,
                    "reason": reason
                })
        
        # Score'a göre sırala
        results.sort(key=lambda x: x["score"], reverse=True)
        return results
    
    async def answer_question(self, question: str, context: str) -> str:
        """Doküman içeriğine dayalı soru cevapla"""
        try:
            answer_prompt = f"""
            Aşağıdaki doküman içeriğine dayalı olarak soruyu cevapla:
            
            Doküman: {context[:2000]}
            
            Soru: {question}
            
            Cevap:
            """
            
            answer = await self._generate_text(answer_prompt)
            return answer.strip()
            
        except Exception as e:
            raise Exception(f"Soru cevaplama hatası: {str(e)}")
    
    async def _generate_text(self, prompt: str) -> str:
        """Gemini API ile metin oluştur"""
        if not self.use_gemini:
            raise Exception("Gemini API kullanılamıyor")
            
        try:
            # Önce sync versiyonu dene (daha güvenilir)
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            # Eğer sync başarısızsa async versiyonu dene
            try:
                response = await self.model.generate_content_async(prompt)
                return response.text
            except Exception as e2:
                raise Exception(f"Gemini API hatası: {str(e2)}")
    
    def validate_api_key(self) -> bool:
        """API anahtarını doğrula"""
        try:
            test_prompt = "Merhaba"
            response = self.model.generate_content(test_prompt)
            return True
        except Exception:
            return False 