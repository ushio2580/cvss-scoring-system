# 🏗️ **ARQUITECTURA DEL SISTEMA - CVSS SCORING SYSTEM**

## 📋 **INFORMACIÓN GENERAL**
- **Proyecto:** CVSS Scoring System
- **Versión:** 1.0
- **Fecha:** Septiembre 2025
- **Arquitectura:** Híbrida (Monolítica + Microservicios)
- **Patrón:** MVC (Model-View-Controller)

---

## 🎯 **VISIÓN GENERAL DE LA ARQUITECTURA**

### **Arquitectura Híbrida:**
El sistema combina una **arquitectura monolítica** para el core del sistema con **componentes especializados** para funcionalidades específicas como el análisis de documentos.

```
                    CVSS SCORING SYSTEM
                           |
        ┌──────────────────┼──────────────────┐
        |                  |                  |
    🌐 FRONTEND        🔧 BACKEND         📊 DATABASE
        |                  |                  |
    React + Vite      Flask + Python      SQLite/PostgreSQL
        |                  |                  |
    ┌───▼───┐          ┌───▼───┐          ┌───▼───┐
    |       |          |       |          |       |
    | UI    |          | API   |          | Data  |
    | Layer |          | Layer |          | Layer |
    └───┬───┘          └───┬───┘          └───┬───┘
        |                  |                  |
    ┌───▼───┐          ┌───▼───┐              |
    |       |          |       |              |
    | State |          | Logic |              |
    | Mgmt  |          | Layer |              |
    └───┬───┘          └───┬───┘              |
        |                  |                  |
    ┌───▼───┐          ┌───▼───┐              |
    |       |          |       |              |
    | Auth  |          | CVSS  |              |
    | Layer |          | Calc  |              |
    └───────┘          └───┬───┘              |
                           |                  |
                    ┌──────▼──────┐           |
                    |             |           |
                    | Document    |           |
                    | Analyzer    |           |
                    └─────────────┘           |
```

---

## 🌐 **CAPA DE PRESENTACIÓN (FRONTEND)**

### **Tecnologías:**
- **Framework:** React 18.2.0
- **Build Tool:** Vite 4.4.5
- **Lenguaje:** TypeScript 5.0.2
- **Styling:** Tailwind CSS 3.3.3
- **UI Components:** shadcn/ui
- **State Management:** React Query + Context API
- **Routing:** React Router DOM 6.15.0

### **Estructura del Frontend:**
```
frontend/
├── src/
│   ├── components/          # Componentes reutilizables
│   │   ├── Dashboard/       # Componentes del dashboard
│   │   ├── DocumentAnalyzer.tsx
│   │   └── ...
│   ├── pages/              # Páginas principales
│   │   ├── Dashboard.tsx
│   │   ├── DocumentAnalyzer.tsx
│   │   └── DocumentAnalysisHistory.tsx
│   ├── hooks/              # Custom hooks
│   ├── utils/              # Utilidades
│   ├── config/             # Configuración
│   └── types/              # Tipos TypeScript
├── public/                 # Archivos estáticos
└── dist/                   # Build de producción
```

### **Patrones de Diseño:**
- **Component Pattern:** Componentes funcionales con hooks
- **Container/Presenter:** Separación de lógica y presentación
- **Custom Hooks:** Lógica reutilizable
- **Context API:** Estado global compartido

---

## 🔧 **CAPA DE LÓGICA DE NEGOCIO (BACKEND)**

### **Tecnologías:**
- **Framework:** Flask 2.3.2
- **Lenguaje:** Python 3.9+
- **ORM:** SQLAlchemy 2.0.19
- **Autenticación:** Flask-JWT-Extended 4.5.2
- **CORS:** Flask-CORS 4.0.0
- **Validación:** Marshmallow 3.20.1

### **Estructura del Backend:**
```
backend/
├── app/
│   ├── __init__.py         # Configuración de Flask
│   ├── models/             # Modelos de datos
│   │   ├── user.py
│   │   ├── vulnerability.py
│   │   └── document_analysis.py
│   ├── routes/             # Rutas de la API
│   │   ├── auth.py
│   │   ├── vulns.py
│   │   ├── document_analyzer.py
│   │   └── database_manager.py
│   ├── services/           # Lógica de negocio
│   │   ├── cvss_calculator.py
│   │   ├── document_processor.py
│   │   └── vulnerability_analyzer.py
│   └── utils/              # Utilidades
├── tests/                  # Pruebas
└── requirements.txt        # Dependencias
```

### **Patrones de Diseño:**
- **MVC Pattern:** Model-View-Controller
- **Repository Pattern:** Acceso a datos
- **Service Layer:** Lógica de negocio
- **Factory Pattern:** Creación de objetos

---

## 📊 **CAPA DE DATOS (DATABASE)**

### **Tecnologías:**
- **Desarrollo:** SQLite 3
- **Producción:** PostgreSQL 14+
- **ORM:** SQLAlchemy
- **Migraciones:** Flask-Migrate

### **Modelos de Datos:**

#### **User Model:**
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
```

#### **Vulnerability Model:**
```python
class Vulnerability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cvss_vector = db.Column(db.String(200), nullable=False)
    cvss_score = db.Column(db.Float, nullable=False)
    severity = db.Column(db.Enum(Severity), nullable=False)
    status = db.Column(db.Enum(Status), default=Status.NEW)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

#### **DocumentAnalysis Model:**
```python
class DocumentAnalysis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    file_size = db.Column(db.Integer, nullable=False)
    file_type = db.Column(db.String(50), nullable=False)
    extracted_text = db.Column(db.Text, nullable=False)
    vulnerability_types = db.Column(db.JSON, nullable=True)
    cvss_score = db.Column(db.Float, nullable=True)
    severity = db.Column(db.String(20), nullable=True)
    recommendations = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

---

## 🔄 **FLUJO DE DATOS DEL SISTEMA**

### **Flujo de Autenticación:**
```
Usuario → Frontend → Backend → Database
   |         |         |         |
   |    [Login Form]   |         |
   |         |         |         |
   |    [JWT Token]    |         |
   |         |         |         |
   |    [Store Token]  |         |
   |         |         |         |
   |    [API Calls]    |         |
   |         |         |         |
   |    [Protected Routes]      |
```

### **Flujo de Análisis de Documentos:**
```
Usuario → Frontend → Backend → Document Processor → Database
   |         |         |            |                |
   |    [Upload File]  |            |                |
   |         |         |            |                |
   |    [File Validation]           |                |
   |         |         |            |                |
   |    [Text Extraction]           |                |
   |         |         |            |                |
   |    [Vulnerability Analysis]    |                |
   |         |         |            |                |
   |    [CVSS Calculation]          |                |
   |         |         |            |                |
   |    [Save Results]              |                |
```

---

## 🏗️ **DIAGRAMA DE ARQUITECTURA DETALLADO**

### **Arquitectura de Componentes:**
```
                    ┌─────────────────────────────────────┐
                    │           USER INTERFACE            │
                    │         (React Frontend)            │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │         API GATEWAY                 │
                    │        (Flask Routes)               │
                    └─────────────────┬───────────────────┘
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
        ▼                             ▼                             ▼
┌───────────────┐           ┌───────────────┐           ┌───────────────┐
│   AUTH        │           │   VULNERABILITY│           │   DOCUMENT    │
│   SERVICE     │           │   SERVICE     │           │   ANALYZER    │
│               │           │               │           │   SERVICE     │
│ • Login       │           │ • CRUD        │           │ • File Upload │
│ • JWT         │           │ • CVSS Calc   │           │ • Text Extract│
│ • Validation  │           │ • Status Mgmt │           │ • Analysis    │
└───────┬───────┘           └───────┬───────┘           └───────┬───────┘
        │                         │                         │
        │                         │                         │
        ▼                         ▼                         ▼
┌───────────────┐           ┌───────────────┐           ┌───────────────┐
│   USER        │           │   VULNERABILITY│           │   DOCUMENT    │
│   MODEL       │           │   MODEL       │           │   ANALYSIS    │
│               │           │               │           │   MODEL       │
└───────┬───────┘           └───────┬───────┘           └───────┬───────┘
        │                         │                         │
        │                         │                         │
        └─────────────────────────┼─────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────────────┐
                    │           DATABASE                  │
                    │      (SQLite/PostgreSQL)           │
                    └─────────────────────────────────────┘
```

---

## 🔐 **ARQUITECTURA DE SEGURIDAD**

### **Capas de Seguridad:**
```
                    ┌─────────────────────────────────────┐
                    │         HTTPS/TLS                   │
                    │      (Transport Security)           │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │         JWT AUTHENTICATION          │
                    │        (Token-based Auth)           │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │         AUTHORIZATION               │
                    │        (Role-based Access)          │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │         INPUT VALIDATION            │
                    │        (Data Sanitization)          │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │         CORS POLICY                 │
                    │        (Cross-origin Control)       │
                    └─────────────────────────────────────┘
```

### **Componentes de Seguridad:**
- **HTTPS:** Todas las comunicaciones encriptadas
- **JWT:** Autenticación stateless con tokens
- **CORS:** Control de acceso cross-origin
- **Input Validation:** Validación de datos de entrada
- **SQL Injection Protection:** ORM con parámetros preparados
- **File Upload Security:** Validación de tipos y tamaños

---

## 📡 **ARQUITECTURA DE API**

### **RESTful API Design:**
```
Base URL: https://cvss-scoring-system.onrender.com/api

Authentication:
POST   /auth/login          # Login de usuario
POST   /auth/logout         # Logout de usuario
POST   /auth/refresh        # Refresh token

Vulnerabilities:
GET    /vulns               # Listar vulnerabilidades
POST   /vulns               # Crear vulnerabilidad
GET    /vulns/{id}          # Obtener vulnerabilidad
PUT    /vulns/{id}          # Actualizar vulnerabilidad
DELETE /vulns/{id}          # Eliminar vulnerabilidad

Document Analysis:
POST   /documents/analyze   # Analizar documento
GET    /documents/history   # Historial de análisis
GET    /documents/{id}      # Detalles de análisis

Database Management:
GET    /database/export     # Exportar base de datos
POST   /database/import     # Importar base de datos
```

### **Estructura de Respuestas:**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "title": "SQL Injection",
    "cvss_score": 9.8,
    "severity": "Critical"
  },
  "message": "Vulnerability created successfully",
  "timestamp": "2025-09-12T10:30:00Z"
}
```

---

## 🚀 **ARQUITECTURA DE DESPLIEGUE**

### **Entorno de Desarrollo:**
```
┌─────────────────────────────────────────────────────────┐
│                    DEVELOPMENT                          │
│                                                         │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │   Frontend  │    │   Backend   │    │   Database  │ │
│  │   (Vite)    │    │   (Flask)   │    │   (SQLite)  │ │
│  │   Port 3000 │    │   Port 5000 │    │   Local     │ │
│  └─────────────┘    └─────────────┘    └─────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### **Entorno de Producción:**
```
┌─────────────────────────────────────────────────────────┐
│                    PRODUCTION                           │
│                                                         │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │   Frontend  │    │   Backend   │    │   Database  │ │
│  │   (Netlify) │    │ (Render.com)│    │(PostgreSQL) │ │
│  │   HTTPS     │    │   HTTPS     │    │   Cloud     │ │
│  └─────────────┘    └─────────────┘    └─────────────┘ │
└─────────────────────────────────────────────────────────┘
```

### **Servicios Externos:**
- **Frontend:** Netlify (CDN, HTTPS, CI/CD)
- **Backend:** Render.com (Auto-deploy, HTTPS, Load Balancing)
- **Database:** PostgreSQL (Render.com managed)
- **File Storage:** Local storage (temporal)

---

## 🔄 **PATRONES DE ARQUITECTURA**

### **1. Model-View-Controller (MVC):**
- **Model:** SQLAlchemy models (User, Vulnerability, DocumentAnalysis)
- **View:** React components (Dashboard, DocumentAnalyzer, etc.)
- **Controller:** Flask routes (auth.py, vulns.py, document_analyzer.py)

### **2. Repository Pattern:**
```python
class VulnerabilityRepository:
    def create(self, data):
        vulnerability = Vulnerability(**data)
        db.session.add(vulnerability)
        db.session.commit()
        return vulnerability
    
    def get_by_id(self, id):
        return Vulnerability.query.get(id)
    
    def get_all(self):
        return Vulnerability.query.all()
```

### **3. Service Layer Pattern:**
```python
class CVSSService:
    def calculate_score(self, metrics):
        calculator = CVSSCalculator()
        return calculator.calculate(metrics)
    
    def validate_metrics(self, metrics):
        validator = MetricsValidator()
        return validator.validate(metrics)
```

### **4. Factory Pattern:**
```python
class DocumentProcessorFactory:
    @staticmethod
    def create_processor(file_type):
        if file_type == 'pdf':
            return PDFProcessor()
        elif file_type == 'docx':
            return WordProcessor()
        else:
            raise ValueError(f"Unsupported file type: {file_type}")
```

---

## 📊 **MÉTRICAS DE ARQUITECTURA**

### **Rendimiento:**
- **Tiempo de respuesta API:** < 200ms
- **Tiempo de carga frontend:** < 3 segundos
- **Throughput:** 100 requests/segundo
- **Latencia de base de datos:** < 50ms

### **Escalabilidad:**
- **Usuarios concurrentes:** 1000+
- **Documentos procesados:** 1000/día
- **Vulnerabilidades:** 10,000+
- **Almacenamiento:** 100GB+

### **Disponibilidad:**
- **Uptime:** 99.5%
- **MTTR:** < 5 minutos
- **Backup:** Diario
- **Recovery:** < 1 hora

---

## 🔧 **HERRAMIENTAS DE DESARROLLO**

### **Frontend:**
- **Build:** Vite
- **Linting:** ESLint
- **Formatting:** Prettier
- **Testing:** Jest + React Testing Library
- **Type Checking:** TypeScript

### **Backend:**
- **Testing:** pytest
- **Linting:** flake8
- **Formatting:** black
- **Type Checking:** mypy
- **API Documentation:** Swagger/OpenAPI

### **DevOps:**
- **Version Control:** Git
- **CI/CD:** GitHub Actions
- **Deployment:** Netlify + Render.com
- **Monitoring:** Logs + Metrics
- **Backup:** Automated daily

---

## 🎯 **PRINCIPIOS DE ARQUITECTURA**

### **1. Separation of Concerns:**
- Frontend: Presentación y interacción
- Backend: Lógica de negocio y API
- Database: Almacenamiento de datos

### **2. Single Responsibility:**
- Cada módulo tiene una responsabilidad específica
- Servicios especializados (CVSS, Document Analysis)
- Componentes reutilizables

### **3. DRY (Don't Repeat Yourself):**
- Utilidades compartidas
- Componentes reutilizables
- Servicios comunes

### **4. SOLID Principles:**
- **S:** Single Responsibility
- **O:** Open/Closed
- **L:** Liskov Substitution
- **I:** Interface Segregation
- **D:** Dependency Inversion

---

## 🚀 **EVOLUCIÓN DE LA ARQUITECTURA**

### **Fase 1 (Actual):** Monolítica
- Sistema integrado
- Base de datos única
- Despliegue simple

### **Fase 2 (Futuro):** Microservicios
- Servicios independientes
- Bases de datos especializadas
- API Gateway
- Message Queue

### **Fase 3 (Escalado):** Cloud Native
- Kubernetes
- Service Mesh
- Event-driven Architecture
- Multi-region deployment

---

**✅ Arquitectura del Sistema Documentada**
**📅 Fecha de Creación: Septiembre 2025**
**👥 Responsable: Equipo de Desarrollo**
