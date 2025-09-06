import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { ResponsiveWrapper, ResponsiveCard, ResponsiveButton } from '../components/ui/responsive-wrapper';
import { API_CONFIG } from '../config/api';
import { ArrowLeft, FileText, Calendar, Shield, Download } from 'lucide-react';

interface DocumentAnalysis {
  id: number;
  filename: string;
  file_size: number;
  file_type: string;
  cvss_score: number;
  severity: string;
  vulnerability_types: string[];
  created_at: string;
  extracted_text_preview: string;
  recommendations: string[];
}

const DocumentAnalysisHistory: React.FC = () => {
  const [analyses, setAnalyses] = useState<DocumentAnalysis[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    fetchAllAnalyses();
  }, []);

  const fetchAllAnalyses = async () => {
    try {
      const response = await fetch(`${API_CONFIG.BASE_URL}/documents/history`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`,
        },
      });

      if (response.ok) {
        const data = await response.json();
        setAnalyses(data.analyses);
      } else {
        setError('Failed to load document analyses');
      }
    } catch (error) {
      setError('Error loading document analyses');
    } finally {
      setLoading(false);
    }
  };

  const getSeverityColor = (severity: string) => {
    switch (severity.toLowerCase()) {
      case 'critical': return 'text-red-600 bg-red-100';
      case 'high': return 'text-orange-600 bg-orange-100';
      case 'medium': return 'text-yellow-600 bg-yellow-100';
      case 'low': return 'text-green-600 bg-green-100';
      default: return 'text-gray-600 bg-gray-100';
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
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return (
      <ResponsiveWrapper>
        <div className="flex items-center justify-center h-64">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-primary"></div>
        </div>
      </ResponsiveWrapper>
    );
  }

  if (error) {
    return (
      <ResponsiveWrapper>
        <div className="text-center py-8">
          <div className="text-red-600 mb-4">{error}</div>
          <ResponsiveButton onClick={fetchAllAnalyses}>
            Try Again
          </ResponsiveButton>
        </div>
      </ResponsiveWrapper>
    );
  }

  return (
    <ResponsiveWrapper>
      <div className="space-y-6">
        {/* Header */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <ResponsiveButton
              variant="outline"
              size="sm"
              onClick={() => navigate('/dashboard')}
              className="flex items-center gap-2"
            >
              <ArrowLeft className="h-4 w-4" />
              Back to Dashboard
            </ResponsiveButton>
            <div>
              <h1 className="text-3xl font-bold text-gray-900">Document Analysis History</h1>
              <p className="text-gray-600">View all document analysis results</p>
            </div>
          </div>
          <ResponsiveButton
            onClick={() => navigate('/document-analyzer')}
            className="flex items-center gap-2"
          >
            <FileText className="h-4 w-4" />
            New Analysis
          </ResponsiveButton>
        </div>

        {/* Summary */}
        <ResponsiveCard>
          <div className="p-6">
            <h2 className="text-xl font-semibold mb-4">Summary</h2>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <div className="text-center p-4 bg-blue-50 rounded-lg">
                <div className="text-2xl font-bold text-blue-600">{analyses.length}</div>
                <div className="text-sm text-blue-700">Total Analyses</div>
              </div>
              <div className="text-center p-4 bg-red-50 rounded-lg">
                <div className="text-2xl font-bold text-red-600">
                  {analyses.filter(a => a.severity.toLowerCase() === 'critical').length}
                </div>
                <div className="text-sm text-red-700">Critical</div>
              </div>
              <div className="text-center p-4 bg-orange-50 rounded-lg">
                <div className="text-2xl font-bold text-orange-600">
                  {analyses.filter(a => a.severity.toLowerCase() === 'high').length}
                </div>
                <div className="text-sm text-orange-700">High</div>
              </div>
              <div className="text-center p-4 bg-green-50 rounded-lg">
                <div className="text-2xl font-bold text-green-600">
                  {analyses.reduce((sum, a) => sum + a.vulnerability_types.length, 0)}
                </div>
                <div className="text-sm text-green-700">Total Vulnerabilities</div>
              </div>
            </div>
          </div>
        </ResponsiveCard>

        {/* Analyses List */}
        <div className="space-y-4">
          {analyses.length === 0 ? (
            <ResponsiveCard>
              <div className="text-center py-8">
                <FileText className="mx-auto h-12 w-12 text-gray-400 mb-4" />
                <h3 className="text-lg font-semibold text-gray-900 mb-2">No analyses found</h3>
                <p className="text-gray-600 mb-4">Start by analyzing your first document</p>
                <ResponsiveButton onClick={() => navigate('/document-analyzer')}>
                  Analyze Document
                </ResponsiveButton>
              </div>
            </ResponsiveCard>
          ) : (
            analyses.map((analysis) => (
              <ResponsiveCard key={analysis.id}>
                <div className="p-6">
                  <div className="flex items-start justify-between mb-4">
                    <div className="flex-1">
                      <div className="flex items-center gap-3 mb-2">
                        <h3 className="text-lg font-semibold text-gray-900">{analysis.filename}</h3>
                        <span className={`px-3 py-1 rounded-full text-sm font-medium ${getSeverityColor(analysis.severity)}`}>
                          {analysis.severity.toUpperCase()}
                        </span>
                      </div>
                      <div className="flex items-center gap-6 text-sm text-gray-500 mb-3">
                        <div className="flex items-center gap-1">
                          <Calendar className="h-4 w-4" />
                          {formatDate(analysis.created_at)}
                        </div>
                        <div className="flex items-center gap-1">
                          <Shield className="h-4 w-4" />
                          CVSS: {analysis.cvss_score}
                        </div>
                        <div className="flex items-center gap-1">
                          <FileText className="h-4 w-4" />
                          {formatFileSize(analysis.file_size)}
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Vulnerabilities */}
                  <div className="mb-4">
                    <h4 className="text-sm font-medium text-gray-700 mb-2">Detected Vulnerabilities:</h4>
                    {analysis.vulnerability_types.length > 0 ? (
                      <div className="flex flex-wrap gap-2">
                        {analysis.vulnerability_types.map((type, index) => (
                          <span key={index} className="px-2 py-1 bg-red-100 text-red-800 rounded text-xs">
                            {type.replace('_', ' ')}
                          </span>
                        ))}
                      </div>
                    ) : (
                      <span className="text-gray-500 text-sm">No specific vulnerabilities detected</span>
                    )}
                  </div>

                  {/* Recommendations */}
                  {analysis.recommendations && analysis.recommendations.length > 0 && (
                    <div className="mb-4">
                      <h4 className="text-sm font-medium text-gray-700 mb-2">Recommendations:</h4>
                      <ul className="text-sm text-gray-600 space-y-1">
                        {analysis.recommendations.slice(0, 2).map((rec, index) => (
                          <li key={index} className="flex items-start gap-2">
                            <span className="text-yellow-500 mt-1">•</span>
                            <span>{rec}</span>
                          </li>
                        ))}
                        {analysis.recommendations.length > 2 && (
                          <li className="text-gray-500 text-xs">
                            +{analysis.recommendations.length - 2} more recommendations
                          </li>
                        )}
                      </ul>
                    </div>
                  )}

                  {/* Text Preview */}
                  <div>
                    <h4 className="text-sm font-medium text-gray-700 mb-2">Text Preview:</h4>
                    <div className="bg-gray-50 p-3 rounded text-sm text-gray-600 max-h-20 overflow-hidden">
                      {analysis.extracted_text_preview}
                    </div>
                  </div>
                </div>
              </ResponsiveCard>
            ))
          )}
        </div>
      </div>
    </ResponsiveWrapper>
  );
};

export default DocumentAnalysisHistory;
