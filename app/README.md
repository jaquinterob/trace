# 🎵 Análisis de Audio con Transcripción

Una aplicación web moderna construida con Streamlit que permite analizar archivos de audio y transcribirlos localmente usando Faster Whisper.

## ✨ Características

- **🎤 Transcripción Local**: Transcribe audio usando Faster Whisper sin necesidad de enviar archivos a servicios externos
- **🌍 Detección de Idioma**: Detecta automáticamente el idioma del audio

- **📊 Análisis de Audio**: Integración con APIs externas para análisis adicional
- **💾 Descarga de Resultados**: Exporta transcripciones y análisis en formato TXT
- **🎨 Interfaz Moderna**: Diseño responsive y amigable al usuario

## 🚀 Instalación

1. **Clona el repositorio:**
```bash
git clone <tu-repositorio>
cd streamlit
```

2. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

3. **Ejecuta la aplicación:**
```bash
streamlit run app.py
```

## 📋 Dependencias

- `streamlit>=1.28.0` - Framework web
- `faster-whisper>=0.10.0` - Transcripción de audio rápida
- `torch>=2.0.0` - Backend de PyTorch
- `torchaudio>=2.0.0` - Audio para PyTorch
- `librosa>=0.10.0` - Procesamiento de audio
- `soundfile>=0.12.0` - Lectura/escritura de archivos de audio
- `requests>=2.31.0` - Cliente HTTP

## 🎯 Uso

### Transcripción Local
1. **Selecciona un archivo de audio** (MP3, WAV, M4A, FLAC, OGG)
2. **Configura el modelo Whisper** en la barra lateral:
   - `tiny`: Más rápido, menos preciso
   - `base`: Balance entre velocidad y precisión (recomendado)
   - `small/medium/large`: Más preciso, más lento
3. **Habilita la transcripción local** marcando la casilla correspondiente
4. **Haz clic en "Analizar Audio"**

### Análisis con API Externa
1. **Configura la URL de tu API** en la barra lateral
2. **Opcionalmente agrega un token de autenticación**
3. **Ajusta el timeout** según tus necesidades
4. **Procesa el audio** para obtener transcripción local + análisis externo

## 🔧 Configuración

### Modelos Whisper Disponibles
- **tiny**: ~39 MB, más rápido
- **base**: ~74 MB, balanceado
- **small**: ~244 MB, más preciso
- **medium**: ~769 MB, alta precisión
- **large**: ~1550 MB, máxima precisión
- **large-v2**: ~1550 MB, versión mejorada

### Formatos de Audio Soportados
- MP3
- WAV
- M4A
- FLAC
- OGG

## 📊 Resultados

### Transcripción
- Texto completo transcrito
- Idioma detectado con nivel de confianza
- Duración del audio

### Análisis Externo
- Resultados de la API configurada
- Descripción detallada
- Opción de descarga en formato TXT

## 💡 Consejos de Uso

- **Para transcripciones rápidas**: Usa el modelo `tiny` o `base`
- **Para máxima precisión**: Usa el modelo `large` o `large-v2`
- **Archivos grandes**: Considera dividir archivos muy largos
- **Calidad de audio**: Mejor calidad = mejor transcripción
- **Idioma**: Faster Whisper detecta automáticamente el idioma

## 🐛 Solución de Problemas

### Error de Memoria
- Usa un modelo más pequeño (tiny/base)
- Cierra otras aplicaciones que consuman memoria

### Error de Transcripción
- Verifica que el archivo de audio no esté corrupto
- Asegúrate de que el formato sea compatible
- Intenta con un archivo más corto

### Dependencias
- Asegúrate de tener Python 3.8+
- Instala todas las dependencias del requirements.txt
- En macOS, puede ser necesario instalar ffmpeg: `brew install ffmpeg`

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- [Faster Whisper](https://github.com/guillaumekln/faster-whisper) por la implementación rápida de Whisper
- [Streamlit](https://streamlit.io/) por el framework web
- [OpenAI Whisper](https://github.com/openai/whisper) por el modelo base
