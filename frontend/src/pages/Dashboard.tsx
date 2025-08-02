import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext.tsx';
import { FileText, Upload, Search, FileSearch, User, Calendar, HardDrive } from 'lucide-react';
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

const Dashboard: React.FC = () => {
  const { user, token } = useAuth();
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loading, setLoading] = useState(true);
  const [stats, setStats] = useState({
    totalDocs: 0,
    totalSize: 0,
    recentDocs: 0
  });

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
      
      const docs = response.data;
      setDocuments(docs);
      
      const totalSize = docs.reduce((sum: number, doc: Document) => sum + doc.file_size, 0);
      const recentDocs = docs.filter((doc: Document) => {
        const docDate = new Date(doc.created_at);
        const weekAgo = new Date();
        weekAgo.setDate(weekAgo.getDate() - 7);
        return docDate > weekAgo;
      }).length;

      setStats({
        totalDocs: docs.length,
        totalSize: totalSize,
        recentDocs: recentDocs
      });
    } catch (error) {
      console.error('Dokümanlar yüklenemedi:', error);
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

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          Hoş geldiniz, {user?.username}!
        </h1>
        <p className="text-gray-600">
          Dokümanlarınızı yönetin ve AI destekli özelliklerden yararlanın.
        </p>
      </div>

      {/* Stats Cards */}
      <div className="grid md:grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <div className="flex items-center">
            <div className="p-3 rounded-full bg-primary-100">
              <FileText className="h-6 w-6 text-primary-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-600">Toplam Doküman</p>
              <p className="text-2xl font-semibold text-gray-900">{stats.totalDocs}</p>
            </div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-md">
          <div className="flex items-center">
            <div className="p-3 rounded-full bg-green-100">
              <HardDrive className="h-6 w-6 text-green-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-600">Toplam Boyut</p>
              <p className="text-2xl font-semibold text-gray-900">{formatFileSize(stats.totalSize)}</p>
            </div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow-md">
          <div className="flex items-center">
            <div className="p-3 rounded-full bg-yellow-100">
              <Calendar className="h-6 w-6 text-yellow-600" />
            </div>
            <div className="ml-4">
              <p className="text-sm font-medium text-gray-600">Bu Hafta</p>
              <p className="text-2xl font-semibold text-gray-900">{stats.recentDocs}</p>
            </div>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="grid md:grid-cols-3 gap-6 mb-8">
        <Link
          to="/upload"
          className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow border-2 border-dashed border-gray-300 hover:border-primary-300"
        >
          <div className="text-center">
            <Upload className="h-12 w-12 text-primary-600 mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Yeni Doküman</h3>
            <p className="text-gray-600">PDF, DOCX, TXT dosyalarınızı yükleyin</p>
          </div>
        </Link>

        <Link
          to="/search"
          className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow"
        >
          <div className="text-center">
            <Search className="h-12 w-12 text-primary-600 mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-gray-900 mb-2">Doküman Ara</h3>
            <p className="text-gray-600">Gelişmiş arama özellikleriyle arayın</p>
          </div>
        </Link>

        <Link
          to="/summary"
          className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow"
        >
          <div className="text-center">
            <FileSearch className="h-12 w-12 text-primary-600 mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-gray-900 mb-2">AI Özetleme</h3>
            <p className="text-gray-600">Dokümanlarınızı AI ile özetleyin</p>
          </div>
        </Link>
      </div>

      {/* Recent Documents */}
      <div className="bg-white rounded-lg shadow-md">
        <div className="px-6 py-4 border-b border-gray-200">
          <h2 className="text-xl font-semibold text-gray-900">Son Dokümanlar</h2>
        </div>
        
        <div className="p-6">
          {documents.length === 0 ? (
            <div className="text-center py-8">
              <FileText className="h-12 w-12 text-gray-400 mx-auto mb-4" />
              <p className="text-gray-600 mb-4">Henüz doküman yüklemediniz.</p>
              <Link
                to="/upload"
                className="inline-flex items-center px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700"
              >
                <Upload className="h-4 w-4 mr-2" />
                İlk Dokümanınızı Yükleyin
              </Link>
            </div>
          ) : (
            <div className="space-y-4">
              {documents.slice(0, 5).map((doc) => (
                <div key={doc.id} className="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:bg-gray-50">
                  <div className="flex items-center space-x-4">
                    <div className="p-2 bg-primary-100 rounded-lg">
                      <FileText className="h-5 w-5 text-primary-600" />
                    </div>
                    <div>
                      <h3 className="font-medium text-gray-900">{doc.title}</h3>
                      <p className="text-sm text-gray-600">
                        {doc.filename} • {formatFileSize(doc.file_size)} • {doc.file_type.toUpperCase()}
                      </p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className="text-sm text-gray-600">{formatDate(doc.created_at)}</p>
                    {doc.summary && (
                      <p className="text-xs text-green-600">✓ Özetlendi</p>
                    )}
                  </div>
                </div>
              ))}
              
              {documents.length > 5 && (
                <div className="text-center pt-4">
                  <Link
                    to="/search"
                    className="text-primary-600 hover:text-primary-700 font-medium"
                  >
                    Tüm dokümanları görüntüle ({documents.length})
                  </Link>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Dashboard; 