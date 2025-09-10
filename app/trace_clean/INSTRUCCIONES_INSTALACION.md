# TRACE - Instrucciones de Instalación

## 📋 Descripción
Esta es una versión limpia de la aplicación TRACE para transcripción de audio con IA. Se han eliminado las dependencias pesadas para reducir el tamaño del archivo.

## 🚀 Instalación Rápida

### 1. Crear entorno virtual
```bash
python -m venv .venv
```

### 2. Activar entorno virtual
**En Windows:**
```bash
.venv\Scripts\activate
```

**En macOS/Linux:**
```bash
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
streamlit run app.py
```

## 📦 Dependencias Incluidas
- streamlit>=1.28.0
- requests>=2.31.0
- faster-whisper>=0.10.0
- torch>=2.0.0
- torchaudio>=2.0.0
- numpy>=1.21.0
- librosa>=0.10.0
- soundfile>=0.12.0

## ⚠️ Notas Importantes
- La primera ejecución puede tardar más tiempo debido a la descarga de modelos de IA
- Asegúrate de tener una conexión a internet estable
- El directorio `.venv` se creará automáticamente al instalar las dependencias

## 🎯 Funcionalidades
- Transcripción de audio local con Whisper
- Análisis de sentimientos y emociones
- Interfaz web moderna y responsive
- Soporte para múltiples formatos de audio (MP3, WAV, M4A, FLAC, OGG)
- Integración con APIs externas (opcional)

## 📁 Estructura de Archivos
```
trace_clean/
├── app.py                 # Aplicación principal
├── custom_styles.css      # Estilos personalizados
├── requirements.txt       # Dependencias de Python
├── README.md             # Documentación
├── install.sh            # Script de instalación
├── run.sh               # Script de ejecución
├── test_audio.py        # Script de prueba
├── images/              # Imágenes y logos
│   └── logo.jpeg
└── INSTRUCCIONES_INSTALACION.md  # Este archivo
```

## 🔧 Solución de Problemas
Si encuentras algún error durante la instalación:
1. Verifica que tengas Python 3.8 o superior instalado
2. Asegúrate de tener permisos de escritura en el directorio
3. En caso de errores con PyTorch, instala la versión CPU: `pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu`
