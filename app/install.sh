#!/bin/bash

echo "🎵 Instalando Análisis de Audio con Transcripción"
echo "=================================================="

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado. Por favor, instala Python 3.8+ primero."
    exit 1
fi

# Verificar versión de Python
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Se requiere Python 3.8+ pero tienes Python $python_version"
    exit 1
fi

echo "✅ Python $python_version detectado"

# Verificar si pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 no está instalado. Instalando pip..."
    python3 -m ensurepip --upgrade
fi

echo "✅ pip3 detectado"

# Actualizar pip
echo "🔄 Actualizando pip..."
python3 -m pip install --upgrade pip

# Instalar dependencias
echo "🔄 Instalando dependencias..."
python3 -m pip install -r requirements.txt

# Verificar instalación
echo "🔍 Verificando instalación..."
python3 -c "import streamlit, faster_whisper, torch, librosa, soundfile; print('✅ Todas las dependencias instaladas correctamente')"

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 ¡Instalación completada exitosamente!"
    echo ""
    echo "Para ejecutar la aplicación:"
    echo "  streamlit run app.py"
    echo ""
    echo "O usa el script de ejecución:"
    echo "  ./run.sh"
    echo ""
    echo "La aplicación se abrirá en tu navegador en http://localhost:8501"
else
    echo "❌ Error durante la instalación. Revisa los mensajes de error arriba."
    exit 1
fi
