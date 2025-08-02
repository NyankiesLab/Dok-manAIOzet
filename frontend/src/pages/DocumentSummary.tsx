import React, { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext.tsx';
import { FileSearch, Brain, AlertCircle, CheckCircle, FileText } from 'lucide-react';
import axios from 'axios';

interface Document {
  id: number;
  title: string;
  filename: string;
  file_size: number;
  file_type: string;
  created_at: string;
  summary?: string;
  keywords?: string;
}

const DocumentSummary: React.FC = () => {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [selectedDocumentId, setSelectedDocumentId] = useState<number | ''>('');
  const [loading, setLoading] = useState(false);
  const [summaryLoading, setSummaryLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [summaryResult, setSummaryResult] = useState<{
    summary: string;
    keywords: string;
  } | null>(null);

  const { token } = useAuth();
  const API_BASE = 'http://localhost:8000/api';

  useEffect(() => {
    if (token) {
      fetchDocuments();
    }
  }, [token]);

  const fetchDocuments = async () => {
    try {
      const response = await axios.get(`${API_BASE}/documents/`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      setDocuments(response.data);
    } catch (error) {
      console.error('Dokümanlar yüklenemedi:', error);
    }
  };

  const handleGenerateSummary = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!selectedDocumentId) {
      setError('Lütfen bir doküman seçin.');
      return;
    }

    setSummaryLoading(true);
    setError('');
    setSuccess('');
    setSummaryResult(null);

    try {
      const response = await axios.post(
        `${API_BASE}/summary/${selectedDocumentId}/generate`,
        {},
        {
          headers: { Authorization: `Bearer ${token}` }
        }
      );

      setSummaryResult(response.data);
      setSuccess('Özet başarıyla oluşturuldu!');
      
      // Doküman listesini güncelle
      await fetchDocuments();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Özet oluşturulurken bir hata oluştu.');
    } finally {
      setSummaryLoading(false);
    }
  };

  const formatFileSize = (bytes: number) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('tr-TR');
  };

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-lg shadow-md">
        <div className="px-6 py-4 border-b border-gray-200">
          <h1 className="text-2xl font-bold text-gray-900">AI Doküman Özetleme</h1>
          <p className="text-gray-600 mt-1">
            Google Gemini AI ile dokümanlarınızı otomatik olarak özetleyin
          </p>
        </div>

        <div className="p-6">
          {/* Summary Form */}
          <form onSubmit={handleGenerateSummary} className="space-y-6 mb-8">
            <div>
              <label htmlFor="documentId" className="block text-sm font-medium text-gray-700 mb-2">
                Özetlenecek Doküman
              </label>
              <select
                id="documentId"
                value={selectedDocumentId}
                onChange={(e) => setSelectedDocumentId(e.target.value ? Number(e.target.value) : '')}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                required
              >
                <option value="">Doküman seçin...</option>
                {documents.map((doc) => (
                  <option key={doc.id} value={doc.id}>
                    {doc.title} ({doc.filename}) - {formatFileSize(doc.file_size)}
                  </option>
                ))}
              </select>
            </div>

            <button
              type="submit"
              disabled={summaryLoading || !selectedDocumentId}
              className="flex items-center space-x-2 px-6 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              <Brain className="h-4 w-4" />
              <span>{summaryLoading ? 'Özet Oluşturuluyor...' : 'AI ile Özetle'}</span>
            </button>
          </form>

          {/* Error/Success Messages */}
          {error && (
            <div className="flex items-center space-x-2 p-4 bg-red-50 border border-red-200 rounded-lg mb-6">
              <AlertCircle className="h-5 w-5 text-red-500" />
              <span className="text-red-700">{error}</span>
            </div>
          )}

          {success && (
            <div className="flex items-center space-x-2 p-4 bg-green-50 border border-green-200 rounded-lg mb-6">
              <CheckCircle className="h-5 w-5 text-green-500" />
              <span className="text-green-700">{success}</span>
            </div>
          )}

          {/* Summary Result */}
          {summaryResult && (
            <div className="space-y-6">
              <h2 className="text-xl font-semibold text-gray-900">AI Özeti</h2>
              
              <div className="bg-gray-50 rounded-lg p-6">
                <h3 className="font-medium text-gray-900 mb-3">Özet</h3>
                <p className="text-gray-700 leading-relaxed">{summaryResult.summary}</p>
              </div>

              <div className="bg-primary-50 rounded-lg p-6">
                <h3 className="font-medium text-gray-900 mb-3">Anahtar Kelimeler</h3>
                <div className="flex flex-wrap gap-2">
                  {summaryResult.keywords.split(',').map((keyword, index) => (
                    <span
                      key={index}
                      className="px-3 py-1 bg-primary-100 text-primary-700 text-sm rounded-full"
                    >
                      {keyword.trim()}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* Documents List */}
          <div className="mt-8">
            <h2 className="text-lg font-semibold text-gray-900 mb-4">Dokümanlarınız</h2>
            
            {loading ? (
              <div className="flex items-center justify-center py-8">
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
              </div>
            ) : documents.length === 0 ? (
              <div className="text-center py-8">
                <FileText className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-600 mb-2">Henüz doküman yüklemediniz.</p>
                <p className="text-sm text-gray-500">
                  Özetleme yapabilmek için önce doküman yüklemeniz gerekiyor.
                </p>
              </div>
            ) : (
              <div className="space-y-4">
                {documents.map((doc) => (
                  <div key={doc.id} className="border border-gray-200 rounded-lg p-4">
                    <div className="flex items-start justify-between">
                      <div className="flex items-start space-x-4">
                        <div className="p-2 bg-primary-100 rounded-lg">
                          <FileText className="h-5 w-5 text-primary-600" />
                        </div>
                        <div className="flex-1">
                          <h3 className="font-medium text-gray-900 mb-1">{doc.title}</h3>
                          <div className="flex items-center space-x-4 text-sm text-gray-600 mb-2">
                            <span>{doc.filename}</span>
                            <span>•</span>
                            <span>{formatFileSize(doc.file_size)}</span>
                            <span>•</span>
                            <span className="uppercase">{doc.file_type}</span>
                            <span>•</span>
                            <span>{formatDate(doc.created_at)}</span>
                          </div>
                          {doc.summary && (
                            <div className="mt-2">
                              <p className="text-xs font-medium text-green-600 mb-1">✓ Özetlendi</p>
                              <p className="text-sm text-gray-700 bg-gray-50 p-3 rounded-lg">
                                {doc.summary.substring(0, 150)}...
                              </p>
                            </div>
                          )}
                        </div>
                      </div>
                      <div className="text-right">
                        {doc.summary ? (
                          <span className="inline-flex items-center px-2 py-1 bg-green-100 text-green-800 text-xs rounded-full">
                            <CheckCircle className="h-3 w-3 mr-1" />
                            Özetlendi
                          </span>
                        ) : (
                          <span className="inline-flex items-center px-2 py-1 bg-gray-100 text-gray-800 text-xs rounded-full">
                            <FileSearch className="h-3 w-3 mr-1" />
                            Özetlenmedi
                          </span>
                        )}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* AI Info */}
          <div className="mt-8 bg-blue-50 rounded-lg p-6">
            <div className="flex items-start space-x-3">
              <Brain className="h-6 w-6 text-blue-600 mt-1" />
              <div>
                <h3 className="font-medium text-blue-900 mb-2">AI Özetleme Hakkında</h3>
                <ul className="space-y-1 text-sm text-blue-800">
                  <li>• Google Gemini AI kullanılarak özetleme yapılır</li>
                  <li>• Dokümanın ana fikirleri ve önemli noktaları çıkarılır</li>
                  <li>• Anahtar kelimeler otomatik olarak tespit edilir</li>
                  <li>• Özetleme işlemi birkaç saniye sürebilir</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DocumentSummary; 