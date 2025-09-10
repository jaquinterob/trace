#!/bin/bash

# Script para ejecutar la aplicación Streamlit
echo "🎵 Iniciando aplicación de Análisis de Audio..."
echo "📦 Verificando dependencias..."

# Verificar si las dependencias están instaladas
python3 -c "import streamlit, requests" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  Instalando dependencias..."
    python3 -m pip install streamlit requests
fi

echo "🚀 Ejecutando aplicación..."
echo "🌐 Abre tu navegador en: http://localhost:8501"
echo "⏹️  Presiona Ctrl+C para detener la aplicación"
echo ""

# Ejecutar la aplicación
python3 -m streamlit run app.py
