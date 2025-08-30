# Despliegue en Netlify

## Configuración Actual

- **Backend**: Desplegado en Render.com en `https://cvss-scoring-system.onrender.com`
- **Frontend**: Configurado para conectarse al backend de Render.com

## Pasos para desplegar en Netlify

### Opción 1: Despliegue desde GitHub (Recomendado)

1. **Conecta tu repositorio de GitHub a Netlify:**
   - Ve a [netlify.com](https://netlify.com)
   - Haz clic en "New site from Git"
   - Selecciona GitHub y autoriza Netlify
   - Selecciona tu repositorio

2. **Configuración del build:**
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`

3. **Variables de entorno:**
   - Ve a Site settings > Environment variables
   - Agrega:
     - `VITE_API_URL`: `https://cvss-scoring-system.onrender.com/api`
     - `VITE_DEV_MODE`: `false`

4. **Haz clic en "Deploy site"**

### Opción 2: Despliegue manual

1. **Sube los archivos del directorio `dist`:**
   - Ve a [netlify.com](https://netlify.com)
   - Arrastra y suelta el directorio `dist` en la zona de deploy

2. **Configura las variables de entorno:**
   - Ve a Site settings > Environment variables
   - Agrega las mismas variables que en la Opción 1

### Opción 3: Usando Netlify CLI

1. **Instala Netlify CLI:**
   ```bash
   npm install -g netlify-cli
   ```

2. **Inicia sesión:**
   ```bash
   netlify login
   ```

3. **Desde el directorio frontend:**
   ```bash
   netlify deploy --prod --dir=dist
   ```

## Verificación

Después del despliegue, tu aplicación debería estar disponible en una URL como:
`https://tu-sitio.netlify.app`

La aplicación se conectará automáticamente con tu backend en Render.com.

## Troubleshooting

- Si hay problemas de CORS, verifica que el backend esté configurado para aceptar requests desde tu dominio de Netlify
- Si las variables de entorno no se cargan, reinicia el deploy después de agregarlas
- Para debugging, revisa los logs de build en Netlify
