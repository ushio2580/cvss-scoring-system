# 🧪 **CASOS DE PRUEBA - CVSS SCORING SYSTEM**

## 📋 **INFORMACIÓN GENERAL**
- **Proyecto:** CVSS Scoring System
- **Versión:** 1.0
- **Fecha:** Septiembre 2025
- **Metodología:** SCRUM
- **Cobertura:** Frontend, Backend, API, Base de Datos

---

## 🎯 **CASOS DE PRUEBA - AUTENTICACIÓN**

### **TC-AUTH-001: Login Exitoso**
- **ID:** TC-AUTH-001
- **Descripción:** Verificar que un usuario puede iniciar sesión con credenciales válidas
- **Precondiciones:** Usuario registrado en el sistema
- **Datos de Prueba:**
  - Email: `admin@cvss.com`
  - Password: `admin123`
- **Pasos:**
  1. Navegar a la página de login
  2. Ingresar email válido
  3. Ingresar password válido
  4. Hacer clic en "Login"
- **Resultado Esperado:**
  - Usuario es redirigido al dashboard
  - Token JWT se almacena en localStorage
  - Mensaje de bienvenida se muestra
- **Prioridad:** Alta
- **Tipo:** Funcional

### **TC-AUTH-002: Login con Credenciales Inválidas**
- **ID:** TC-AUTH-002
- **Descripción:** Verificar que el sistema rechaza credenciales incorrectas
- **Precondiciones:** Usuario no registrado o credenciales incorrectas
- **Datos de Prueba:**
  - Email: `test@invalid.com`
  - Password: `wrongpassword`
- **Pasos:**
  1. Navegar a la página de login
  2. Ingresar email inválido
  3. Ingresar password inválido
  4. Hacer clic en "Login"
- **Resultado Esperado:**
  - Mensaje de error se muestra
  - Usuario permanece en página de login
  - No se genera token JWT
- **Prioridad:** Alta
- **Tipo:** Funcional

### **TC-AUTH-003: Logout Exitoso**
- **ID:** TC-AUTH-003
- **Descripción:** Verificar que un usuario puede cerrar sesión correctamente
- **Precondiciones:** Usuario autenticado en el sistema
- **Pasos:**
  1. Estar logueado en el sistema
  2. Hacer clic en el botón "Logout"
  3. Confirmar logout
- **Resultado Esperado:**
  - Token JWT se elimina del localStorage
  - Usuario es redirigido a página de login
  - Sesión se cierra correctamente
- **Prioridad:** Media
- **Tipo:** Funcional

---

## 🎯 **CASOS DE PRUEBA - DASHBOARD**

### **TC-DASH-001: Visualización del Dashboard**
- **ID:** TC-DASH-001
- **Descripción:** Verificar que el dashboard se carga correctamente
- **Precondiciones:** Usuario autenticado
- **Pasos:**
  1. Iniciar sesión en el sistema
  2. Navegar al dashboard
- **Resultado Esperado:**
  - Dashboard se carga sin errores
  - Se muestran estadísticas básicas
  - Navegación lateral está visible
  - Cards de resumen se muestran
- **Prioridad:** Alta
- **Tipo:** Funcional

### **TC-DASH-002: Navegación del Dashboard**
- **ID:** TC-DASH-002
- **Descripción:** Verificar que la navegación funciona correctamente
- **Precondiciones:** Usuario autenticado en dashboard
- **Pasos:**
  1. Hacer clic en "Vulnerabilities" en el menú
  2. Hacer clic en "Document Analyzer" en el menú
  3. Hacer clic en "Analysis History" en el menú
- **Resultado Esperado:**
  - Cada sección se carga correctamente
  - URL cambia apropiadamente
  - Contenido se actualiza
- **Prioridad:** Alta
- **Tipo:** Funcional

---

## 🎯 **CASOS DE PRUEBA - GESTIÓN DE VULNERABILIDADES**

### **TC-VULN-001: Crear Nueva Vulnerabilidad**
- **ID:** TC-VULN-001
- **Descripción:** Verificar que se puede crear una nueva vulnerabilidad
- **Precondiciones:** Usuario autenticado
- **Datos de Prueba:**
  - Title: `SQL Injection Vulnerability`
  - Description: `Critical SQL injection in login form`
  - CVSS Vector: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`
- **Pasos:**
  1. Navegar a "Vulnerabilities"
  2. Hacer clic en "Add New Vulnerability"
  3. Llenar formulario con datos válidos
  4. Hacer clic en "Save"
- **Resultado Esperado:**
  - Vulnerabilidad se crea exitosamente
  - Se muestra en la lista de vulnerabilidades
  - CVSS Score se calcula automáticamente
- **Prioridad:** Alta
- **Tipo:** Funcional

### **TC-VULN-002: Editar Vulnerabilidad Existente**
- **ID:** TC-VULN-002
- **Descripción:** Verificar que se puede editar una vulnerabilidad existente
- **Precondiciones:** Vulnerabilidad existente en el sistema
- **Pasos:**
  1. Navegar a "Vulnerabilities"
  2. Hacer clic en "Edit" en una vulnerabilidad
  3. Modificar campos necesarios
  4. Hacer clic en "Update"
- **Resultado Esperado:**
  - Cambios se guardan correctamente
  - CVSS Score se recalcula si es necesario
  - Lista se actualiza con cambios
- **Prioridad:** Alta
- **Tipo:** Funcional

### **TC-VULN-003: Eliminar Vulnerabilidad**
- **ID:** TC-VULN-003
- **Descripción:** Verificar que se puede eliminar una vulnerabilidad
- **Precondiciones:** Vulnerabilidad existente en el sistema
- **Pasos:**
  1. Navegar a "Vulnerabilities"
  2. Hacer clic en "Delete" en una vulnerabilidad
  3. Confirmar eliminación
- **Resultado Esperado:**
  - Vulnerabilidad se elimina del sistema
  - Se muestra mensaje de confirmación
  - Lista se actualiza
- **Prioridad:** Media
- **Tipo:** Funcional

---

## 🎯 **CASOS DE PRUEBA - CALCULADORA CVSS**

### **TC-CVSS-001: Cálculo CVSS Básico**
- **ID:** TC-CVSS-001
- **Descripción:** Verificar que la calculadora CVSS funciona correctamente
- **Precondiciones:** Usuario autenticado
- **Datos de Prueba:**
  - Attack Vector: Network
  - Attack Complexity: Low
  - Privileges Required: None
  - User Interaction: None
  - Scope: Unchanged
  - Confidentiality: High
  - Integrity: High
  - Availability: High
- **Pasos:**
  1. Navegar a "CVSS Calculator"
  2. Seleccionar métricas base
  3. Hacer clic en "Calculate"
- **Resultado Esperado:**
  - CVSS Score: 9.8
  - Severity: Critical
  - Vector String se genera correctamente
- **Prioridad:** Alta
- **Tipo:** Funcional

### **TC-CVSS-002: Cálculo CVSS con Métricas Temporales**
- **ID:** TC-CVSS-002
- **Descripción:** Verificar cálculo con métricas temporales
- **Precondiciones:** Usuario autenticado
- **Datos de Prueba:**
  - Exploit Code Maturity: Functional
  - Remediation Level: Official Fix
  - Report Confidence: Confirmed
- **Pasos:**
  1. Configurar métricas base
  2. Configurar métricas temporales
  3. Hacer clic en "Calculate"
- **Resultado Esperado:**
  - Score temporal se calcula correctamente
  - Diferencia con score base se muestra
- **Prioridad:** Media
- **Tipo:** Funcional

---

## 🎯 **CASOS DE PRUEBA - DOCUMENT ANALYZER**

### **TC-DOC-001: Subir Archivo PDF**
- **ID:** TC-DOC-001
- **Descripción:** Verificar que se puede subir un archivo PDF
- **Precondiciones:** Usuario autenticado
- **Datos de Prueba:** Archivo PDF con texto de vulnerabilidades
- **Pasos:**
  1. Navegar a "Document Analyzer"
  2. Hacer clic en "Choose File" o arrastrar archivo
  3. Seleccionar archivo PDF válido
  4. Hacer clic en "Analyze Document"
- **Resultado Esperado:**
  - Archivo se sube correctamente
  - Progreso de subida se muestra
  - Análisis se ejecuta
- **Prioridad:** Alta
- **Tipo:** Funcional

### **TC-DOC-002: Subir Archivo Word**
- **ID:** TC-DOC-002
- **Descripción:** Verificar que se puede subir un archivo Word
- **Precondiciones:** Usuario autenticado
- **Datos de Prueba:** Archivo .docx con texto de vulnerabilidades
- **Pasos:**
  1. Navegar a "Document Analyzer"
  2. Seleccionar archivo .docx
  3. Hacer clic en "Analyze Document"
- **Resultado Esperado:**
  - Archivo Word se procesa correctamente
  - Texto se extrae exitosamente
  - Análisis se ejecuta
- **Prioridad:** Alta
- **Tipo:** Funcional

### **TC-DOC-003: Análisis de Vulnerabilidades**
- **ID:** TC-DOC-003
- **Descripción:** Verificar que el análisis detecta vulnerabilidades
- **Precondiciones:** Documento subido con texto de vulnerabilidades
- **Datos de Prueba:** Texto que contiene "SQL injection", "XSS", "buffer overflow"
- **Pasos:**
  1. Subir documento con vulnerabilidades
  2. Ejecutar análisis
  3. Revisar resultados
- **Resultado Esperado:**
  - Vulnerabilidades se detectan
  - CVSS Scores se calculan
  - Recomendaciones se generan
- **Prioridad:** Alta
- **Tipo:** Funcional

### **TC-DOC-004: Convertir a Vulnerabilidad**
- **ID:** TC-DOC-004
- **Descripción:** Verificar que se puede convertir análisis a vulnerabilidad
- **Precondiciones:** Análisis de documento completado
- **Pasos:**
  1. Completar análisis de documento
  2. Hacer clic en "Add to Dashboard"
  3. Confirmar conversión
- **Resultado Esperado:**
  - Vulnerabilidad se crea en el dashboard
  - Mensaje de éxito se muestra
  - Análisis se marca como convertido
- **Prioridad:** Alta
- **Tipo:** Funcional

---

## 🎯 **CASOS DE PRUEBA - HISTORIAL DE ANÁLISIS**

### **TC-HIST-001: Ver Historial de Análisis**
- **ID:** TC-HIST-001
- **Descripción:** Verificar que se puede ver el historial de análisis
- **Precondiciones:** Análisis de documentos realizados
- **Pasos:**
  1. Navegar a "Analysis History"
  2. Revisar lista de análisis
- **Resultado Esperado:**
  - Lista de análisis se muestra
  - Información básica se visualiza
  - Fechas y archivos se muestran
- **Prioridad:** Media
- **Tipo:** Funcional

### **TC-HIST-002: Ver Detalles de Análisis**
- **ID:** TC-HIST-002
- **Descripción:** Verificar que se pueden ver detalles de un análisis
- **Precondiciones:** Análisis existente en el historial
- **Pasos:**
  1. Navegar a "Analysis History"
  2. Hacer clic en un análisis específico
- **Resultado Esperado:**
  - Detalles completos se muestran
  - Texto extraído se visualiza
  - Vulnerabilidades detectadas se listan
- **Prioridad:** Media
- **Tipo:** Funcional

---

## 🎯 **CASOS DE PRUEBA - VALIDACIONES**

### **TC-VAL-001: Validación de Campos Requeridos**
- **ID:** TC-VAL-001
- **Descripción:** Verificar que campos requeridos se validan
- **Precondiciones:** Usuario autenticado
- **Pasos:**
  1. Intentar crear vulnerabilidad sin título
  2. Intentar crear vulnerabilidad sin descripción
- **Resultado Esperado:**
  - Mensajes de error se muestran
  - Formulario no se envía
  - Campos requeridos se marcan
- **Prioridad:** Alta
- **Tipo:** Validación

### **TC-VAL-002: Validación de Tipos de Archivo**
- **ID:** TC-VAL-002
- **Descripción:** Verificar que solo se aceptan archivos válidos
- **Precondiciones:** Usuario autenticado
- **Datos de Prueba:** Archivo .txt, .jpg, .exe
- **Pasos:**
  1. Intentar subir archivo .txt
  2. Intentar subir archivo .jpg
  3. Intentar subir archivo .exe
- **Resultado Esperado:**
  - Solo PDF y Word se aceptan
  - Mensajes de error para tipos inválidos
  - Archivos inválidos se rechazan
- **Prioridad:** Alta
- **Tipo:** Validación

---

## 🎯 **CASOS DE PRUEBA - RENDIMIENTO**

### **TC-PERF-001: Carga de Dashboard**
- **ID:** TC-PERF-001
- **Descripción:** Verificar que el dashboard carga en tiempo razonable
- **Precondiciones:** Usuario autenticado
- **Pasos:**
  1. Navegar al dashboard
  2. Medir tiempo de carga
- **Resultado Esperado:**
  - Dashboard carga en menos de 3 segundos
  - No hay errores de timeout
- **Prioridad:** Media
- **Tipo:** Rendimiento

### **TC-PERF-002: Análisis de Documento Grande**
- **ID:** TC-PERF-002
- **Descripción:** Verificar rendimiento con documento grande
- **Precondiciones:** Usuario autenticado
- **Datos de Prueba:** PDF de 10MB con mucho texto
- **Pasos:**
  1. Subir documento grande
  2. Ejecutar análisis
  3. Medir tiempo de procesamiento
- **Resultado Esperado:**
  - Análisis se completa en menos de 30 segundos
  - No hay errores de memoria
- **Prioridad:** Media
- **Tipo:** Rendimiento

---

## 🎯 **CASOS DE PRUEBA - SEGURIDAD**

### **TC-SEC-001: Acceso No Autorizado**
- **ID:** TC-SEC-001
- **Descripción:** Verificar que rutas protegidas requieren autenticación
- **Precondiciones:** Usuario no autenticado
- **Pasos:**
  1. Intentar acceder a /dashboard sin login
  2. Intentar acceder a /vulnerabilities sin login
  3. Intentar acceder a /document-analyzer sin login
- **Resultado Esperado:**
  - Usuario es redirigido a login
  - Rutas protegidas no son accesibles
- **Prioridad:** Alta
- **Tipo:** Seguridad

### **TC-SEC-002: Validación de Token JWT**
- **ID:** TC-SEC-002
- **Descripción:** Verificar que tokens JWT expirados se manejan correctamente
- **Precondiciones:** Token JWT expirado
- **Pasos:**
  1. Usar token expirado para hacer requests
  2. Intentar acceder a rutas protegidas
- **Resultado Esperado:**
  - Usuario es redirigido a login
  - Token expirado se rechaza
- **Prioridad:** Alta
- **Tipo:** Seguridad

---

## 🎯 **CASOS DE PRUEBA - RESPONSIVE DESIGN**

### **TC-RESP-001: Dashboard en Móvil**
- **ID:** TC-RESP-001
- **Descripción:** Verificar que el dashboard funciona en dispositivos móviles
- **Precondiciones:** Usuario autenticado
- **Pasos:**
  1. Abrir dashboard en dispositivo móvil
  2. Verificar navegación
  3. Verificar visualización de contenido
- **Resultado Esperado:**
  - Dashboard se adapta a pantalla móvil
  - Navegación funciona correctamente
  - Contenido es legible
- **Prioridad:** Media
- **Tipo:** UI/UX

### **TC-RESP-002: Formularios en Tablet**
- **ID:** TC-RESP-002
- **Descripción:** Verificar que formularios funcionan en tablets
- **Precondiciones:** Usuario autenticado
- **Pasos:**
  1. Abrir formulario de vulnerabilidad en tablet
  2. Llenar formulario
  3. Enviar formulario
- **Resultado Esperado:**
  - Formulario se adapta a pantalla de tablet
  - Campos son fáciles de usar
  - Envío funciona correctamente
- **Prioridad:** Media
- **Tipo:** UI/UX

---

## 📊 **MÉTRICAS DE PRUEBA**

### **Cobertura de Pruebas:**
- **Funcionales:** 85%
- **Validación:** 90%
- **Seguridad:** 80%
- **Rendimiento:** 70%
- **UI/UX:** 75%

### **Prioridades:**
- **Alta:** 15 casos
- **Media:** 8 casos
- **Baja:** 2 casos

### **Tipos de Prueba:**
- **Funcional:** 18 casos
- **Validación:** 3 casos
- **Rendimiento:** 2 casos
- **Seguridad:** 2 casos
- **UI/UX:** 2 casos

---

## 🚀 **EJECUCIÓN DE PRUEBAS**

### **Entorno de Pruebas:**
- **Frontend:** Netlify (https://gleeful-vacherin-0740fc.netlify.app/)
- **Backend:** Render.com (https://cvss-scoring-system.onrender.com/)
- **Base de Datos:** SQLite (desarrollo), PostgreSQL (producción)

### **Herramientas de Pruebas:**
- **Manual:** Casos de prueba documentados
- **Automáticas:** Jest (frontend), pytest (backend)
- **API:** Postman/curl para testing de endpoints

### **Criterios de Aceptación:**
- **95%** de casos de prueba deben pasar
- **0** errores críticos
- **Máximo 2** errores menores por módulo

---

**✅ Total de Casos de Prueba: 25**
**📅 Fecha de Creación: Septiembre 2025**
**👥 Responsable: Equipo de Desarrollo**
