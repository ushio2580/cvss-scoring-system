#!/bin/bash

echo "🚀 Preparando despliegue en Netlify..."

# Verificar que estamos en el directorio correcto
if [ ! -f "package.json" ]; then
    echo "❌ Error: No se encontró package.json. Asegúrate de estar en el directorio frontend/"
    exit 1
fi

# Instalar dependencias si no están instaladas
if [ ! -d "node_modules" ]; then
    echo "📦 Instalando dependencias..."
    npm install
fi

# Construir el proyecto
echo "🔨 Construyendo el proyecto..."
npm run build

# Verificar que el build fue exitoso
if [ ! -d "dist" ]; then
    echo "❌ Error: El directorio dist no se creó. El build falló."
    exit 1
fi

echo "✅ Build completado exitosamente!"
echo ""
echo "📋 Próximos pasos para desplegar en Netlify:"
echo "1. Ve a https://netlify.com"
echo "2. Arrastra y suelta el directorio 'dist' en la zona de deploy"
echo "3. O conecta tu repositorio de GitHub y configura:"
echo "   - Base directory: frontend"
echo "   - Build command: npm run build"
echo "   - Publish directory: dist"
echo ""
echo "🔧 Variables de entorno a configurar en Netlify:"
echo "   VITE_API_URL=https://cvss-scoring-system.onrender.com/api"
echo "   VITE_DEV_MODE=false"
echo ""
echo "🎉 ¡Tu frontend está listo para desplegar!"
