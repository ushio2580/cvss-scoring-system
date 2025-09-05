# 📄 Analizador de Documentos - CVSS Scoring System

## 🚀 **Nueva Funcionalidad Implementada**

Se ha agregado un **Analizador de Documentos** que permite subir archivos PDF y Word para detectar automáticamente vulnerabilidades y generar evaluaciones CVSS.

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

## 🛠️ **Implementación Técnica**

### **Backend (Flask)**
- **Nuevo endpoint**: `/api/documents/analyze`
- **Dependencias agregadas**:
  - `PyPDF2==3.0.1` - Para extraer texto de PDFs
  - `python-docx==1.1.0` - Para extraer texto de documentos Word
- **Funcionalidades**:
  - Extracción de texto de documentos
  - Análisis de patrones de vulnerabilidades
  - Cálculo de scores CVSS
  - Generación de recomendaciones
  - Integración con sistema de auditoría

### **Frontend (React)**
- **Nuevo componente**: `DocumentAnalyzer.tsx`
- **Características**:
  - Interfaz drag-and-drop para subir archivos
  - Diseño responsive con Tailwind CSS
  - Visualización detallada de resultados
  - Traducción de términos técnicos al español
  - Integración con sistema de autenticación

### **Navegación**
- **Nueva ruta**: `/document-analyzer`
- **Acceso**: Disponible para todos los usuarios autenticados
- **Botón de navegación** agregado al header del dashboard

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
- **Recomendaciones**:
  1. Implementar prepared statements
  2. Sanitizar entrada de usuario
  3. URGENTE: Atención inmediata requerida

## 🚀 **Despliegue**

### **Backend (Render.com)**
- Las nuevas dependencias se instalarán automáticamente
- El endpoint estará disponible en: `https://cvss-scoring-system.onrender.com/api/documents/analyze`

### **Frontend (Netlify)**
- El nuevo componente se desplegará automáticamente
- Accesible en: `https://tu-sitio.netlify.app/document-analyzer`

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

## 🎯 **Casos de Uso**

- **Auditorías de seguridad**: Analizar reportes de vulnerabilidades
- **Revisión de código**: Procesar documentación técnica
- **Compliance**: Evaluar documentos de cumplimiento
- **Educación**: Enseñar sobre vulnerabilidades comunes
- **Investigación**: Analizar documentos de investigación de seguridad

---

**¡El Analizador de Documentos está listo para usar!** 🎉

Sube tus documentos PDF o Word y descubre automáticamente las vulnerabilidades y sus evaluaciones CVSS.
