# 📖 Manual de Usuario - CVSS Scoring System

## 🎯 **Introducción**

El **CVSS Scoring System** es una aplicación web completa para la evaluación y gestión de vulnerabilidades de seguridad usando el estándar CVSS v3.1. Este manual te guiará a través de todas las funcionalidades del sistema.

## 🚀 **Acceso al Sistema**

### **URLs de Acceso**
- **Sistema Local**: http://localhost:3001
- **Sistema Desplegado**: https://tu-sitio.netlify.app

### **Credenciales por Defecto**
- **Email**: admin@cvss.com
- **Password**: admin123
- **Rol**: Administrador

## 🔐 **Sistema de Autenticación**

### **Roles de Usuario**

#### **👑 Administrador (Admin)**
- ✅ Acceso completo a todas las funcionalidades
- ✅ Gestión de usuarios
- ✅ Database Manager
- ✅ Configuración del sistema
- ✅ Auditoría completa

#### **🔍 Analista (Analyst)**
- ✅ Crear y editar vulnerabilidades
- ✅ Realizar evaluaciones CVSS
- ✅ Analizar documentos
- ✅ Generar reportes
- ❌ Gestión de usuarios
- ❌ Database Manager

#### **👁️ Visualizador (Viewer)**
- ✅ Ver vulnerabilidades
- ✅ Ver evaluaciones
- ✅ Ver reportes
- ❌ Crear o editar contenido
- ❌ Analizar documentos

### **Inicio de Sesión**
1. Ve a la página de login
2. Ingresa tu email y contraseña
3. Haz clic en **"Sign In"**
4. Serás redirigido al dashboard principal

## 🏠 **Dashboard Principal**

### **Vista General**
El dashboard es tu centro de control principal donde puedes ver:

#### **📊 KPIs Principales**
- **Total Vulnerabilities**: Número total de vulnerabilidades registradas
- **Critical Vulnerabilities**: Vulnerabilidades con severidad crítica
- **Total Evaluations**: Evaluaciones CVSS realizadas
- **Document Analyses**: Análisis de documentos realizados

#### **📈 Gráficos Interactivos**
- **Severity Distribution**: Distribución de vulnerabilidades por severidad
- **Temporal Trend**: Tendencia temporal de vulnerabilidades
- **Evaluation Timeline**: Línea de tiempo de evaluaciones

#### **📄 Document Analysis Card**
- Resumen de análisis de documentos recientes
- Acceso rápido al Document Analyzer
- Vista del historial de análisis

### **Navegación Principal**
- **Dashboard**: Vista principal con KPIs y gráficos
- **Vulnerabilities**: Gestión de vulnerabilidades
- **Document Analyzer**: Análisis de documentos PDF/Word
- **Audit Logs**: Registro de actividades del sistema
- **Database Manager**: Gestión de base de datos (solo Admin)

## 🔍 **Gestión de Vulnerabilidades**

### **Ver Lista de Vulnerabilidades**
1. Haz clic en **"Vulnerabilities"** en el menú principal
2. Verás una tabla con todas las vulnerabilidades
3. Usa los filtros para buscar vulnerabilidades específicas

### **Crear Nueva Vulnerabilidad**
1. En la página de vulnerabilidades, haz clic en **"Add Vulnerability"**
2. Completa el formulario:
   - **Title**: Título descriptivo de la vulnerabilidad
   - **Description**: Descripción detallada
   - **CVE ID**: Identificador CVE (opcional)
   - **Status**: Estado actual (Open, In Progress, Closed)
   - **Source**: Fuente de la vulnerabilidad
3. Haz clic en **"Save"**

### **Editar Vulnerabilidad**
1. En la lista de vulnerabilidades, haz clic en el botón **"Edit"**
2. Modifica los campos necesarios
3. Haz clic en **"Save"**

### **Evaluar Vulnerabilidad**
1. En la lista de vulnerabilidades, haz clic en **"Evaluations"**
2. Haz clic en **"Add Evaluation"**
3. Usa la **Calculadora CVSS** o ingresa un vector manualmente
4. Completa las métricas:
   - **Base Metrics**: Attack Vector, Attack Complexity, etc.
   - **Temporal Metrics**: Exploitability, Remediation Level, etc.
   - **Environmental Metrics**: Collateral Damage, Target Distribution, etc.
5. Haz clic en **"Save Evaluation"**

## 📄 **Document Analyzer**

### **Acceder al Document Analyzer**
1. Haz clic en **"Document Analyzer"** en el menú principal
2. O desde el dashboard, haz clic en **"New Analysis"** en la Document Analysis Card

### **Analizar Documento**
1. **Seleccionar Archivo**:
   - Arrastra y suelta un archivo PDF o Word
   - O haz clic en el área de carga para seleccionar
   - Formatos soportados: PDF, DOC, DOCX
   - Tamaño máximo: 16MB

2. **Analizar**:
   - Haz clic en **"Analyze Document"**
   - El sistema procesará el archivo automáticamente
   - Espera a que se complete el análisis

3. **Revisar Resultados**:
   - **Analysis Summary**: Score CVSS, severidad, archivo procesado
   - **Detected Vulnerabilities**: Tipos de vulnerabilidades encontradas
   - **CVSS Components**: Desglose detallado de la evaluación
   - **Recommendations**: Acciones sugeridas para mitigación
   - **Extracted Text Preview**: Texto extraído del documento

### **Gestión de Resultados**
- **Ver en Dashboard**: Los análisis aparecen automáticamente en la Document Analysis Card
- **Add to Dashboard**: Convierte el análisis en una vulnerabilidad del sistema principal
- **Back to Dashboard**: Regresa al panel principal

### **Historial de Análisis**
1. Haz clic en **"View All"** en la Document Analysis Card
2. O navega a **"Document Analysis History"** desde el menú
3. Verás una lista completa de todos los análisis realizados
4. Haz clic en cualquier análisis para ver detalles completos

## 📊 **Generación de Reportes**

### **Exportar Datos**
1. En el dashboard, haz clic en **"Export CSV"** o **"Export PDF"**
2. Selecciona las opciones de filtrado:
   - **Date Range**: Rango de fechas
   - **Severity**: Filtro por severidad
   - **Status**: Filtro por estado
3. Haz clic en **"Generate Report"**
4. Descarga el archivo generado

### **Tipos de Reportes**
- **CSV**: Datos en formato de hoja de cálculo
- **PDF**: Reporte profesional con gráficos y diseño

## 🔍 **Auditoría y Logs**

### **Ver Logs de Auditoría**
1. Haz clic en **"Audit Logs"** en el menú principal
2. Verás un registro detallado de todas las actividades
3. Usa los filtros para buscar actividades específicas

### **Información de Logs**
- **Timestamp**: Fecha y hora de la actividad
- **User**: Usuario que realizó la acción
- **Action**: Tipo de acción realizada
- **Resource**: Recurso afectado
- **IP Address**: Dirección IP del usuario
- **Details**: Detalles adicionales

## 🗄️ **Database Manager (Solo Admin)**

### **Acceder al Database Manager**
1. Haz clic en **"Database Manager"** en el menú principal
2. Solo disponible para usuarios con rol Admin

### **Funcionalidades Disponibles**
- **Table Structure**: Ver estructura de tablas
- **Custom Queries**: Ejecutar consultas SQL personalizadas
- **Data Export**: Exportar datos de la base de datos
- **User Management**: Gestionar usuarios del sistema

### **Ejecutar Consultas SQL**
1. Ve a la sección **"Custom Queries"**
2. Escribe tu consulta SQL
3. Haz clic en **"Execute Query"**
4. Revisa los resultados

⚠️ **Advertencia**: Ten cuidado con las consultas SQL. Las consultas destructivas pueden afectar la integridad de los datos.

## 🔧 **Configuración y Personalización**

### **Perfil de Usuario**
1. Haz clic en tu nombre en la esquina superior derecha
2. Selecciona **"Profile"**
3. Actualiza tu información personal
4. Cambia tu contraseña si es necesario

### **Configuración del Sistema**
- **Theme**: El sistema usa un tema claro por defecto
- **Language**: Interfaz en inglés
- **Timezone**: Configurado automáticamente

## 🚨 **Solución de Problemas Comunes**

### **No Puedo Iniciar Sesión**
1. Verifica que estés usando las credenciales correctas
2. Asegúrate de que el sistema esté funcionando
3. Contacta al administrador si el problema persiste

### **Error al Analizar Documento**
1. Verifica que el archivo sea PDF, DOC o DOCX
2. Asegúrate de que el archivo sea menor a 16MB
3. Verifica que el archivo no esté corrupto

### **Error al Generar Reporte**
1. Verifica que tengas permisos para generar reportes
2. Asegúrate de que haya datos para exportar
3. Intenta con un rango de fechas diferente

### **Problemas de Rendimiento**
1. Cierra pestañas innecesarias del navegador
2. Verifica tu conexión a internet
3. Contacta al administrador si el problema persiste

## 📱 **Uso en Dispositivos Móviles**

### **Compatibilidad**
- ✅ **Smartphones**: iOS 12+, Android 8+
- ✅ **Tablets**: iPad, Android tablets
- ✅ **Navegadores**: Chrome, Safari, Firefox, Edge

### **Funcionalidades Móviles**
- ✅ Navegación completa
- ✅ Análisis de documentos
- ✅ Visualización de reportes
- ✅ Gestión de vulnerabilidades
- ✅ Dashboard responsive

## 🔒 **Seguridad y Privacidad**

### **Medidas de Seguridad**
- **Autenticación JWT**: Tokens seguros para sesiones
- **CORS**: Configuración de seguridad para requests
- **Validación**: Validación de entrada en todos los formularios
- **Auditoría**: Registro completo de todas las actividades

### **Privacidad de Datos**
- Los datos se almacenan de forma segura
- Solo usuarios autorizados pueden acceder a la información
- Se mantiene un registro de auditoría de todas las actividades
- Los archivos subidos se procesan y eliminan automáticamente

## 📞 **Soporte y Contacto**

### **Recursos de Ayuda**
- **Documentación**: README.md, INSTALLATION_GUIDE.md
- **Issues**: Crear un issue en GitHub
- **Logs**: Revisar logs de auditoría para debugging

### **Contacto**
- **Email**: admin@cvss.com
- **GitHub**: [Repositorio del proyecto]
- **Documentación**: [Enlaces a documentación]

## 🎯 **Mejores Prácticas**

### **Gestión de Vulnerabilidades**
1. **Títulos Descriptivos**: Usa títulos claros y descriptivos
2. **Descripciones Detalladas**: Incluye información técnica relevante
3. **CVE IDs**: Incluye identificadores CVE cuando estén disponibles
4. **Estados Actualizados**: Mantén el estado de las vulnerabilidades actualizado

### **Evaluaciones CVSS**
1. **Métricas Precisas**: Usa las métricas CVSS correctas
2. **Justificación**: Documenta el razonamiento detrás de las evaluaciones
3. **Revisión**: Revisa las evaluaciones regularmente
4. **Actualización**: Actualiza las evaluaciones cuando cambien las circunstancias

### **Análisis de Documentos**
1. **Archivos Limpios**: Asegúrate de que los archivos no estén corruptos
2. **Contenido Relevante**: Sube documentos que contengan información de vulnerabilidades
3. **Revisión de Resultados**: Revisa siempre los resultados del análisis
4. **Conversión**: Convierte hallazgos importantes a vulnerabilidades del sistema

### **Seguridad**
1. **Contraseñas Fuertes**: Usa contraseñas seguras
2. **Cierre de Sesión**: Cierra sesión cuando termines
3. **Acceso Limitado**: Solo comparte credenciales con usuarios autorizados
4. **Auditoría**: Revisa regularmente los logs de auditoría

---

**¡Bienvenido al CVSS Scoring System!** 🎉

Este manual te ayudará a aprovechar al máximo todas las funcionalidades del sistema. Si tienes preguntas o necesitas ayuda, no dudes en contactar al equipo de soporte.
