# 📖 Ejemplo de Uso - Análisis de Audio con Transcripción

## 🚀 Inicio Rápido

### 1. Instalación
```bash
# Dar permisos de ejecución al script de instalación
chmod +x install.sh

# Ejecutar instalación automática
./install.sh
```

### 2. Ejecución
```bash
# Opción 1: Script automático
./run.sh

# Opción 2: Comando directo
streamlit run app.py
```

## 🎯 Casos de Uso Comunes

### Caso 1: Transcripción Rápida de Entrevista
**Objetivo**: Transcribir una entrevista de 10 minutos en español

**Configuración recomendada**:
- Modelo Whisper: `base` (balance entre velocidad y precisión)
- Transcripción local: ✅ Habilitada
- API externa: Opcional

**Pasos**:
1. Carga el archivo MP3 de la entrevista
2. Verifica que "Habilitar transcripción local" esté marcado
3. Selecciona modelo `base`
4. Haz clic en "Analizar Audio"
5. Espera la transcripción (puede tomar 2-3 minutos)
6. Descarga la transcripción en formato TXT

**Resultado esperado**:
- Transcripción completa en español
- Detección automática del idioma
- Duración del audio

### Caso 2: Análisis de Podcast en Inglés
**Objetivo**: Transcribir y analizar un podcast de 30 minutos

**Configuración recomendada**:
- Modelo Whisper: `medium` (mayor precisión para inglés)
- Transcripción local: ✅ Habilitada
- API externa: Configurada para análisis de contenido

**Pasos**:
1. Carga el archivo del podcast
2. Selecciona modelo `medium`
3. Configura la URL de tu API de análisis
4. Procesa el audio
5. Obtén transcripción + análisis externo

### Caso 3: Transcripción de Notas de Voz
**Objetivo**: Transcribir múltiples notas de voz cortas

**Configuración recomendada**:
- Modelo Whisper: `tiny` (máxima velocidad)
- Transcripción local: ✅ Habilitada
- API externa: No necesaria

**Ventajas**:
- Procesamiento muy rápido
- Ideal para notas de 1-2 minutos
- Menor uso de memoria

## 🔧 Configuraciones Avanzadas

### Optimización de Memoria
```python
# En la función transcribe_audio, puedes modificar:
model = WhisperModel(
    model_size, 
    device="cpu",           # Usar CPU en lugar de GPU
    compute_type="int8"     # Reducir precisión para ahorrar memoria
)
```

### Personalización de Transcripción
```python
# Modificar parámetros de transcripción:
segments, info = model.transcribe(
    tmp_file_path,
    beam_size=5,           # Aumentar para mayor precisión
    language="es",          # Forzar idioma español
    task="transcribe"       # o "translate" para traducción
)
```

## 📊 Comparación de Modelos

| Modelo | Tamaño | Velocidad | Precisión | Uso de Memoria |
|--------|--------|-----------|-----------|----------------|
| tiny   | ~39 MB | ⚡⚡⚡⚡⚡ | ⭐⭐ | 💾💾 |
| base   | ~74 MB | ⚡⚡⚡⚡ | ⭐⭐⭐ | 💾💾💾 |
| small  | ~244 MB| ⚡⚡⚡ | ⭐⭐⭐⭐ | 💾💾💾💾 |
| medium | ~769 MB| ⚡⚡ | ⭐⭐⭐⭐⭐ | 💾💾💾💾💾 |
| large  | ~1550 MB| ⚡ | ⭐⭐⭐⭐⭐ | 💾💾💾💾💾💾 |

## 🎵 Formatos de Audio Soportados

### Recomendados
- **WAV**: Mejor calidad, mayor tamaño
- **MP3**: Balance calidad/tamaño, ampliamente compatible
- **M4A**: Buena calidad, menor tamaño

### Especializados
- **FLAC**: Sin pérdida, muy alta calidad
- **OGG**: Código abierto, buena compresión

## 💡 Consejos de Rendimiento

### Para Archivos Grandes (>50 MB)
1. Usa modelo `tiny` o `base`
2. Cierra otras aplicaciones
3. Considera dividir el archivo
4. Usa formato WAV para mejor calidad

### Para Transcripciones en Tiempo Real
1. Usa modelo `tiny`
2. Archivos de máximo 5 minutos
3. Calidad de audio 16kHz
4. Formato WAV o MP3

### Para Máxima Precisión
1. Usa modelo `large` o `large-v2`
2. Audio de alta calidad (44.1kHz+)
3. Formato WAV sin compresión
4. Ambiente silencioso en la grabación

## 🐛 Solución de Problemas Comunes

### Error: "CUDA out of memory"
**Solución**: Cambia a modelo más pequeño o usa CPU
```python
model = WhisperModel(model_size, device="cpu")
```

### Error: "File format not supported"
**Solución**: Convierte a formato compatible
```bash
ffmpeg -i audio.m4a audio.wav
```

### Transcripción muy lenta
**Soluciones**:
- Usa modelo más pequeño
- Reduce calidad del audio
- Cierra otras aplicaciones
- Verifica espacio en disco

### Calidad de transcripción baja
**Soluciones**:
- Usa modelo más grande
- Mejora calidad del audio original
- Verifica que no haya ruido de fondo
- Usa formato WAV sin compresión

## 📱 Uso en Diferentes Sistemas

### macOS
```bash
# Instalar ffmpeg si es necesario
brew install ffmpeg

# Ejecutar aplicación
./run.sh
```

### Linux
```bash
# Instalar dependencias del sistema
sudo apt-get install ffmpeg python3-pip

# Ejecutar aplicación
./run.sh
```

### Windows
```bash
# Usar WSL o Git Bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
streamlit run app.py
```

## 🔮 Próximas Características

- [ ] Soporte para GPU (CUDA)
- [ ] Transcripción en tiempo real
- [ ] Traducción automática
- [ ] Análisis de sentimientos
- [ ] Exportación a formatos múltiples
- [ ] Integración con servicios en la nube
- [ ] API REST para uso programático
