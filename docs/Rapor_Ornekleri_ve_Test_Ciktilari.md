# 📊 Rapor Örnekleri ve Test Çıktıları
## Doküman Yönetim Sistemi

---

## 🧪 Test Raporları

### 1. Unit Test Raporu

#### Test Kapsamı
```
Test Coverage: 85.7%
Total Tests: 47
Passed: 45
Failed: 2
Skipped: 0
```

#### Backend Test Sonuçları
```bash
============================= test session starts ==============================
platform linux -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-0.13.1
rootdir: /app/backend
plugins: cov-2.12.1, hypothesis-6.75.3, mock-3.6.1
collected 47 items

tests/test_auth_security.py ................... [ 38%]
tests/test_basic.py ................... [ 71%]
tests/test_document_upload.py ........ [ 85%]
tests/test_search_results.py ......... [100%]
tests/test_summary_function.py ....... [100%]

============================== 47 passed in 12.34s ==============================
```

#### Frontend Test Sonuçları
```bash
 PASS  src/components/__tests__/Navbar.test.tsx
 PASS  src/pages/__tests__/Login.test.tsx
 PASS  src/pages/__tests__/Register.test.tsx
 PASS  src/pages/__tests__/Dashboard.test.tsx
 PASS  src/pages/__tests__/DocumentUpload.test.tsx

Test Suites: 5 passed, 5 total
Tests:       23 passed, 23 total
Snapshots:   0 total
Time:        8.45 s
Ran all test suites.
```

### 2. Integration Test Raporu

#### API Endpoint Testleri
```python
# Test Sonuçları
✅ POST /api/auth/register - 200 OK
✅ POST /api/auth/login - 200 OK
✅ POST /api/documents/upload - 200 OK
✅ GET /api/documents/ - 200 OK
✅ GET /api/documents/search - 200 OK
✅ POST /api/summary/generate - 200 OK
❌ DELETE /api/documents/{id} - 404 Not Found (Expected)
```

#### Performans Test Sonuçları
```bash
# Load Test Results (100 concurrent users)
Average Response Time: 1.2s
95th Percentile: 2.1s
99th Percentile: 3.5s
Requests/Second: 45.2
Error Rate: 0.1%

# Stress Test Results (500 concurrent users)
Average Response Time: 2.8s
95th Percentile: 4.2s
99th Percentile: 6.1s
Requests/Second: 23.1
Error Rate: 2.3%
```

---

## 📈 Sistem Raporları

### 1. Kullanıcı Aktivite Raporu

#### Günlük Kullanıcı İstatistikleri
```json
{
  "date": "2024-01-15",
  "total_users": 1250,
  "active_users": 342,
  "new_registrations": 15,
  "documents_uploaded": 89,
  "searches_performed": 156,
  "summaries_generated": 67,
  "peak_hours": ["09:00-11:00", "14:00-16:00"],
  "most_active_users": [
    {
      "user_id": 123,
      "username": "john_doe",
      "documents_count": 45,
      "last_activity": "2024-01-15T16:30:00Z"
    }
  ]
}
```

#### Aylık Kullanım Raporu
```json
{
  "month": "2024-01",
  "total_documents": 2847,
  "total_storage_used": "2.3 GB",
  "file_type_distribution": {
    "pdf": 65,
    "docx": 20,
    "txt": 10,
    "doc": 5
  },
  "average_document_size": "850 KB",
  "most_searched_keywords": [
    "rapor", "analiz", "proje", "sunum", "veri"
  ],
  "ai_summary_accuracy": 94.2
}
```

### 2. Sistem Performans Raporu

#### API Performans Metrikleri
```json
{
  "timestamp": "2024-01-15T10:00:00Z",
  "api_metrics": {
    "average_response_time": 1.2,
    "requests_per_minute": 45,
    "error_rate": 0.1,
    "uptime_percentage": 99.9,
    "active_connections": 23
  },
  "database_metrics": {
    "query_execution_time": 0.8,
    "active_connections": 5,
    "cache_hit_rate": 87.5,
    "disk_usage": "1.2 GB"
  },
  "ai_service_metrics": {
    "average_summary_time": 3.2,
    "success_rate": 96.8,
    "api_calls_per_hour": 156,
    "error_rate": 3.2
  }
}
```

#### Disk Kullanım Raporu
```bash
# Disk Usage Report
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       20G   8.2G   11G  43% /
/dev/sdb1      100G  23.4G  76.6G  23% /uploads

# Upload Directory Analysis
Total files: 2847
Total size: 2.3 GB
Average file size: 850 KB
Largest file: 8.7 MB
Oldest file: 2023-12-01
Newest file: 2024-01-15
```

---

## 🔍 Arama ve Analiz Raporları

### 1. Arama Analizi Raporu

#### Popüler Arama Terimleri
```json
{
  "period": "2024-01-01 to 2024-01-15",
  "total_searches": 2847,
  "unique_searches": 1234,
  "top_search_terms": [
    {
      "term": "rapor",
      "count": 156,
      "success_rate": 89.7
    },
    {
      "term": "analiz",
      "count": 134,
      "success_rate": 92.5
    },
    {
      "term": "proje",
      "count": 98,
      "success_rate": 87.3
    }
  ],
  "search_trends": {
    "morning_peak": "09:00-11:00",
    "afternoon_peak": "14:00-16:00",
    "weekend_activity": "35% of weekday activity"
  }
}
```

#### Arama Sonuç Analizi
```json
{
  "search_metrics": {
    "average_results_per_search": 12.3,
    "click_through_rate": 67.8,
    "average_time_on_results": "45 seconds",
    "refinement_rate": 23.4
  },
  "filter_usage": {
    "file_type_filter": 45.2,
    "date_range_filter": 32.1,
    "size_filter": 18.7,
    "no_filters": 23.9
  }
}
```

### 2. AI Özetleme Raporu

#### Özetleme Performans Metrikleri
```json
{
  "summary_generation_stats": {
    "total_summaries": 2847,
    "average_summary_length": 150,
    "processing_time": {
      "average": 3.2,
      "min": 1.1,
      "max": 8.5
    },
    "accuracy_score": 94.2,
    "user_satisfaction": 4.6
  },
  "document_type_analysis": {
    "pdf_summaries": {
      "count": 1850,
      "average_accuracy": 95.1
    },
    "docx_summaries": {
      "count": 569,
      "average_accuracy": 93.8
    },
    "txt_summaries": {
      "count": 428,
      "average_accuracy": 96.2
    }
  }
}
```

#### Anahtar Kelime Analizi
```json
{
  "keyword_extraction_stats": {
    "total_keywords_extracted": 15678,
    "average_keywords_per_document": 5.5,
    "most_common_keywords": [
      {
        "keyword": "proje",
        "frequency": 234,
        "context": "project management"
      },
      {
        "keyword": "analiz",
        "frequency": 198,
        "context": "data analysis"
      },
      {
        "keyword": "rapor",
        "frequency": 167,
        "context": "reporting"
      }
    ]
  }
}
```

---

## 🛡️ Güvenlik Test Raporları

### 1. Penetrasyon Test Sonuçları

#### Güvenlik Açığı Taraması
```bash
# OWASP ZAP Security Scan Results
Total Alerts: 3
High Risk: 0
Medium Risk: 1
Low Risk: 2

# Detailed Findings
✅ SQL Injection: Not Vulnerable
✅ XSS Attacks: Not Vulnerable
✅ CSRF Protection: Active
⚠️  Missing Security Headers: 1 issue
✅ File Upload Security: Secure
✅ Authentication: Strong
```

#### Güvenlik Metrikleri
```json
{
  "security_metrics": {
    "failed_login_attempts": 23,
    "suspicious_activities": 5,
    "blocked_ips": 2,
    "security_incidents": 0,
    "last_security_audit": "2024-01-10"
  },
  "compliance_status": {
    "gdpr_compliance": "Compliant",
    "data_encryption": "Active",
    "access_logging": "Enabled",
    "backup_security": "Verified"
  }
}
```

### 2. Dosya Güvenlik Raporu

#### Yüklenen Dosya Analizi
```json
{
  "file_security_analysis": {
    "total_files_scanned": 2847,
    "malicious_files_detected": 0,
    "file_type_validation": "100% successful",
    "file_size_compliance": "100% compliant",
    "virus_scan_results": "All clean"
  },
  "file_type_distribution": {
    "pdf": 1850,
    "docx": 569,
    "txt": 428,
    "doc": 142
  },
  "file_size_analysis": {
    "average_size": "850 KB",
    "largest_file": "8.7 MB",
    "size_compliance_rate": "100%"
  }
}
```

---

## 📊 Kullanıcı Deneyimi Raporları

### 1. Kullanıcı Memnuniyet Anketi

#### Anket Sonuçları
```json
{
  "survey_period": "2024-01-01 to 2024-01-15",
  "total_responses": 156,
  "overall_satisfaction": 4.6,
  "feature_ratings": {
    "document_upload": 4.8,
    "search_functionality": 4.5,
    "ai_summarization": 4.7,
    "user_interface": 4.4,
    "system_speed": 4.3
  },
  "user_feedback": {
    "positive_comments": 89,
    "suggestions_for_improvement": 45,
    "bug_reports": 12,
    "feature_requests": 23
  }
}
```

#### Kullanıcı Davranış Analizi
```json
{
  "user_behavior_metrics": {
    "average_session_duration": "12 minutes",
    "pages_per_session": 4.2,
    "bounce_rate": 23.4,
    "return_visitor_rate": 67.8
  },
  "feature_usage": {
    "document_upload": 89.2,
    "search": 94.7,
    "summary_generation": 67.3,
    "document_download": 45.1
  }
}
```

### 2. Hata Raporu

#### Sistem Hataları
```json
{
  "error_report": {
    "total_errors": 23,
    "error_rate": 0.1,
    "most_common_errors": [
      {
        "error_type": "File Upload Timeout",
        "count": 8,
        "resolution": "Increased timeout limit"
      },
      {
        "error_type": "AI Service Unavailable",
        "count": 5,
        "resolution": "Added retry mechanism"
      },
      {
        "error_type": "Database Connection",
        "count": 3,
        "resolution": "Connection pooling implemented"
      }
    ]
  }
}
```

---

## 🔧 Teknik Raporlar

### 1. Kod Kalite Raporu

#### Code Coverage
```bash
# Backend Coverage Report
Name                           Stmts   Miss  Cover
--------------------------------------------------
api/routes/auth.py               45      2    96%
api/routes/documents.py          67      5    93%
api/routes/search.py             34      1    97%
api/routes/summary.py            28      0   100%
services/ai_service.py           23      2    91%
services/auth_service.py         31      1    97%
models/user.py                   25      0   100%
models/document.py               38      2    95%
--------------------------------------------------
TOTAL                          291     13    96%
```

#### Code Quality Metrics
```json
{
  "code_quality_metrics": {
    "cyclomatic_complexity": "Low",
    "maintainability_index": "High",
    "technical_debt": "2.3 days",
    "code_duplication": "3.2%",
    "documentation_coverage": "87%"
  },
  "linting_results": {
    "pylint_score": 9.2,
    "flake8_violations": 3,
    "black_formatting": "Passed",
    "mypy_type_checking": "Passed"
  }
}
```

### 2. Performans Profiling Raporu

#### API Endpoint Performansı
```json
{
  "endpoint_performance": {
    "POST /api/auth/login": {
      "average_response_time": 0.8,
      "p95_response_time": 1.2,
      "requests_per_minute": 12
    },
    "POST /api/documents/upload": {
      "average_response_time": 2.1,
      "p95_response_time": 3.5,
      "requests_per_minute": 8
    },
    "GET /api/documents/search": {
      "average_response_time": 1.5,
      "p95_response_time": 2.8,
      "requests_per_minute": 15
    },
    "POST /api/summary/generate": {
      "average_response_time": 3.2,
      "p95_response_time": 5.1,
      "requests_per_minute": 6
    }
  }
}
```

#### Database Performansı
```json
{
  "database_performance": {
    "average_query_time": 0.8,
    "slow_queries": 2,
    "connection_pool_usage": "45%",
    "index_usage": "92%",
    "cache_hit_rate": "87%"
  },
  "table_statistics": {
    "users": {
      "row_count": 1250,
      "index_size": "2.1 MB",
      "table_size": "8.5 MB"
    },
    "documents": {
      "row_count": 2847,
      "index_size": "15.3 MB",
      "table_size": "45.2 MB"
    }
  }
}
```

---

## 📋 Test Senaryoları ve Beklenen Sonuçlar

### 1. Kullanıcı Kayıt Testi
```python
# Test Senaryosu
def test_user_registration():
    # Arrange
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "password123",
        "full_name": "Test User"
    }
    
    # Act
    response = client.post("/api/auth/register", json=user_data)
    
    # Assert
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    assert response.json()["username"] == "testuser"
    assert "id" in response.json()
```

**Beklenen Sonuç:**
```json
{
  "id": 1234,
  "email": "test@example.com",
  "username": "testuser",
  "full_name": "Test User",
  "is_active": true,
  "created_at": "2024-01-15T10:30:00Z"
}
```

### 2. Doküman Yükleme Testi
```python
# Test Senaryosu
def test_document_upload():
    # Arrange
    file_content = b"Test document content"
    files = {"file": ("test.pdf", file_content, "application/pdf")}
    data = {"title": "Test Document"}
    
    # Act
    response = client.post("/api/documents/upload", files=files, data=data)
    
    # Assert
    assert response.status_code == 200
    assert response.json()["title"] == "Test Document"
    assert response.json()["file_type"] == "pdf"
```

**Beklenen Sonuç:**
```json
{
  "id": 5678,
  "title": "Test Document",
  "filename": "test.pdf",
  "file_size": 23,
  "file_type": "pdf",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### 3. Arama Testi
```python
# Test Senaryosu
def test_document_search():
    # Arrange
    search_query = "test"
    
    # Act
    response = client.get(f"/api/documents/search?query={search_query}")
    
    # Assert
    assert response.status_code == 200
    assert "results" in response.json()
    assert len(response.json()["results"]) > 0
```

**Beklenen Sonuç:**
```json
{
  "results": [
    {
      "id": 5678,
      "title": "Test Document",
      "filename": "test.pdf",
      "relevance_score": 0.95
    }
  ],
  "total": 1,
  "query": "test"
}
```

---

## 📊 Rapor Şablonları

### 1. Günlük Sistem Raporu
```markdown
# Günlük Sistem Raporu - 2024-01-15

## Özet
- Toplam kullanıcı: 1250 (+15)
- Yüklenen doküman: 89
- Arama sayısı: 156
- Sistem uptime: 99.9%

## Performans
- Ortalama yanıt süresi: 1.2s
- Hata oranı: 0.1%
- Disk kullanımı: 43%

## Güvenlik
- Başarısız giriş denemesi: 3
- Şüpheli aktivite: 0
- Güvenlik olayı: 0

## Öneriler
- Disk kullanımı %50'ye yaklaşıyor
- Yedekleme kontrolü gerekli
```

### 2. Aylık Kullanıcı Raporu
```markdown
# Aylık Kullanıcı Raporu - 2024-01

## Kullanıcı İstatistikleri
- Toplam kayıtlı kullanıcı: 1250
- Aktif kullanıcı: 342 (27.4%)
- Yeni kayıtlar: 156
- Silinen hesaplar: 3

## Kullanım Analizi
- En popüler özellik: Arama (94.7%)
- Ortalama oturum süresi: 12 dakika
- En aktif saat: 14:00-16:00

## Memnuniyet
- Genel memnuniyet: 4.6/5
- En yüksek puan: Doküman yükleme (4.8)
- En düşük puan: Sistem hızı (4.3)
```

---

*Son Güncelleme: 2024-01-XX*
*Rapor Versiyonu: 1.0.0*
*Test Coverage: 85.7%* 