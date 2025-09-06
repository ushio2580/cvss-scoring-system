# 🚀 Guía de Despliegue - CVSS Scoring System

## 🌐 **Opciones de Despliegue**

### **Opción 1: Render.com (Backend) + Netlify (Frontend) - RECOMENDADO**
- ✅ **Gratuito** para proyectos pequeños
- ✅ **Fácil configuración**
- ✅ **Despliegue automático** desde GitHub
- ✅ **SSL automático**
- ✅ **Base de datos PostgreSQL incluida**

### **Opción 2: Railway (Backend) + Vercel (Frontend)**
- ✅ **Gratuito** con límites generosos
- ✅ **Despliegue automático**
- ✅ **Base de datos PostgreSQL incluida**

### **Opción 3: Heroku (Backend) + Vercel (Frontend)**
- ⚠️ **Heroku ya no es gratuito**
- ✅ **Muy estable y confiable**

## 🎯 **Despliegue en Render.com + Netlify**

### **Paso 1: Preparar el Repositorio**

#### **1.1 Verificar Estructura del Proyecto**
```bash
# Verificar que todos los archivos estén presentes
ls -la
ls -la backend/
ls -la frontend/

# Verificar archivos de configuración
cat backend/requirements.txt
cat frontend/package.json
```

#### **1.2 Configurar Archivos de Despliegue**
```bash
# Crear Procfile para Render.com (si no existe)
echo "web: gunicorn wsgi:app" > Procfile

# Crear runtime.txt para especificar versión de Python
echo "python-3.10.11" > runtime.txt

# Verificar netlify.toml en frontend
cat frontend/netlify.toml
```

### **Paso 2: Desplegar Backend en Render.com**

#### **2.1 Crear Cuenta en Render.com**
1. Ve a [render.com](https://render.com)
2. Crea una cuenta gratuita
3. Conecta tu cuenta de GitHub

#### **2.2 Crear Servicio Web**
1. Haz clic en **"New +"** → **"Web Service"**
2. Conecta tu repositorio de GitHub
3. Configura el servicio:

```
Name: cvss-scoring-system
Environment: Python 3
Build Command: pip install -r backend/requirements.txt
Start Command: gunicorn wsgi:app
```

#### **2.3 Configurar Variables de Entorno**
En la sección **"Environment Variables"**:

```
SECRET_KEY=tu-secret-key-super-seguro-para-produccion
JWT_SECRET_KEY=tu-jwt-secret-key-super-seguro-para-produccion
FLASK_ENV=production
CORS_ORIGINS=https://tu-frontend-url.netlify.app
```

#### **2.4 Crear Base de Datos PostgreSQL**
1. Haz clic en **"New +"** → **"PostgreSQL"**
2. Configura la base de datos:

```
Name: cvss-database
Database: cvss_database
User: cvss_user
```

3. Copia la **"External Database URL"**
4. Agrega la variable de entorno:

```
DATABASE_URL=postgresql://usuario:password@host:puerto/database
```

#### **2.5 Desplegar**
1. Haz clic en **"Create Web Service"**
2. Espera a que se complete el despliegue (5-10 minutos)
3. Anota la URL del servicio: `https://tu-servicio.onrender.com`

### **Paso 3: Desplegar Frontend en Netlify**

#### **3.1 Crear Cuenta en Netlify**
1. Ve a [netlify.com](https://netlify.com)
2. Crea una cuenta gratuita
3. Conecta tu cuenta de GitHub

#### **3.2 Crear Nuevo Sitio**
1. Haz clic en **"New site from Git"**
2. Selecciona **"GitHub"**
3. Elige tu repositorio

#### **3.3 Configurar Build Settings**
```
Base directory: frontend
Build command: npm run build
Publish directory: frontend/dist
```

#### **3.4 Configurar Variables de Entorno**
En **"Site settings"** → **"Environment variables"**:

```
VITE_API_URL=https://tu-servicio.onrender.com
```

#### **3.5 Desplegar**
1. Haz clic en **"Deploy site"**
2. Espera a que se complete el build (3-5 minutos)
3. Anota la URL del sitio: `https://tu-sitio.netlify.app`

### **Paso 4: Configurar CORS y Finalizar**

#### **4.1 Actualizar CORS en Backend**
En Render.com, actualiza la variable de entorno:

```
CORS_ORIGINS=https://tu-sitio.netlify.app
```

#### **4.2 Reiniciar Servicio Backend**
1. Ve a tu servicio en Render.com
2. Haz clic en **"Manual Deploy"** → **"Deploy latest commit"**

#### **4.3 Verificar Despliegue**
```bash
# Verificar backend
curl https://tu-servicio.onrender.com/api/admin/health

# Verificar frontend
curl https://tu-sitio.netlify.app
```

## 🚀 **Despliegue en Railway + Vercel**

### **Paso 1: Desplegar Backend en Railway**

#### **1.1 Crear Cuenta en Railway**
1. Ve a [railway.app](https://railway.app)
2. Crea una cuenta gratuita
3. Conecta tu cuenta de GitHub

#### **1.2 Crear Proyecto**
1. Haz clic en **"New Project"**
2. Selecciona **"Deploy from GitHub repo"**
3. Elige tu repositorio

#### **1.3 Configurar Servicio**
1. Railway detectará automáticamente que es un proyecto Python
2. Configura las variables de entorno:

```
SECRET_KEY=tu-secret-key-super-seguro
JWT_SECRET_KEY=tu-jwt-secret-key-super-seguro
FLASK_ENV=production
```

#### **1.4 Agregar Base de Datos PostgreSQL**
1. Haz clic en **"New"** → **"Database"** → **"PostgreSQL"**
2. Railway creará automáticamente la variable `DATABASE_URL`

#### **1.5 Configurar Build**
En **"Settings"** → **"Build"**:

```
Build Command: cd backend && pip install -r requirements.txt
Start Command: cd backend && gunicorn wsgi:app
```

### **Paso 2: Desplegar Frontend en Vercel**

#### **2.1 Crear Cuenta en Vercel**
1. Ve a [vercel.com](https://vercel.com)
2. Crea una cuenta gratuita
3. Conecta tu cuenta de GitHub

#### **2.2 Importar Proyecto**
1. Haz clic en **"New Project"**
2. Importa tu repositorio de GitHub
3. Configura el proyecto:

```
Framework Preset: Vite
Root Directory: frontend
Build Command: npm run build
Output Directory: dist
```

#### **2.3 Configurar Variables de Entorno**
```
VITE_API_URL=https://tu-servicio.railway.app
```

#### **2.4 Desplegar**
1. Haz clic en **"Deploy"**
2. Espera a que se complete el build

## 🔧 **Configuración Avanzada**

### **Configuración de Dominio Personalizado**

#### **Netlify**
1. Ve a **"Domain settings"**
2. Haz clic en **"Add custom domain"**
3. Agrega tu dominio
4. Configura los registros DNS según las instrucciones

#### **Render.com**
1. Ve a **"Settings"** → **"Custom Domains"**
2. Agrega tu dominio
3. Configura los registros DNS

### **Configuración de SSL**
- ✅ **Netlify**: SSL automático con Let's Encrypt
- ✅ **Render.com**: SSL automático
- ✅ **Vercel**: SSL automático
- ✅ **Railway**: SSL automático

### **Configuración de Monitoreo**

#### **Render.com**
- Monitoreo básico incluido
- Logs disponibles en tiempo real
- Alertas por email

#### **Netlify**
- Analytics básico incluido
- Logs de build disponibles
- Webhooks para integración

## 🚨 **Solución de Problemas de Despliegue**

### **Error: Build Failed**

#### **Backend Build Failed**
```bash
# Verificar logs en Render.com/Railway
# Problemas comunes:
# 1. Dependencias faltantes en requirements.txt
# 2. Versión de Python incorrecta
# 3. Variables de entorno faltantes

# Solución:
# 1. Verificar requirements.txt
cat backend/requirements.txt

# 2. Verificar runtime.txt
cat runtime.txt

# 3. Verificar variables de entorno en el panel
```

#### **Frontend Build Failed**
```bash
# Verificar logs en Netlify/Vercel
# Problemas comunes:
# 1. Variables de entorno faltantes
# 2. Errores de TypeScript
# 3. Dependencias faltantes

# Solución:
# 1. Verificar package.json
cat frontend/package.json

# 2. Verificar variables de entorno
# 3. Verificar tsconfig.json
cat frontend/tsconfig.json
```

### **Error: CORS Policy**

```bash
# Verificar configuración CORS en backend
# En Render.com/Railway, agregar:
CORS_ORIGINS=https://tu-frontend-url.com

# Reiniciar el servicio backend
```

### **Error: Database Connection**

```bash
# Verificar DATABASE_URL
# Debe incluir usuario, password, host, puerto y database
DATABASE_URL=postgresql://usuario:password@host:puerto/database

# Verificar que la base de datos esté activa
# En Render.com: verificar que el servicio PostgreSQL esté "Live"
# En Railway: verificar que la base de datos esté "Active"
```

### **Error: 404 en Frontend**

```bash
# Verificar configuración de redirects
# En Netlify, crear _redirects en public/:
echo "/*    /index.html   200" > frontend/public/_redirects

# En Vercel, crear vercel.json:
echo '{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}' > frontend/vercel.json
```

## 📊 **Monitoreo y Mantenimiento**

### **Logs y Debugging**

#### **Render.com**
```bash
# Ver logs en tiempo real
# En el dashboard, ve a "Logs"
# O usa la CLI:
npx render-cli logs --service tu-servicio
```

#### **Netlify**
```bash
# Ver logs de build
# En el dashboard, ve a "Deploys" → "Deploy log"
# O usa la CLI:
npx netlify-cli logs
```

### **Actualizaciones Automáticas**

#### **Configurar Auto-Deploy**
1. **Render.com**: Auto-deploy está habilitado por defecto
2. **Netlify**: Auto-deploy está habilitado por defecto
3. **Railway**: Auto-deploy está habilitado por defecto
4. **Vercel**: Auto-deploy está habilitado por defecto

#### **Branch Deployments**
```bash
# Para testing, puedes configurar deploys desde branches específicos
# En Netlify: Settings → Build & deploy → Branch deploys
# En Vercel: Settings → Git → Production Branch
```

### **Backup y Recuperación**

#### **Base de Datos**
```bash
# Render.com: Backup automático diario
# Railway: Backup automático
# Para backup manual:
pg_dump $DATABASE_URL > backup.sql

# Para restaurar:
psql $DATABASE_URL < backup.sql
```

## 🎯 **Checklist de Despliegue**

### **Pre-Despliegue**
- [ ] Repositorio actualizado en GitHub
- [ ] Tests pasando localmente
- [ ] Variables de entorno configuradas
- [ ] Archivos de configuración presentes
- [ ] Base de datos configurada

### **Post-Despliegue**
- [ ] Backend respondiendo correctamente
- [ ] Frontend cargando correctamente
- [ ] CORS configurado correctamente
- [ ] Base de datos conectada
- [ ] SSL funcionando
- [ ] Dominio personalizado configurado (si aplica)

### **Verificación Final**
- [ ] Login funcionando
- [ ] Dashboard cargando
- [ ] Document Analyzer funcionando
- [ ] API endpoints respondiendo
- [ ] Base de datos persistente

---

**¡Despliegue completado!** 🎉

Tu sistema CVSS Scoring está ahora disponible en:
- **Frontend**: https://tu-sitio.netlify.app
- **Backend**: https://tu-servicio.onrender.com
- **Credenciales**: admin@cvss.com / admin123
