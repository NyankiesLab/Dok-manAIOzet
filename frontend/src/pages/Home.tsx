import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { FileText, Upload, Search, FileSearch, Brain, Shield, Zap } from 'lucide-react';

const Home: React.FC = () => {
  const { user } = useAuth();

  const features = [
    {
      icon: <Upload className="h-8 w-8 text-primary-600" />,
      title: 'Kolay Doküman Yükleme',
      description: 'PDF, DOCX, TXT dosyalarınızı güvenle yükleyin ve organize edin.'
    },
    {
      icon: <Brain className="h-8 w-8 text-primary-600" />,
      title: 'AI Destekli Özetleme',
      description: 'Google Gemini AI ile dokümanlarınızı otomatik olarak özetleyin.'
    },
    {
      icon: <Search className="h-8 w-8 text-primary-600" />,
      title: 'Gelişmiş Arama',
      description: 'Doğal dilde arama yapın ve istediğiniz bilgiyi hızlıca bulun.'
    },
    {
      icon: <Shield className="h-8 w-8 text-primary-600" />,
      title: 'Güvenli Saklama',
      description: 'Dokümanlarınız güvenli bir şekilde saklanır ve korunur.'
    }
  ];

  return (
    <div className="max-w-7xl mx-auto">
      {/* Hero Section */}
      <div className="text-center py-16">
        <div className="flex justify-center mb-6">
          <FileText className="h-16 w-16 text-primary-600" />
        </div>
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          AI Destekli Doküman Yönetim Sistemi
        </h1>
        <p className="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
          Dokümanlarınızı yükleyin, AI ile özetleyin ve gelişmiş arama özellikleriyle 
          istediğiniz bilgiyi hızlıca bulun.
        </p>
        
        {user ? (
          <div className="flex justify-center space-x-4">
            <Link
              to="/upload"
              className="flex items-center space-x-2 px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
            >
              <Upload className="h-5 w-5" />
              <span>Doküman Yükle</span>
            </Link>
            <Link
              to="/search"
              className="flex items-center space-x-2 px-6 py-3 border border-primary-600 text-primary-600 rounded-lg hover:bg-primary-50 transition-colors"
            >
              <Search className="h-5 w-5" />
              <span>Doküman Ara</span>
            </Link>
          </div>
        ) : (
          <div className="flex justify-center space-x-4">
            <Link
              to="/register"
              className="px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
            >
              Hemen Başla
            </Link>
            <Link
              to="/login"
              className="px-6 py-3 border border-primary-600 text-primary-600 rounded-lg hover:bg-primary-50 transition-colors"
            >
              Giriş Yap
            </Link>
          </div>
        )}
      </div>

      {/* Features Section */}
      <div className="py-16">
        <h2 className="text-3xl font-bold text-center text-gray-900 mb-12">
          Özellikler
        </h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature, index) => (
            <div key={index} className="text-center p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow">
              <div className="flex justify-center mb-4">
                {feature.icon}
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                {feature.title}
              </h3>
              <p className="text-gray-600">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>

      {/* Stats Section */}
      <div className="py-16 bg-primary-50 rounded-lg">
        <div className="text-center mb-12">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">
            Neden Doküman Forum?
          </h2>
          <p className="text-xl text-gray-600">
            Modern teknolojilerle güçlendirilmiş doküman yönetim deneyimi
          </p>
        </div>
        
        <div className="grid md:grid-cols-3 gap-8">
          <div className="text-center">
            <div className="flex justify-center mb-4">
              <Zap className="h-12 w-12 text-primary-600" />
            </div>
            <h3 className="text-2xl font-bold text-gray-900 mb-2">Hızlı</h3>
            <p className="text-gray-600">Saniyeler içinde doküman yükleme ve işleme</p>
          </div>
          
          <div className="text-center">
            <div className="flex justify-center mb-4">
              <Brain className="h-12 w-12 text-primary-600" />
            </div>
            <h3 className="text-2xl font-bold text-gray-900 mb-2">Akıllı</h3>
            <p className="text-gray-600">AI destekli özetleme ve anahtar kelime çıkarımı</p>
          </div>
          
          <div className="text-center">
            <div className="flex justify-center mb-4">
              <Shield className="h-12 w-12 text-primary-600" />
            </div>
            <h3 className="text-2xl font-bold text-gray-900 mb-2">Güvenli</h3>
            <p className="text-gray-600">JWT tabanlı güvenli kimlik doğrulama</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home; 