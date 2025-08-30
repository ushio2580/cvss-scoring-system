# 🚀 Sistema de Scoring CVSS

Sistema web completo para evaluación de vulnerabilidades usando CVSS v3.1, con dashboard interactivo, exportes profesionales, auditoría detallada y gestión de base de datos.

## 🎯 Características

- **Dashboard Interactivo** con KPIs y gráficos en tiempo real
- **Sistema de Evaluaciones CVSS** con seguimiento temporal
- **Exportes Profesionales** (CSV/PDF) con gráficos y diseño avanzado
- **Historial de cambios** de vulnerabilidades
- **Carga masiva** de vulnerabilidades (CSV/JSON)
- **Sistema de Auditoría** con logs detallados
- **Database Manager** para administradores
- **Calculadora CVSS** interactiva
- **Autenticación JWT** con roles (Admin/Analyst/Viewer)
- **API REST** completa

## 🏗️ Estructura del Proyecto

```
PyFlask/
├── backend/
│   ├── app/
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── vulnerability.py
│   │   │   ├── evaluation.py
│   │   │   ├── audit_log.py
│   │   │   └── vulnerability_history.py
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── vulns.py
│   │   │   ├── dashboard.py
│   │   │   ├── exports.py
│   │   │   ├── bulk_upload.py
│   │   │   ├── audit_logs.py
│   │   │   ├── database_manager.py
│   │   │   └── evaluations.py
│   │   ├── services/
│   │   │   ├── cvss_service.py
│   │   │   └── report_generator.py
│   │   └── utils/
│   │       └── authorization.py
│   ├── requirements.txt
│   └── run.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── VulnerabilityList.tsx
│   │   │   ├── VulnerabilityEvaluations.tsx
│   │   │   ├── CreateEvaluationModal.tsx
│   │   │   ├── EditEvaluationModal.tsx
│   │   │   ├── BulkUploadModal.tsx
│   │   │   ├── AuditLogs.tsx
│   │   │   ├── DatabaseManager.tsx
│   │   │   └── CVSSCalculator.tsx
│   │   ├── pages/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Vulnerabilities.tsx
│   │   │   ├── AuditLogs.tsx
│   │   │   └── DatabaseManager.tsx
│   │   ├── services/
│   │   │   └── api.ts
│   │   └── types/
│   │       └── index.ts
│   ├── package.json
│   └── vite.config.ts
├── Procfile
├── runtime.txt
└── README.md
```

## 🚀 Dashboard Features

- **KPIs en tiempo real** (Total vulnerabilidades, Críticas, Evaluaciones)
- **Gráficos interactivos** (Distribución por severidad, Tendencia temporal)
- **Exportes Profesionales** con gráficos y diseño avanzado
- **Sistema de Evaluaciones CVSS** con seguimiento temporal
- **Auditoría y Logs** detallados
- **Database Manager** para administradores

## 🔧 Funcionalidades Avanzadas

### Sistema de Evaluaciones CVSS
- Múltiples evaluaciones por vulnerabilidad
- Seguimiento temporal de cambios de severidad
- Calculadora CVSS interactiva
- Métricas base, temporales y ambientales

### Auditoría y Logs
- Registro detallado de todas las acciones
- Historial de cambios de vulnerabilidades
- Exportes de logs (CSV/PDF)
- Filtros y búsqueda avanzada

### Database Manager
- Vista de estructura de tablas
- Consultas SQL personalizadas
- Exportes de datos
- Gestión de usuarios
- Solo para roles Admin/DB Manager

### Reportes Profesionales
- Diseño avanzado con gráficos
- Información detallada y estadísticas
- Exportes en PDF y CSV
- Personalización de contenido

## 🚀 Uso del Sistema

### Crear una Vulnerabilidad
1. Ve a "Vulnerabilities" → "Add Vulnerability"
2. Completa: Título, Descripción, CVE ID, Estado
3. Guarda la vulnerabilidad

### Evaluar una Vulnerabilidad
1. En la lista de vulnerabilidades, haz clic en "Evaluations"
2. Haz clic en "Add Evaluation"
3. Usa la calculadora CVSS o ingresa un vector manualmente
4. Completa las métricas base, temporales y ambientales
5. Guarda la evaluación

### Seguimiento Temporal
1. Crea múltiples evaluaciones para la misma vulnerabilidad
2. Observa cómo cambia la severidad a lo largo del tiempo
3. Usa el dashboard para ver tendencias

### Generar Reportes
1. Ve al Dashboard
2. Haz clic en "Export CSV" o "Export PDF"
3. Selecciona las opciones de filtrado
4. Descarga el reporte profesional

## 🌐 Despliegue en Heroku

### Paso 1: Preparar el Proyecto
```bash
# Instalar dependencias
npm run install-all

# Construir el frontend
npm run build-frontend
```

### Paso 2: Crear Cuenta en Heroku
1. Ve a [heroku.com](https://heroku.com)
2. Crea una cuenta gratuita
3. Instala Heroku CLI

### Paso 3: Desplegar
```bash
# Login a Heroku
heroku login

# Crear aplicación
heroku create tu-app-cvss

# Agregar base de datos PostgreSQL
heroku addons:create heroku-postgresql:mini

# Configurar variables de entorno
heroku config:set SECRET_KEY="tu-secret-key-super-seguro"
heroku config:set JWT_SECRET_KEY="tu-jwt-secret-key-super-seguro"

# Desplegar
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# Ejecutar migraciones
heroku run python -c "from app import create_app; app = create_app(); app.app_context().push(); from app import db; db.create_all()"
```

### Paso 4: Configurar Frontend
1. Ve a [vercel.com](https://vercel.com)
2. Conecta tu repositorio de GitHub
3. Configura las variables de entorno:
   - `VITE_API_URL`: `https://tu-app-cvss.herokuapp.com`
4. Despliega

### Credenciales por Defecto
- **Email:** admin@cvss.com
- **Password:** admin123
- **Rol:** Admin

## 🛠️ Instalación Local

### Requisitos
- Python 3.10+
- Node.js 18+
- pip
- npm

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Acceso
- **Backend:** http://localhost:5000
- **Frontend:** http://localhost:3001
- **Credenciales:** admin@cvss.com / admin123

## 📊 Tecnologías

### Backend
- **Python 3.10** - Lenguaje principal
- **Flask** - Framework web
- **SQLAlchemy** - ORM para base de datos
- **Flask-JWT-Extended** - Autenticación JWT
- **Pandas** - Manipulación de datos
- **ReportLab** - Generación de PDFs
- **Matplotlib/Seaborn** - Gráficos para reportes

### Frontend
- **React 18** - Framework de UI
- **TypeScript** - Tipado estático
- **Vite** - Build tool
- **Tailwind CSS** - Framework CSS
- **shadcn/ui** - Componentes UI
- **TanStack Query** - Gestión de estado
- **Recharts** - Gráficos interactivos
- **Framer Motion** - Animaciones

### Base de Datos
- **SQLite** (desarrollo)
- **PostgreSQL** (producción)

## 🔐 Autenticación y Autorización

### Roles de Usuario
- **Admin:** Acceso completo, Database Manager
- **Analyst:** Crear/editar vulnerabilidades y evaluaciones
- **Viewer:** Solo lectura

### Endpoints Protegidos
- `/api/vulns/*` - Requiere autenticación
- `/api/dashboard/*` - Requiere autenticación
- `/api/exports/*` - Requiere autenticación
- `/api/database-manager/*` - Solo Admin/DB Manager

## 📈 Métricas y KPIs

### Dashboard Principal
- Total de vulnerabilidades
- Vulnerabilidades críticas
- Evaluaciones realizadas
- Distribución por severidad
- Tendencia temporal

### Reportes
- Vulnerabilidades por estado
- Evaluaciones por período
- Actividad de usuarios
- Logs de auditoría

## 🔧 Configuración Avanzada

### Variables de Entorno
```bash
# Backend
SECRET_KEY=tu-secret-key
JWT_SECRET_KEY=tu-jwt-secret
DATABASE_URL=postgresql://...

# Frontend
VITE_API_URL=https://tu-backend-url.com
```

### Personalización
- Modificar estilos en `frontend/src/index.css`
- Agregar nuevos endpoints en `backend/app/routes/`
- Personalizar reportes en `backend/app/services/report_generator.py`

## 🧪 Testing

### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm test
```

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📞 Soporte

Para soporte técnico o preguntas:
- Crear un issue en GitHub
- Contactar al equipo de desarrollo

---

**¡Sistema de Scoring CVSS - Evaluación profesional de vulnerabilidades!** 🛡️

