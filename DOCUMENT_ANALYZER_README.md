# 📄 Document Analyzer - CVSS Scoring System

## 🚀 **Funcionalidad Completa Implementada**

Se ha implementado un **Document Analyzer** completo que permite subir archivos PDF y Word para detectar automáticamente vulnerabilidades, generar evaluaciones CVSS, y gestionar los resultados con una arquitectura híbrida integrada al dashboard principal.

## ✨ **Características Principales**

### **📁 Formatos Soportados**
- **PDF** (.pdf)
- **Microsoft Word** (.doc, .docx)
- **Tamaño máximo**: 16MB

### **🔍 Detección Automática de Vulnerabilidades**
El sistema detecta automáticamente los siguientes tipos de vulnerabilidades:

- **SQL Injection** - Inyección SQL
- **XSS** - Cross-Site Scripting
- **CSRF** - Cross-Site Request Forgery
- **Authentication Bypass** - Bypass de Autenticación
- **Authorization Issues** - Problemas de Autorización
- **Code Injection** - Inyección de Código
- **Crypto Vulnerabilities** - Vulnerabilidades Criptográficas
- **Network Vulnerabilities** - Vulnerabilidades de Red

### **📊 Evaluación CVSS Automática**
- **Cálculo automático** del score CVSS basado en el contenido del documento
- **Detección de componentes CVSS**:
  - Attack Vector (Red, Adyacente, Local, Físico)
  - Attack Complexity (Baja, Alta)
  - Privileges Required (Ninguno, Bajo, Alto)
  - User Interaction (Ninguna, Requerida)
  - Scope (Sin Cambio, Con Cambio)
  - Confidentiality, Integrity, Availability (Ninguno, Bajo, Alto)

### **💡 Recomendaciones Inteligentes**
El sistema genera recomendaciones específicas basadas en:
- **Tipos de vulnerabilidades detectadas**
- **Score CVSS calculado**
- **Mejores prácticas de seguridad**

### **🏗️ Arquitectura Híbrida**
- **Almacenamiento separado** de análisis de documentos en tabla dedicada
- **Vista en dashboard** con resumen de análisis recientes
- **Conversión opcional** de hallazgos a vulnerabilidades del sistema principal
- **Historial completo** de análisis con vista detallada
- **Integración perfecta** con el flujo de trabajo existente

## 🛠️ **Implementación Técnica**

### **Backend (Flask)**
- **Nuevos endpoints**:
  - `/api/documents/analyze` - Análisis de documentos
  - `/api/documents/history` - Historial de análisis
  - `/api/documents/history/<id>` - Detalle de análisis específico
  - `/api/documents/supported-formats` - Formatos soportados
- **Nuevo modelo**: `DocumentAnalysis` para almacenar resultados
- **Dependencias agregadas**:
  - `PyPDF2==3.0.1` - Para extraer texto de PDFs
  - `python-docx==1.1.0` - Para extraer texto de documentos Word
- **Funcionalidades**:
  - Extracción de texto de documentos
  - Análisis de patrones de vulnerabilidades
  - Cálculo de scores CVSS
  - Generación de recomendaciones
  - Almacenamiento en base de datos
  - Integración con sistema de auditoría
  - Conversión a vulnerabilidades del sistema principal

### **Frontend (React)**
- **Nuevos componentes**:
  - `DocumentAnalyzer.tsx` - Interfaz principal de análisis
  - `DocumentAnalysisCard.tsx` - Tarjeta de resumen en dashboard
  - `DocumentAnalysisHistory.tsx` - Página de historial completo
- **Características**:
  - Interfaz drag-and-drop para subir archivos
  - Diseño responsive con Tailwind CSS
  - Visualización detallada de resultados
  - Interfaz completamente en inglés
  - Integración con sistema de autenticación
  - Botón "Add to Dashboard" para conversión
  - Historial completo de análisis
  - Navegación fluida entre secciones

### **Navegación**
- **Nuevas rutas**:
  - `/document-analyzer` - Análisis de documentos
  - `/document-analysis-history` - Historial de análisis
- **Acceso**: Disponible para todos los usuarios autenticados
- **Integración**: Tarjeta de resumen en dashboard principal

## 📋 **Cómo Usar**

### **1. Acceder al Analizador**
- Inicia sesión en el sistema
- Haz clic en **"Document Analyzer"** en el header del dashboard
- O navega directamente a `/document-analyzer`

### **2. Subir Documento**
- Arrastra y suelta un archivo PDF o Word
- O haz clic en el área de carga para seleccionar un archivo
- El archivo debe ser menor a 16MB

### **3. Analizar**
- Haz clic en **"Analizar Documento"**
- El sistema procesará el archivo y extraerá el texto
- Se detectarán automáticamente las vulnerabilidades

### **4. Revisar Resultados**
- **Resumen**: Score CVSS, severidad, archivo procesado
- **Vulnerabilidades Detectadas**: Lista de tipos encontrados
- **Componentes CVSS**: Desglose detallado de la evaluación
- **Recomendaciones**: Acciones sugeridas para mitigar riesgos
- **Vista Previa**: Texto extraído del documento
- **Estado de Guardado**: Confirmación de almacenamiento en base de datos

### **5. Gestión de Resultados**
- **Ver en Dashboard**: Los análisis aparecen automáticamente en la tarjeta "Document Analysis"
- **Convertir a Vulnerabilidad**: Usa el botón "Add to Dashboard" para crear una vulnerabilidad del sistema principal
- **Ver Historial**: Accede a "Document Analysis History" para ver todos los análisis realizados
- **Navegación**: Usa "Back to Dashboard" para regresar al panel principal

## 🔧 **Ejemplo de Uso**

### **Documento de Entrada**
```
REPORTE DE VULNERABILIDADES

1. SQL INJECTION
- El sistema es vulnerable a inyección SQL
- Severidad: CRITICAL

2. CROSS-SITE SCRIPTING (XSS)
- Vulnerabilidad XSS en formularios
- Severidad: HIGH
```

### **Resultado del Análisis**
- **Score CVSS**: 9.8
- **Severidad**: Critical
- **Vulnerabilidades**: SQL Injection, XSS
- **Componentes CVSS**: Attack Vector (Network), Attack Complexity (Low), etc.
- **Recomendaciones**:
  1. HIGH PRIORITY: This vulnerability should be fixed soon
  2. Implement prepared statements for SQL queries
  3. Sanitize user input to prevent XSS attacks
- **Estado**: Guardado en base de datos ✓
- **Opciones**: 
  - Ver en Dashboard (automático)
  - Convertir a Vulnerabilidad (botón "Add to Dashboard")
  - Ver Historial Completo

## 🚀 **Despliegue**

### **Backend (Render.com)**
- Las nuevas dependencias se instalarán automáticamente
- Los endpoints estarán disponibles en:
  - `https://cvss-scoring-system.onrender.com/api/documents/analyze`
  - `https://cvss-scoring-system.onrender.com/api/documents/history`
  - `https://cvss-scoring-system.onrender.com/api/documents/supported-formats`

### **Frontend (Netlify)**
- Los nuevos componentes se desplegarán automáticamente
- Accesible en:
  - `https://tu-sitio.netlify.app/document-analyzer`
  - `https://tu-sitio.netlify.app/document-analysis-history`
- La tarjeta de resumen aparecerá automáticamente en el dashboard

## 🔒 **Seguridad**

- **Autenticación requerida** para acceder al analizador
- **Validación de tipos de archivo** (solo PDF, DOC, DOCX)
- **Límite de tamaño** (16MB máximo)
- **Archivos temporales** se eliminan automáticamente después del procesamiento
- **Auditoría completa** de todas las operaciones de análisis

## 📈 **Beneficios**

1. **Automatización**: Reduce el tiempo de análisis manual
2. **Consistencia**: Aplica criterios estándar CVSS
3. **Eficiencia**: Procesa documentos en segundos
4. **Precisión**: Detecta patrones de vulnerabilidades conocidas
5. **Trazabilidad**: Registra todas las operaciones en auditoría
6. **Accesibilidad**: Interfaz intuitiva y responsive
7. **Integración**: Arquitectura híbrida que se integra perfectamente con el sistema existente
8. **Flexibilidad**: Permite convertir hallazgos a vulnerabilidades del sistema principal
9. **Historial**: Mantiene un registro completo de todos los análisis realizados
10. **Escalabilidad**: Diseño modular que permite futuras extensiones

## 🎯 **Casos de Uso**

- **Auditorías de seguridad**: Analizar reportes de vulnerabilidades
- **Revisión de código**: Procesar documentación técnica
- **Compliance**: Evaluar documentos de cumplimiento
- **Educación**: Enseñar sobre vulnerabilidades comunes
- **Investigación**: Analizar documentos de investigación de seguridad

## 🔧 **Estructura de Base de Datos**

### **Tabla: document_analyses**
```sql
CREATE TABLE document_analyses (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    filename VARCHAR(255) NOT NULL,
    file_size INTEGER NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    extracted_text TEXT,
    vulnerability_types TEXT, -- JSON array
    cvss_score FLOAT,
    severity VARCHAR(20),
    cvss_components TEXT, -- JSON object
    recommendations TEXT, -- JSON array
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

## 🚀 **Instalación y Configuración**

### **Dependencias Backend**
```bash
pip install PyPDF2==3.0.1 python-docx==1.1.0
```

### **Variables de Entorno**
```bash
# Backend
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret

# Frontend
VITE_API_URL=https://your-backend-url.com
```

### **Migración de Base de Datos**
```bash
# El modelo DocumentAnalysis se crea automáticamente
# No se requieren migraciones adicionales
```

---

**¡El Document Analyzer está completamente implementado y listo para usar!** 🎉

Sube tus documentos PDF o Word, analiza vulnerabilidades automáticamente, y gestiona los resultados con la arquitectura híbrida integrada al dashboard principal.
