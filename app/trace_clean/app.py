import streamlit as st
import requests
import io
import base64
from typing import Dict, Any
import time
import tempfile
import os
from faster_whisper import WhisperModel
import numpy as np
import librosa
import soundfile as sf

# Configuración de la página
st.set_page_config(
    page_title="TRACE",
    page_icon="♫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la apariencia
st.markdown("""
<style>
    /* Configuración global de fuentes */
    .stApp {
        font-size: 12px !important;  /* Tamaño base de fuente reducido */
    }
    
    /* Títulos principales */
    .main-header h1 {
        font-size: 1.6rem !important;
        font-weight: bold;
    }
    
    .main-header p {
        font-size: 0.8rem !important;
    }
    
    /* Headers de secciones */
    h1, h2, h3 {
        font-size: 1.2rem !important;
        font-weight: 600;
    }
    
    /* Texto del sidebar */
    .css-1d391kg {
        font-size: 12px;
    }
    
    /* Métricas y estadísticas */
    .stMetric {
        font-size: 0.7rem;
    }
    
    /* Métricas de información del archivo */
    .stMetric .metric-container {
        font-size: 0.8rem !important;
    }
    
    .stMetric .metric-value {
        font-size: 0.9rem !important;
        font-weight: 600;
    }
    
    .stMetric .metric-label {
        font-size: 0.7rem !important;
        font-weight: 500;
    }
    
    /* Botones */
    .stButton > button {
        font-size: 0.7rem;
        font-weight: 500;
    }
    
    /* Campos de texto */
    .stTextInput input {
        font-size: 12px;
    }
    
    /* Selectores */
    .stSelectbox select {
        font-size: 12px;
    }
    
    /* Checkboxes */
    .stCheckbox label {
        font-size: 12px;
    }
    
    /* Sliders */
    .stSlider label {
        font-size: 12px;
    }
    
    .main-header {
        height: 200px;
        text-align: center;
        padding: 1rem 0;
        background: #25054c;
        color: white;
        border-radius: 10px;
        margin-bottom: 1rem;
    }

.st-cf {
    background: linear-gradient(to right, rgb(253 116 1) 0%, rgb(254 119 1) 21.7391%, rgba(151, 166, 195, 0.25) 21.7391%, rgba(151, 166, 195, 0.25) 100%);
}


    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 0.5rem;
        flex-wrap: wrap;
        gap: 20px;
    }
    
    .logo-container img {
        height: 150px;
        width: auto;
    }
    
    .logo-container h1 {
        margin: 0;
        font-size: 1.6rem !important;
        font-weight: bold;
    }
    
    @media (max-width: 768px) {
        .logo-container {
            flex-direction: column;
            gap: 10px;
        }
        
        .logo-container img {
            height: 600px;
        }
        
        .logo-container h1 {
            font-size: 1.3rem !important;
        }
    }
    
    .upload-section {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 2px dashed #dee2e6;
        text-align: center;
        margin: 1rem 0;
    }
    
    .result-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 4px solid #667eea;
    }
    
    .success-message {
        background-color: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
    }
    
    .error-message {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
    }
    
    .loading-spinner {
        text-align: center;
        padding: 2rem;
    }
    
    /* Sección de información del archivo */
    .file-info-section {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    .file-info-section .stMetric {
        font-size: 0.6rem !important;
    }
    
    .file-info-section .stMetric .metric-value {
        font-size: 0.7rem !important;
        font-weight: 500;
    }
    
    .file-info-section .stMetric .metric-label {
        font-size: 0.6rem !important;
        font-weight: 400;
    }
    
    /* Iconos profesionales con símbolos Unicode */
    .icon-music::before {
        content: "♫";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-settings::before {
        content: "⚙";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-upload::before {
        content: "↑";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-download::before {
        content: "↓";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-play::before {
        content: "▶";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-check::before {
        content: "✓";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #28a745;
    }
    
    .icon-error::before {
        content: "✕";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #dc3545;
    }
    
    .icon-info::before {
        content: "ℹ";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #17a2b8;
    }
    
    .icon-warning::before {
        content: "⚠";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #ffc107;
    }
    
    .icon-stats::before {
        content: "📊";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-tips::before {
        content: "💡";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #ffc107;
    }
    
    .icon-file::before {
        content: "📁";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-time::before {
        content: "⏱";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }

    .st-emotion-cache-11xx4re {
        background-color: rgb(253 116 1);
    }

    .st-e3 {
    background-color: rgb(249 119 0);
}
    
    .icon-globe::before {
        content: "🌐";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-microphone::before {
        content: "🎤";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-target::before {
        content: "🎯";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-document::before {
        content: "📄";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
    }
    
    .icon-loading::before {
        content: "⟳";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #667eea;
        animation: spin 1s linear infinite;
    }
    
    .icon-success::before {
        content: "✓";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #28a745;
    }
    
    .icon-waiting::before {
        content: "⏳";
        font-family: "Arial", sans-serif;
        margin-right: 8px;
        font-weight: bold;
        color: #6c757d;
    }
    
    /* Animación para el icono de carga */
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Clases para elementos específicos */
    .metric-icon {
        font-size: 1.2em;
        margin-right: 8px;
    }
    
    .button-icon {
        font-size: 1.1em;
        margin-right: 6px;
    }
    
    .header-icon {
        font-size: 1.3em;
        margin-right: 10px;
    }
    
    /* Estilos para la tabla de IA */
    .stDataFrame {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .stDataFrame table {
        border-collapse: collapse;
    }
    
    .stDataFrame th {
        background-color: #f8f9fa !important;
        color: #495057 !important;
        font-weight: 600 !important;
        border-bottom: 2px solid #dee2e6 !important;
    }
    
    .stDataFrame td {
        border-bottom: 1px solid #e9ecef !important;
        padding: 0.75rem !important;
    }
    
    .stDataFrame tr:hover {
        background-color: #f8f9fa !important;
    }
</style>
""", unsafe_allow_html=True)

def transcribe_audio(audio_file, model_size="base"):
    """
    Transcribe audio using Faster Whisper
    
    Args:
        audio_file: Uploaded audio file
        model_size: Whisper model size (tiny, base, small, medium, large, large-v2)
    
    Returns:
        dict: Transcription results
    """
    try:
        # Create temporary file to save the uploaded audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            # Convert audio to WAV format if needed
            if audio_file.type != "audio/wav":
                # Load audio with librosa and resample to 16kHz
                audio_data, sr = librosa.load(audio_file, sr=16000)
                # Save as WAV
                sf.write(tmp_file.name, audio_data, sr)
            else:
                # Save original WAV file
                tmp_file.write(audio_file.read())
                audio_file.seek(0)  # Reset file pointer
            
            tmp_file_path = tmp_file.name
        
        try:
            # Initialize Whisper model
            with st.spinner(f"⟳ Cargando modelo Whisper {model_size}..."):
                model = WhisperModel(model_size, device="cpu", compute_type="int8")
            
            # Transcribe audio
            with st.spinner("🎤 Transcribiendo audio..."):
                segments, info = model.transcribe(tmp_file_path, beam_size=5)
                
                # Collect transcription results
                transcription_text = ""
                
                for segment in segments:
                    transcription_text += segment.text + " "
                
                # Get language info
                detected_language = info.language
                language_probability = info.language_probability
                
                return {
                    "success": True,
                    "transcription": transcription_text.strip(),
                    "language": detected_language,
                    "language_probability": language_probability,
                    "duration": info.duration
                }
                
        finally:
            # Clean up temporary file
            if os.path.exists(tmp_file_path):
                os.unlink(tmp_file_path)
                
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

def display_transcription_results(transcription_result: Dict[str, Any]):
    """Muestra los resultados de la transcripción de manera amigable"""
    
    st.markdown('<h2><span class="icon-microphone header-icon"></span>Resultados de la Transcripción</h2>', unsafe_allow_html=True)
    
    if transcription_result["success"]:
        # Mostrar transcripción completa
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<h3><span class="icon-document header-icon"></span>Transcripción Completa</h3>', unsafe_allow_html=True)
        st.markdown(f"**{transcription_result['transcription']}**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Mostrar información del idioma
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🌐 Idioma Detectado", transcription_result['language'].upper())
        with col2:
            st.metric("📊 Confianza", f"{transcription_result['language_probability']:.2%}")
        with col3:
            st.metric("⏱ Duración", f"{transcription_result['duration']:.1f}s")
        
        # Botón para descargar transcripción
        if st.button("↓ Descargar Transcripción", use_container_width=True):
            # Crear archivo de texto con la transcripción
            transcription_text = f"""Transcripción de Audio
=============================

Idioma: {transcription_result['language']} (Confianza: {transcription_result['language_probability']:.2%})
Duración: {transcription_result['duration']:.1f} segundos

TRANSCRIPCIÓN:
{transcription_result['transcription']}

Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')}
"""
            
            st.download_button(
                label="↓ Descargar como TXT",
                data=transcription_text,
                file_name=f"transcripcion_audio_{int(time.time())}.txt",
                mime="text/plain"
            )
    
    else:
        st.error(f"✕ Error en la transcripción: {transcription_result['error']}")

def generate_ai_results():
    """Genera resultados de ejemplo de un modelo de IA"""
    import random
    
    # Datos de ejemplo para la tabla de resultados de IA
    results = [
        {
            "categoria": "Sentimiento",
            "resultado": "Positivo",
            "confianza": random.uniform(0.75, 0.95),
            "descripcion": "El audio muestra un tono optimista y constructivo",
            "status": "success"
        },
        {
            "categoria": "Idioma Principal",
            "resultado": "Español",
            "confianza": random.uniform(0.85, 0.98),
            "descripcion": "Idioma detectado con alta precisión",
            "status": "success"
        },
        {
            "categoria": "Calidad de Audio",
            "resultado": "Buena",
            "confianza": random.uniform(0.70, 0.90),
            "descripcion": "Ruido de fondo mínimo, voz clara",
            "status": "success"
        },
        {
            "categoria": "Temas Detectados",
            "resultado": "Tecnología, Negocios",
            "confianza": random.uniform(0.60, 0.85),
            "descripcion": "Conversación sobre innovación tecnológica",
            "status": "warning"
        },
        {
            "categoria": "Emociones",
            "resultado": "Confianza, Entusiasmo",
            "confianza": random.uniform(0.65, 0.80),
            "descripcion": "El hablante muestra seguridad en sus ideas",
            "status": "success"
        },
        {
            "categoria": "Ruido de Fondo",
            "resultado": "Bajo",
            "confianza": random.uniform(0.80, 0.95),
            "descripcion": "Entorno de grabación controlado",
            "status": "success"
        }
    ]
    
    return results

def display_ai_results_table():
    """Muestra la tabla de resultados de IA"""
    results = generate_ai_results()
    
    # Crear DataFrame para la tabla
    import pandas as pd
    
    # Preparar datos para la tabla
    table_data = []
    for result in results:
        table_data.append({
            "Categoría": result["categoria"],
            "Resultado": result["resultado"],
            "Confianza": f"{result['confianza']:.1%}",
            "Descripción": result["descripcion"],
            "Estado": result["status"].upper()
        })
    
    # Crear DataFrame
    df = pd.DataFrame(table_data)
    
    # Mostrar título
    st.markdown("### Análisis de IA - Resultados del Modelo")
    
    # Mostrar tabla con estilo
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Categoría": st.column_config.TextColumn(
                "Categoría",
                width="medium",
                help="Tipo de análisis realizado"
            ),
            "Resultado": st.column_config.TextColumn(
                "Resultado",
                width="medium",
                help="Valor detectado por la IA"
            ),
            "Confianza": st.column_config.TextColumn(
                "Confianza",
                width="small",
                help="Nivel de confianza del modelo"
            ),
            "Descripción": st.column_config.TextColumn(
                "Descripción",
                width="large",
                help="Explicación detallada del resultado"
            ),
            "Estado": st.column_config.TextColumn(
                "Estado",
                width="small",
                help="Estado del análisis"
            )
        }
    )

def is_valid_api_url(url: str) -> bool:
    """Verifica si la URL de la API es válida y no es la URL de ejemplo"""
    if not url or not url.strip():
        return False
    
    # Verificar si es la URL de ejemplo
    if "api.ejemplo.com" in url or "example.com" in url:
        return False
    
    # Verificar formato básico de URL
    if not url.startswith(("http://", "https://")):
        return False
    
    return True

def process_audio(uploaded_file, api_url: str, api_token: str, timeout: int, enable_transcription: bool = True, whisper_model: str = "base"):
    """Procesa el archivo de audio enviándolo a la API y opcionalmente transcribe localmente"""
    
    # Verificar si la API es válida
    api_is_valid = is_valid_api_url(api_url)
    
    # Si la transcripción está habilitada, transcribir primero
    transcription_result = None
    if enable_transcription:
        st.info("🎤 Iniciando transcripción local del audio...")
        transcription_result = transcribe_audio(uploaded_file, whisper_model)
        
        if transcription_result["success"]:
            st.success("✓ Transcripción completada!")
            display_transcription_results(transcription_result)
        else:
            st.error(f"✕ Error en la transcripción: {transcription_result['error']}")
    
    # Solo intentar usar la API si es válida
    if api_is_valid:
        st.info("🌐 Enviando archivo a API externa para análisis adicional...")
        
        # Mostrar spinner de carga
        with st.spinner("⟳ Procesando con API externa..."):
            try:
                # Preparar los datos para enviar a la API
                files = {
                    'audio': (uploaded_file.name, uploaded_file, uploaded_file.type)
                }
                
                # Headers
                headers = {}
                if api_token:
                    headers['Authorization'] = f'Bearer {api_token}'
                
                # Realizar la petición a la API externa
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simular progreso
                for i in range(3):
                    progress_bar.progress((i + 1) * 33)
                    if i == 0:
                        status_text.text("↑ Enviando archivo a API externa...")
                    elif i == 1:
                        status_text.text("⟳ Procesando en API externa...")
                    else:
                        status_text.text("↓ Recibiendo respuesta de API...")
                    time.sleep(0.5)
                
                # Hacer la petición real
                response = requests.post(
                    api_url,
                    files=files,
                    headers=headers,
                    timeout=timeout
                )
                
                progress_bar.progress(100)
                status_text.text("✓ Completado!")
                
                # Verificar respuesta
                if response.status_code == 200:
                    result = response.json()
                    display_results(result)
                else:
                    st.error(f"✕ Error en la API externa: {response.status_code}")
                    st.error(f"Respuesta: {response.text}")
                    
            except requests.exceptions.Timeout:
                st.error("⏱ Timeout: La API externa tardó demasiado en responder")
            except requests.exceptions.ConnectionError:
                st.error("✕ Error de conexión: No se pudo conectar con la API externa")
            except requests.exceptions.RequestException as e:
                st.error(f"✕ Error en la petición: {str(e)}")
            except Exception as e:
                st.error(f"✕ Error inesperado: {str(e)}")
            
            # Limpiar elementos de progreso
            time.sleep(1)
            st.empty()
    else:
        # Si no hay API válida, mostrar mensaje informativo
        st.info("ℹ No se configuró una API externa válida. Solo se realizó la transcripción local.")
        st.markdown("""
        <div class="result-card">
        <h3><span class="icon-tips"></span>Para análisis adicional</h3>
        <p>Si deseas enviar el audio a una API externa para análisis adicional, configura una URL válida en la barra lateral.</p>
        </div>
        """, unsafe_allow_html=True)

def display_results(result: Dict[str, Any]):
    """Muestra los resultados de manera amigable"""
    
    st.markdown('<h2><span class="icon-document header-icon"></span>Resultados del Análisis</h2>', unsafe_allow_html=True)
    
    # Verificar que el resultado tenga la estructura esperada
    if 'resultado' in result and 'descripcion' in result:
        # Mostrar resultado principal
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<h3><span class="icon-target header-icon"></span>Resultado Principal</h3>', unsafe_allow_html=True)
        st.markdown(f"**{result['resultado']}**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Mostrar descripción
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown('<h3><span class="icon-document header-icon"></span>Descripción Detallada</h3>', unsafe_allow_html=True)
        st.markdown(result['descripcion'])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Botón para descargar resultados
        if st.button("↓ Descargar Resultados", use_container_width=True):
            # Crear archivo de texto con los resultados
            results_text = f"""Resultado del Análisis de Audio
=====================================

Resultado: {result['resultado']}

Descripción:
{result['descripcion']}

Fecha: {time.strftime('%Y-%m-%d %H:%M:%S')}
"""
            
            st.download_button(
                label="↓ Descargar como TXT",
                data=results_text,
                file_name=f"analisis_audio_{int(time.time())}.txt",
                mime="text/plain"
            )
    
    else:
        st.warning("⚠ El resultado no tiene la estructura esperada")
        st.json(result)

def main():
    # Header principal con logo
    st.markdown("""
    <div class="main-header">
        <div class="logo-container">
            <img src="data:image/jpeg;base64,{}" alt="TRACE Logo">
        </div>
    </div>
    """.format(base64.b64encode(open("images/logo.jpeg", "rb").read()).decode()), unsafe_allow_html=True)
    
    # Sidebar para configuración
    with st.sidebar:
        st.markdown('<h2>Configuración</h2>', unsafe_allow_html=True)
        
        # URL de la API
        api_url = st.text_input(
            "URL de la API",
            value="",
            placeholder="https://tu-api.com/analyze",
            help="Ingresa la URL del endpoint de tu API (opcional - si no se proporciona, solo se realizará transcripción local)"
        )
        
        # Token de autenticación (opcional)
        api_token = st.text_input(
            "Token de API (opcional)",
            type="password",
            help="Si tu API requiere autenticación"
        )
        
        # Timeout para la petición
        timeout = st.slider(
            "Timeout (segundos)",
            min_value=5,
            max_value=120,
            value=30,
            help="Tiempo máximo de espera para la respuesta de la API"
        )
        
        st.markdown("---")
        st.markdown('<h3>Transcripción de Audio</h3>', unsafe_allow_html=True)
        
        # Modelo de Whisper
        whisper_model = st.selectbox(
            "Modelo Whisper",
            options=["tiny", "base", "small", "medium", "large", "large-v2"],
            index=1,  # base por defecto
            help="Modelo más pequeño = más rápido, modelo más grande = más preciso"
        )
        
        # Habilitar transcripción
        enable_transcription = st.checkbox(
            "Habilitar transcripción local",
            value=True,
            help="Usar Faster Whisper para transcripción local del audio"
        )
        
        st.markdown("---")
        st.markdown('<h3>Formatos soportados</h3>', unsafe_allow_html=True)
        st.markdown("- MP3")
        st.markdown("- WAV")
        st.markdown("- M4A")
        st.markdown("- FLAC")
        st.markdown("- OGG")
    
    # Sección principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('', unsafe_allow_html=True)
        
        # Uploader de archivos
        uploaded_file = st.file_uploader(
            "Selecciona tu archivo de audio",
            type=['mp3', 'wav', 'm4a', 'flac', 'ogg'],
            help="Arrastra y suelta tu archivo aquí o haz clic para seleccionar"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Mostrar tabla de resultados de IA
        display_ai_results_table()
        
        # Mostrar información del archivo si se ha cargado
        if uploaded_file is not None:
            st.success(f"✓ Archivo cargado: {uploaded_file.name}")
            
            # Información del archivo
            file_size = uploaded_file.size
            file_size_mb = file_size / (1024 * 1024)
            
            st.markdown('<div class="file-info-section">', unsafe_allow_html=True)
            col_info1, col_info2, col_info3 = st.columns(3)
            with col_info1:
                st.metric("📁 Nombre", uploaded_file.name)
            with col_info2:
                st.metric("📏 Tamaño", f"{file_size_mb:.2f} MB")
            with col_info3:
                st.metric("♫ Tipo", uploaded_file.type)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Botón para procesar
            if st.button("▶ Analizar Audio", type="primary", width='stretch'):
                process_audio(uploaded_file, api_url, api_token, timeout, enable_transcription, whisper_model)
    
    with col2:
        st.markdown('<div class="stats-section"><h3>Estadísticas</h3></div>', unsafe_allow_html=True)
        
        # Placeholder para estadísticas
        st.markdown('<div class="stats-section">', unsafe_allow_html=True)
        if uploaded_file is not None:
            st.metric("Estado", "✓ Listo")
            st.metric("Progreso", "0%")
        else:
            st.markdown('<div style="font-size: 16px;">Estado: Esperando</div>', unsafe_allow_html=True)
            st.metric("Progreso", "0%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown('<h3><span class="icon-tips header-icon"></span>Consejos</h3>', unsafe_allow_html=True)
        st.markdown("- Asegúrate de que el archivo no sea muy grande")
        st.markdown("- Verifica que la URL de la API sea correcta")
        st.markdown("- El proceso puede tomar unos segundos")
        st.markdown("- La transcripción local es más rápida que enviar a API")

if __name__ == "__main__":
    main()
