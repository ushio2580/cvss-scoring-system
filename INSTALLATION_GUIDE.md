# 🚀 Guía de Instalación Completa - CVSS Scoring System

## 📋 **Requisitos del Sistema**

### **Requisitos Mínimos**
- **Python**: 3.10 o superior
- **Node.js**: 18.0 o superior
- **npm**: 9.0 o superior
- **Git**: Para clonar el repositorio
- **Memoria RAM**: 4GB mínimo (8GB recomendado)
- **Espacio en disco**: 2GB libres

### **Sistemas Operativos Soportados**
- ✅ **Windows** 10/11
- ✅ **macOS** 10.15+
- ✅ **Linux** (Ubuntu 20.04+, CentOS 8+, Debian 11+)
- ✅ **WSL2** (Windows Subsystem for Linux)

## 🛠️ **Instalación Paso a Paso**

### **Paso 1: Clonar el Repositorio**
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/PyFlask-clean.git
cd PyFlask-clean

# Verificar la estructura del proyecto
ls -la
```

### **Paso 2: Configurar el Backend**

#### **2.1 Crear Entorno Virtual**
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
```

#### **2.2 Instalar Dependencias del Backend**
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt
```

#### **2.3 Configurar Variables de Entorno**
```bash
# Crear archivo .env en la carpeta backend
touch .env  # En Windows: type nul > .env

# Agregar las siguientes variables:
echo "SECRET_KEY=tu-secret-key-super-seguro-aqui" >> .env
echo "JWT_SECRET_KEY=tu-jwt-secret-key-super-seguro-aqui" >> .env
echo "DATABASE_URL=sqlite:///instance/cvss.db" >> .env
echo "FLASK_ENV=development" >> .env
```

#### **2.4 Inicializar Base de Datos**
```bash
# Crear directorio instance si no existe
mkdir -p instance

# Inicializar base de datos
python -c "
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
    print('Base de datos inicializada correctamente')
"
```

#### **2.5 Verificar Instalación del Backend**
```bash
# Ejecutar el servidor de desarrollo
python run.py

# Deberías ver:
# * Running on http://127.0.0.1:5000
# * Debug mode: on
```

### **Paso 3: Configurar el Frontend**

#### **3.1 Instalar Dependencias del Frontend**
```bash
# En una nueva terminal, navegar al directorio frontend
cd frontend
npm install
```

#### **3.2 Configurar Variables de Entorno del Frontend**
```bash
# Crear archivo .env en la carpeta frontend
touch .env  # En Windows: type nul > .env

# Agregar la URL del backend
echo "VITE_API_URL=http://localhost:5000" >> .env
```

#### **3.3 Verificar Instalación del Frontend**
```bash
# Ejecutar el servidor de desarrollo
npm run dev

# Deberías ver:
# Local:   http://localhost:3001/
# Network: http://192.168.x.x:3001/
```

## 🔧 **Configuración Avanzada**

### **Base de Datos PostgreSQL (Producción)**

#### **Instalar PostgreSQL**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# macOS (con Homebrew)
brew install postgresql
brew services start postgresql

# Windows
# Descargar desde: https://www.postgresql.org/download/windows/
```

#### **Configurar PostgreSQL**
```bash
# Crear usuario y base de datos
sudo -u postgres psql
CREATE USER cvss_user WITH PASSWORD 'tu_password_seguro';
CREATE DATABASE cvss_database OWNER cvss_user;
GRANT ALL PRIVILEGES ON DATABASE cvss_database TO cvss_user;
\q
```

#### **Actualizar Variables de Entorno**
```bash
# En backend/.env
DATABASE_URL=postgresql://cvss_user:tu_password_seguro@localhost:5432/cvss_database
```

### **Configuración de Producción**

#### **Variables de Entorno de Producción**
```bash
# Backend (.env)
SECRET_KEY=tu-secret-key-super-seguro-para-produccion
JWT_SECRET_KEY=tu-jwt-secret-key-super-seguro-para-produccion
DATABASE_URL=postgresql://usuario:password@host:puerto/database
FLASK_ENV=production
CORS_ORIGINS=https://tu-frontend-url.com

# Frontend (.env)
VITE_API_URL=https://tu-backend-url.com
```

## 🚀 **Scripts de Automatización**

### **Script de Instalación Completa (Linux/macOS)**
```bash
#!/bin/bash
# install.sh

echo "🚀 Instalando CVSS Scoring System..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

# Verificar Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js no está instalado"
    exit 1
fi

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias backend
echo "🔧 Instalando dependencias del backend..."
cd backend
pip install --upgrade pip
pip install -r requirements.txt

# Configurar base de datos
echo "🗄️ Configurando base de datos..."
mkdir -p instance
python -c "
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
    print('✅ Base de datos inicializada')
"

# Instalar dependencias frontend
echo "🎨 Instalando dependencias del frontend..."
cd ../frontend
npm install

echo "✅ Instalación completada!"
echo "🚀 Para ejecutar:"
echo "   Backend:  cd backend && python run.py"
echo "   Frontend: cd frontend && npm run dev"
```

### **Script de Instalación para Windows**
```batch
@echo off
REM install.bat

echo 🚀 Instalando CVSS Scoring System...

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no está instalado
    pause
    exit /b 1
)

REM Verificar Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js no está instalado
    pause
    exit /b 1
)

REM Crear entorno virtual
echo 📦 Creando entorno virtual...
python -m venv venv
call venv\Scripts\activate

REM Instalar dependencias backend
echo 🔧 Instalando dependencias del backend...
cd backend
pip install --upgrade pip
pip install -r requirements.txt

REM Configurar base de datos
echo 🗄️ Configurando base de datos...
if not exist instance mkdir instance
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all(); print('✅ Base de datos inicializada')"

REM Instalar dependencias frontend
echo 🎨 Instalando dependencias del frontend...
cd ..\frontend
npm install

echo ✅ Instalación completada!
echo 🚀 Para ejecutar:
echo    Backend:  cd backend ^&^& python run.py
echo    Frontend: cd frontend ^&^& npm run dev
pause
```

## 🧪 **Verificación de la Instalación**

### **Test del Backend**
```bash
cd backend
python -c "
import sys
sys.path.append('.')
from app import create_app
app = create_app()
print('✅ Backend configurado correctamente')
print('📊 Endpoints disponibles:')
for rule in app.url_map.iter_rules():
    print(f'   {rule.methods} {rule.rule}')
"
```

### **Test del Frontend**
```bash
cd frontend
npm run build
echo "✅ Frontend compilado correctamente"
```

### **Test de Integración**
```bash
# En una terminal - Backend
cd backend
python run.py &

# En otra terminal - Frontend
cd frontend
npm run dev &

# Verificar que ambos servicios estén ejecutándose
curl http://localhost:5000/api/admin/health
curl http://localhost:3001
```

## 🔍 **Solución de Problemas Comunes**

### **Error: Python no encontrado**
```bash
# Verificar instalación
python --version
python3 --version

# Instalar Python (Ubuntu/Debian)
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Instalar Python (macOS)
brew install python3
```

### **Error: Node.js no encontrado**
```bash
# Verificar instalación
node --version
npm --version

# Instalar Node.js (Ubuntu/Debian)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Instalar Node.js (macOS)
brew install node
```

### **Error: Dependencias no se instalan**
```bash
# Limpiar cache de pip
pip cache purge

# Reinstalar dependencias
pip install --no-cache-dir -r requirements.txt

# Para problemas con Node.js
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### **Error: Base de datos no se crea**
```bash
# Verificar permisos
ls -la instance/

# Crear manualmente
mkdir -p instance
chmod 755 instance

# Recrear base de datos
rm -f instance/cvss.db
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); db.create_all()"
```

### **Error: Puerto en uso**
```bash
# Encontrar proceso usando el puerto
lsof -i :5000  # Backend
lsof -i :3001  # Frontend

# Terminar proceso
kill -9 <PID>

# O usar puertos diferentes
# Backend: python run.py --port 5001
# Frontend: npm run dev -- --port 3002
```

## 📚 **Recursos Adicionales**

### **Documentación**
- [README.md](./README.md) - Documentación principal
- [DOCUMENT_ANALYZER_README.md](./DOCUMENT_ANALYZER_README.md) - Document Analyzer
- [API Documentation](./API_DOCUMENTATION.md) - Documentación de API

### **Enlaces Útiles**
- [Python 3.10+](https://www.python.org/downloads/)
- [Node.js 18+](https://nodejs.org/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Git](https://git-scm.com/downloads)

### **Soporte**
- Crear un issue en GitHub
- Revisar la documentación completa
- Verificar los logs de error

---

**¡Instalación completada!** 🎉

Tu sistema CVSS Scoring está listo para usar. Accede a:
- **Frontend**: http://localhost:3001
- **Backend**: http://localhost:5000
- **Credenciales**: admin@cvss.com / admin123
