import React, { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext.tsx';
import { FileText, AlertCircle, Download, Eye, Search } from 'lucide-react';
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

const DocumentSearch: React.FC = () => {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchQuery, setSearchQuery] = useState('');
  const [fileType, setFileType] = useState('all');

  const { token } = useAuth();
  const API_BASE = 'http://localhost:5000/api';

  useEffect(() => {
    if (searchQuery.trim()) {
      // Arama sorgusu varsa arama yap
      searchDocuments();
    } else {
      // Arama sorgusu yoksa tüm dokümanları getir
      fetchDocuments();
    }
  }, [searchQuery, fileType]);

  const searchDocuments = async () => {
    setLoading(true);
    setError('');

    try {
      const params = new URLSearchParams();
      params.append('query', searchQuery);
      if (fileType && fileType !== 'all') {
        params.append('file_type', fileType);
      }

      const response = await axios.get(`${API_BASE}/search/?${params}`, {
        headers: token ? { 'Authorization': `Bearer ${token}` } : {}
      });

      setDocuments(response.data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Arama yapılırken bir hata oluştu.');
      setDocuments([]);
    } finally {
      setLoading(false);
    }
  };

  const fetchDocuments = async () => {
    setLoading(true);
    setError('');

    try {
      const params = new URLSearchParams();
      if (fileType && fileType !== 'all') {
        params.append('file_type', fileType);
      }

      const response = await axios.get(`${API_BASE}/documents/?${params}`, {
        headers: token ? { 'Authorization': `Bearer ${token}` } : {}
      });

      setDocuments(response.data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Dokümanlar yüklenirken bir hata oluştu.');
      setDocuments([]);
    } finally {
      setLoading(false);
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

  const handleDocumentClick = (documentId: number) => {
    // Doküman detay sayfasına yönlendir
    window.open(`${API_BASE}/documents/${documentId}`, '_blank');
  };

  return (
    <div className="max-w-6xl mx-auto">
      <div className="bg-white rounded-lg shadow-md">
        <div className="px-6 py-4 border-b border-gray-200">
          <h1 className="text-2xl font-bold text-gray-900">Doküman Arama</h1>
          <p className="text-gray-600 mt-1">
            Dokümanlarınızda arama yapın ve filtreleyin
          </p>
        </div>

        <div className="p-6">
          {/* Search and Filter */}
          <div className="mb-6 space-y-4">
            {/* Search Input */}
            <div>
              <label htmlFor="searchQuery" className="block text-sm font-medium text-gray-700 mb-2">
                Arama
              </label>
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
                <input
                  type="text"
                  id="searchQuery"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Doküman başlığı, içerik veya dosya adında arama yapın..."
                  className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
                />
              </div>
            </div>

            {/* File Type Filter */}
            <div>
              <label htmlFor="fileType" className="block text-sm font-medium text-gray-700 mb-2">
                Dosya Türü Filtresi
              </label>
              <select
                id="fileType"
                value={fileType}
                onChange={(e) => setFileType(e.target.value)}
                className="w-full md:w-48 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
              >
                <option value="all">Tüm Dosya Türleri</option>
                <option value="pdf">PDF</option>
                <option value="docx">DOCX</option>
                <option value="txt">TXT</option>
                <option value="doc">DOC</option>
              </select>
            </div>
          </div>

          {/* Error Message */}
          {error && (
            <div className="flex items-center space-x-2 p-4 bg-red-50 border border-red-200 rounded-lg mb-6">
              <AlertCircle className="h-5 w-5 text-red-500" />
              <span className="text-red-700">{error}</span>
            </div>
          )}

          {/* Results Count */}
          {!loading && (
            <div className="mb-4">
              <p className="text-sm text-gray-600">
                {searchQuery ? `"${searchQuery}" için ` : ''}
                {documents.length} doküman bulundu
              </p>
            </div>
          )}

          {/* Documents List */}
          {loading ? (
            <div className="flex items-center justify-center py-8">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
            </div>
          ) : documents.length === 0 ? (
            <div className="text-center py-8">
              <FileText className="h-12 w-12 text-gray-400 mx-auto mb-4" />
              <p className="text-gray-600 mb-2">
                {searchQuery ? 'Arama kriterlerinize uygun doküman bulunamadı.' : 'Henüz doküman yüklemediniz.'}
              </p>
              {!searchQuery && (
                <p className="text-sm text-gray-500">
                  Arama yapabilmek için önce doküman yüklemeniz gerekiyor.
                </p>
              )}
            </div>
          ) : (
            <div className="space-y-4">
              {documents.map((doc) => (
                <div key={doc.id} className="border border-gray-200 rounded-lg p-4 hover:bg-gray-50 transition-colors">
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
                    <div className="flex items-center space-x-2">
                      <button
                        onClick={() => handleDocumentClick(doc.id)}
                        className="p-2 text-gray-600 hover:text-primary-600 transition-colors"
                        title="Dokümanı görüntüle"
                      >
                        <Eye className="h-4 w-4" />
                      </button>
                      <a
                        href={`${API_BASE}/documents/${doc.id}/download`}
                        className="p-2 text-gray-600 hover:text-primary-600 transition-colors"
                        title="Dokümanı indir"
                      >
                        <Download className="h-4 w-4" />
                      </a>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default DocumentSearch; 