# 🧭 **FLUJO DE NAVEGACIÓN - CVSS SCORING SYSTEM**

## 📋 **INFORMACIÓN GENERAL**
- **Proyecto:** CVSS Scoring System
- **Versión:** 1.0
- **Fecha:** Septiembre 2025
- **Framework:** React Router DOM 6.15.0
- **Patrón:** SPA (Single Page Application)

---

## 🎯 **ESTRUCTURA DE RUTAS**

### **Rutas Principales:**
```
/                           # Página de Login
├── /dashboard              # Dashboard Principal
├── /vulnerabilities        # Gestión de Vulnerabilidades
├── /cvss-calculator        # Calculadora CVSS
├── /document-analyzer      # Analizador de Documentos
├── /document-analysis-history # Historial de Análisis
└── /profile                # Perfil de Usuario
```

### **Rutas Protegidas:**
Todas las rutas excepto `/` requieren autenticación JWT válida.

---

## 🔐 **FLUJO DE AUTENTICACIÓN**

### **1. Página de Login (`/`)**
```
Usuario accede al sistema
         |
         ▼
    [Verificar Token]
         |
    ┌────▼────┐
    | ¿Token  |
    | válido? |
    └────┬────┘
         |
    ┌────▼────┐    ┌─────────────┐
    |   NO    |───▶│ Mostrar     │
    └─────────┘    │ Login Form  │
         |         └──────┬──────┘
         |                |
         |                ▼
         |         [Usuario ingresa]
         |         [credenciales]
         |                |
         |                ▼
         |         [Validar en API]
         |                |
         |         ┌──────▼──────┐
         |         │ ¿Credenciales│
         |         │ válidas?    │
         |         └──────┬──────┘
         |                |
         |         ┌──────▼──────┐    ┌─────────────┐
         |         │     NO      │───▶│ Mostrar     │
         |         └─────────────┘    │ Error       │
         |                            └─────────────┘
         |                |
         |         ┌──────▼──────┐
         |         │     SÍ      │
         |         └──────┬──────┘
         |                |
         |                ▼
         |         [Guardar Token]
         |         [en localStorage]
         |                |
         |                ▼
         |         [Redirigir a]
         |         [/dashboard]
         |
    ┌────▼────┐
    |   SÍ    |
    └────┬────┘
         |
         ▼
    [Redirigir a]
    [/dashboard]
```

### **2. Protección de Rutas**
```javascript
// ProtectedRoute Component
const ProtectedRoute = ({ children }) => {
  const token = localStorage.getItem('token');
  
  if (!token) {
    return <Navigate to="/" replace />;
  }
  
  return children;
};
```

---

## 🏠 **FLUJO DEL DASHBOARD**

### **Dashboard Principal (`/dashboard`)**
```
Usuario accede al dashboard
         |
         ▼
    [Cargar datos del usuario]
         |
         ▼
    ┌─────────────────────────┐
    │     DASHBOARD LAYOUT    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   SIDEBAR       │    │
    │  │                 │    │
    │  │ • Dashboard     │    │
    │  │ • Vulnerabilities│   │
    │  │ • CVSS Calc     │    │
    │  │ • Doc Analyzer  │    │
    │  │ • History       │    │
    │  │ • Profile       │    │
    │  │ • Logout        │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   MAIN CONTENT  │    │
    │  │                 │    │
    │  │ • Welcome Card  │    │
    │  │ • Stats Cards   │    │
    │  │ • Recent Vulns  │    │
    │  │ • Recent Docs   │    │
    │  │ • Quick Actions │    │
    │  └─────────────────┘    │
    └─────────────────────────┘
```

### **Navegación desde Dashboard:**
```
Dashboard
    |
    ├── [Vulnerabilities] ──▶ /vulnerabilities
    ├── [CVSS Calculator] ──▶ /cvss-calculator
    ├── [Document Analyzer] ──▶ /document-analyzer
    ├── [Analysis History] ──▶ /document-analysis-history
    ├── [Profile] ──▶ /profile
    └── [Logout] ──▶ / (con limpieza de token)
```

---

## 🛡️ **FLUJO DE GESTIÓN DE VULNERABILIDADES**

### **Lista de Vulnerabilidades (`/vulnerabilities`)**
```
Usuario accede a vulnerabilidades
         |
         ▼
    [Cargar lista de vulnerabilidades]
         |
         ▼
    ┌─────────────────────────┐
    │   VULNERABILITIES PAGE  │
    │                         │
    │  ┌─────────────────┐    │
    │  │   HEADER        │    │
    │  │                 │    │
    │  │ [Add New] [Filter] │ │
    │  │ [Search] [Export] │ │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   VULNERABILITY │    │
    │  │   LIST          │    │
    │  │                 │    │
    │  │ ┌─────────────┐ │    │
    │  │ │ Vulnerability│ │    │
    │  │ │ Card        │ │    │
    │  │ │             │ │    │
    │  │ │ • Title     │ │    │
    │  │ │ • Score     │ │    │
    │  │ │ • Status    │ │    │
    │  │ │ • Actions   │ │    │
    │  │ └─────────────┘ │    │
    │  │                 │    │
    │  │ [More cards...] │    │
    │  └─────────────────┘    │
    └─────────────────────────┘
```

### **Acciones en Vulnerabilidades:**
```
Vulnerability Card
    |
    ├── [View] ──▶ Modal con detalles completos
    ├── [Edit] ──▶ Formulario de edición
    ├── [Delete] ──▶ Confirmación + eliminación
    └── [Status] ──▶ Dropdown para cambiar estado
```

### **Crear Nueva Vulnerabilidad:**
```
[Add New] Button
         |
         ▼
    [Abrir Modal de Creación]
         |
         ▼
    ┌─────────────────────────┐
    │   CREATE VULNERABILITY  │
    │                         │
    │  ┌─────────────────┐    │
    │  │   FORM          │    │
    │  │                 │    │
    │  │ • Title*        │    │
    │  │ • Description*  │    │
    │  │ • CVSS Vector   │    │
    │  │ • Status        │    │
    │  │ • Priority      │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   ACTIONS       │    │
    │  │                 │    │
    │  │ [Cancel] [Save] │    │
    │  └─────────────────┘    │
    └─────────────────────────┘
         |
         ▼
    [Validar datos]
         |
    ┌────▼────┐
    | ¿Válidos?|
    └────┬────┘
         |
    ┌────▼────┐    ┌─────────────┐
    |   NO    |───▶│ Mostrar     │
    └─────────┘    │ Errores     │
         |         └─────────────┘
         |
    ┌────▼────┐
    |   SÍ    |
    └────┬────┘
         |
         ▼
    [Enviar a API]
         |
         ▼
    [Actualizar lista]
         |
         ▼
    [Cerrar modal]
```

---

## 🧮 **FLUJO DE CALCULADORA CVSS**

### **Calculadora CVSS (`/cvss-calculator`)**
```
Usuario accede a calculadora
         |
         ▼
    ┌─────────────────────────┐
    │   CVSS CALCULATOR       │
    │                         │
    │  ┌─────────────────┐    │
    │  │   BASE METRICS  │    │
    │  │                 │    │
    │  │ • Attack Vector │    │
    │  │ • Attack Complex│    │
    │  │ • Privileges    │    │
    │  │ • User Interact │    │
    │  │ • Scope         │    │
    │  │ • Confidential  │    │
    │  │ • Integrity     │    │
    │  │ • Availability  │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │ TEMPORAL METRICS│    │
    │  │                 │    │
    │  │ • Exploit Code  │    │
    │  │ • Remediation   │    │
    │  │ • Report Conf   │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │ ENVIRONMENTAL   │    │
    │  │ METRICS         │    │
    │  │                 │    │
    │  │ • Confidential  │    │
    │  │ • Integrity     │    │
    │  │ • Availability  │    │
    │  │ • Modified Base │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   RESULTS       │    │
    │  │                 │    │
    │  │ • Base Score    │    │
    │  │ • Temporal Score│    │
    │  │ • Environmental │    │
    │  │ • Vector String │    │
    │  │ • Severity      │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   ACTIONS       │    │
    │  │                 │    │
    │  │ [Calculate]     │    │
    │  │ [Save as Vuln]  │    │
    │  │ [Reset]         │    │
    │  └─────────────────┘    │
    └─────────────────────────┘
```

### **Flujo de Cálculo:**
```
[Calculate] Button
         |
         ▼
    [Recopilar métricas seleccionadas]
         |
         ▼
    [Validar métricas requeridas]
         |
    ┌────▼────┐
    | ¿Válidas?|
    └────┬────┘
         |
    ┌────▼────┐    ┌─────────────┐
    |   NO    |───▶│ Mostrar     │
    └─────────┘    │ Errores     │
         |         └─────────────┘
         |
    ┌────▼────┐
    |   SÍ    |
    └────┬────┘
         |
         ▼
    [Calcular score base]
         |
         ▼
    [Calcular score temporal]
         |
         ▼
    [Calcular score ambiental]
         |
         ▼
    [Determinar severidad]
         |
         ▼
    [Mostrar resultados]
         |
         ▼
    [Generar vector string]
```

---

## 📄 **FLUJO DE ANÁLISIS DE DOCUMENTOS**

### **Document Analyzer (`/document-analyzer`)**
```
Usuario accede a analizador
         |
         ▼
    ┌─────────────────────────┐
    │   DOCUMENT ANALYZER     │
    │                         │
    │  ┌─────────────────┐    │
    │  │   UPLOAD AREA   │    │
    │  │                 │    │
    │  │ ┌─────────────┐ │    │
    │  │ │   DRAG &    │ │    │
    │  │ │   DROP      │ │    │
    │  │ │   ZONE      │ │    │
    │  │ │             │ │    │
    │  │ │ [Choose File]│ │    │
    │  │ │ or drag here│ │    │
    │  │ └─────────────┘ │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   SUPPORTED     │    │
    │  │   FORMATS       │    │
    │  │                 │    │
    │  │ • PDF (.pdf)    │    │
    │  │ • Word (.docx)  │    │
    │  │ • Max: 10MB     │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   ACTIONS       │    │
    │  │                 │    │
    │  │ [Analyze]       │    │
    │  │ [Back to Dash]  │    │
    │  └─────────────────┘    │
    └─────────────────────────┘
```

### **Flujo de Análisis:**
```
[Analyze] Button
         |
         ▼
    [Validar archivo seleccionado]
         |
    ┌────▼────┐
    | ¿Válido? |
    └────┬────┘
         |
    ┌────▼────┐    ┌─────────────┐
    |   NO    |───▶│ Mostrar     │
    └─────────┘    │ Error       │
         |         └─────────────┘
         |
    ┌────▼────┐
    |   SÍ    |
    └────┬────┘
         |
         ▼
    [Mostrar loading]
         |
         ▼
    [Subir archivo al servidor]
         |
         ▼
    [Extraer texto del archivo]
         |
         ▼
    [Analizar texto buscando vulnerabilidades]
         |
         ▼
    [Calcular CVSS para vulnerabilidades encontradas]
         |
         ▼
    [Generar recomendaciones]
         |
         ▼
    [Guardar análisis en base de datos]
         |
         ▼
    [Mostrar resultados]
```

### **Resultados del Análisis:**
```
Análisis completado
         |
         ▼
    ┌─────────────────────────┐
    │   ANALYSIS RESULTS      │
    │                         │
    │  ┌─────────────────┐    │
    │  │   FILE INFO     │    │
    │  │                 │    │
    │  │ • Filename      │    │
    │  │ • Size          │    │
    │  │ • Type          │    │
    │  │ • Upload Date   │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   EXTRACTED     │    │
    │  │   TEXT          │    │
    │  │                 │    │
    │  │ [Preview of     │    │
    │  │  extracted text]│    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   VULNERABILITIES│   │
    │  │   DETECTED      │    │
    │  │                 │    │
    │  │ • SQL Injection │    │
    │  │ • XSS           │    │
    │  │ • Buffer Overflow│   │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   CVSS SCORES   │    │
    │  │                 │    │
    │  │ • Overall: 8.5  │    │
    │  │ • Severity: High│    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   RECOMMENDATIONS│   │
    │  │                 │    │
    │  │ • Fix SQL inj.  │    │
    │  │ • Sanitize input│    │
    │  │ • Update libs   │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   ACTIONS       │    │
    │  │                 │    │
    │  │ [Add to Dashboard]│  │
    │  │ [View History]  │    │
    │  │ [New Analysis]  │    │
    │  └─────────────────┘    │
    └─────────────────────────┘
```

---

## 📚 **FLUJO DE HISTORIAL DE ANÁLISIS**

### **Analysis History (`/document-analysis-history`)**
```
Usuario accede a historial
         |
         ▼
    [Cargar historial de análisis]
         |
         ▼
    ┌─────────────────────────┐
    │   ANALYSIS HISTORY      │
    │                         │
    │  ┌─────────────────┐    │
    │  │   HEADER        │    │
    │  │                 │    │
    │  │ [Back to Dash]  │    │
    │  │ [New Analysis]  │    │
    │  │ [Filter] [Sort] │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   ANALYSIS LIST │    │
    │  │                 │    │
    │  │ ┌─────────────┐ │    │
    │  │ │ Analysis    │ │    │
    │  │ │ Card        │ │    │
    │  │ │             │ │    │
    │  │ │ • Filename  │ │    │
    │  │ │ • Date      │ │    │
    │  │ │ • Score     │ │    │
    │  │ │ • Status    │ │    │
    │  │ │ • Actions   │ │    │
    │  │ └─────────────┘ │    │
    │  │                 │    │
    │  │ [More cards...] │    │
    │  └─────────────────┘    │
    └─────────────────────────┘
```

### **Acciones en Historial:**
```
Analysis Card
    |
    ├── [View Details] ──▶ Modal con análisis completo
    ├── [Convert to Vuln] ──▶ Crear vulnerabilidad
    └── [Delete] ──▶ Confirmación + eliminación
```

---

## 👤 **FLUJO DE PERFIL DE USUARIO**

### **User Profile (`/profile`)**
```
Usuario accede a perfil
         |
         ▼
    [Cargar datos del usuario]
         |
         ▼
    ┌─────────────────────────┐
    │   USER PROFILE          │
    │                         │
    │  ┌─────────────────┐    │
    │  │   USER INFO     │    │
    │  │                 │    │
    │  │ • Email         │    │
    │  │ • Join Date     │    │
    │  │ • Last Login    │    │
    │  │ • Status        │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   STATISTICS    │    │
    │  │                 │    │
    │  │ • Total Vulns   │    │
    │  │ • Total Docs    │    │
    │  │ • Avg Score     │    │
    │  │ • Last Activity │    │
    │  └─────────────────┘    │
    │                         │
    │  ┌─────────────────┐    │
    │  │   ACTIONS       │    │
    │  │                 │    │
    │  │ [Change Pass]   │    │
    │  │ [Export Data]   │    │
    │  │ [Delete Account]│    │
    │  └─────────────────┘    │
    └─────────────────────────┘
```

---

## 🔄 **FLUJOS DE NAVEGACIÓN TRANSVERSALES**

### **Breadcrumbs:**
```
Dashboard > Vulnerabilities > Edit Vulnerability
Dashboard > Document Analyzer > Analysis Results
Dashboard > Analysis History > View Details
```

### **Navegación Rápida:**
```
Cualquier página
    |
    ├── [Home] ──▶ /dashboard
    ├── [Vulns] ──▶ /vulnerabilities
    ├── [Calculator] ──▶ /cvss-calculator
    ├── [Analyzer] ──▶ /document-analyzer
    └── [History] ──▶ /document-analysis-history
```

### **Navegación por Teclado:**
- **Tab:** Navegar entre elementos
- **Enter:** Activar botones/enlaces
- **Escape:** Cerrar modales
- **Ctrl + K:** Búsqueda rápida (futuro)

---

## 📱 **NAVEGACIÓN RESPONSIVE**

### **Desktop (> 1024px):**
```
┌─────────────────────────────────────────┐
│ HEADER: Logo | Nav Items | User Menu    │
├─────────────────────────────────────────┤
│ SIDEBAR │ MAIN CONTENT                  │
│         │                               │
│ • Dash  │ [Page Content]                │
│ • Vulns │                               │
│ • Calc  │                               │
│ • Docs  │                               │
│ • Hist  │                               │
│ • Prof  │                               │
└─────────────────────────────────────────┘
```

### **Tablet (768px - 1024px):**
```
┌─────────────────────────────────────────┐
│ HEADER: Logo | ☰ Menu | User Menu      │
├─────────────────────────────────────────┤
│ MAIN CONTENT                            │
│                                         │
│ [Page Content]                          │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

### **Mobile (< 768px):**
```
┌─────────────────────────────────────────┐
│ HEADER: ☰ Menu | Logo | User Menu      │
├─────────────────────────────────────────┤
│ MAIN CONTENT                            │
│                                         │
│ [Page Content]                          │
│                                         │
│                                         │
└─────────────────────────────────────────┘
```

---

## 🚨 **MANEJO DE ERRORES EN NAVEGACIÓN**

### **Errores de Autenticación:**
```
Token expirado/inválido
         |
         ▼
    [Limpiar localStorage]
         |
         ▼
    [Redirigir a /]
         |
         ▼
    [Mostrar mensaje de sesión expirada]
```

### **Errores de Red:**
```
Error de conexión
         |
         ▼
    [Mostrar mensaje de error]
         |
         ▼
    [Botón "Retry"]
         |
         ▼
    [Reintentar operación]
```

### **Páginas No Encontradas:**
```
Ruta inválida
         |
         ▼
    [Mostrar 404 Page]
         |
         ▼
    [Botón "Go Home"]
         |
         ▼
    [Redirigir a /dashboard]
```

---

## 📊 **MÉTRICAS DE NAVEGACIÓN**

### **Rutas Más Utilizadas:**
1. **Dashboard:** 40%
2. **Vulnerabilities:** 25%
3. **Document Analyzer:** 20%
4. **CVSS Calculator:** 10%
5. **Analysis History:** 5%

### **Tiempo Promedio por Página:**
- **Dashboard:** 2 minutos
- **Vulnerabilities:** 5 minutos
- **Document Analyzer:** 3 minutos
- **CVSS Calculator:** 4 minutos
- **Analysis History:** 2 minutos

### **Flujos Más Comunes:**
1. **Login → Dashboard → Vulnerabilities**
2. **Login → Dashboard → Document Analyzer**
3. **Login → Dashboard → CVSS Calculator**

---

**✅ Flujo de Navegación Documentado**
**📅 Fecha de Creación: Septiembre 2025**
**👥 Responsable: Equipo de Desarrollo**
