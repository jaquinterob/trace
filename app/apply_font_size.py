#!/usr/bin/env python3
"""
Script para cambiar el tamaño de fuente en la aplicación Streamlit
"""

import streamlit as st

def apply_font_size(size="18px"):
    """
    Aplica un tamaño de fuente específico a toda la aplicación
    
    Args:
        size (str): Tamaño de fuente (ej: "16px", "18px", "20px", "24px")
    """
    
    st.markdown(f"""
    <style>
        /* Configuración global de fuentes */
        .stApp {{
            font-size: {size} !important;
        }}
        
        /* Títulos principales */
        .main-header h1 {{
            font-size: 2.5rem !important;
            font-weight: bold;
        }}
        
        .main-header p {{
            font-size: 1.2rem !important;
        }}
        
        /* Headers de secciones */
        h1, h2, h3 {{
            font-size: 1.8rem !important;
            font-weight: 600;
        }}
        
        /* Texto general */
        .stMarkdown {{
            font-size: {size} !important;
        }}
        
        /* Labels de widgets */
        label {{
            font-size: calc({size} * 0.9) !important;
        }}
        
        /* Botones */
        .stButton > button {{
            font-size: calc({size} * 0.9) !important;
            font-weight: 500;
        }}
        
        /* Métricas */
        .stMetric {{
            font-size: calc({size} * 0.9) !important;
        }}
        
        /* Campos de texto */
        .stTextInput input {{
            font-size: calc({size} * 0.9) !important;
        }}
        
        /* Selectores */
        .stSelectbox select {{
            font-size: calc({size} * 0.9) !important;
        }}
        
        /* Checkboxes */
        .stCheckbox label {{
            font-size: calc({size} * 0.9) !important;
        }}
        
        /* Sliders */
        .stSlider label {{
            font-size: calc({size} * 0.9) !important;
        }}
    </style>
    """, unsafe_allow_html=True)

def show_font_controls():
    """
    Muestra controles para cambiar el tamaño de fuente
    """
    
    st.sidebar.markdown("### 🎨 Configuración de Fuente")
    
    font_size = st.sidebar.selectbox(
        "Tamaño de fuente",
        options=["14px", "16px", "18px", "20px", "22px", "24px"],
        index=2,  # 18px por defecto
        help="Selecciona el tamaño de fuente para toda la aplicación"
    )
    
    if st.sidebar.button("🔄 Aplicar Tamaño de Fuente"):
        apply_font_size(font_size)
        st.sidebar.success(f"✅ Tamaño de fuente cambiado a {font_size}")
    
    # Mostrar información sobre el tamaño actual
    st.sidebar.markdown(f"**Tamaño actual:** {font_size}")
    
    # Aplicar el tamaño seleccionado automáticamente
    apply_font_size(font_size)

if __name__ == "__main__":
    st.title("🎨 Configurador de Tamaño de Fuente")
    st.write("Este script te permite cambiar el tamaño de fuente de tu aplicación Streamlit.")
    
    show_font_controls()
    
    st.markdown("---")
    st.markdown("### 📋 Cómo usar:")
    st.markdown("1. Selecciona el tamaño de fuente deseado")
    st.markdown("2. Haz clic en 'Aplicar Tamaño de Fuente'")
    st.markdown("3. El cambio se aplicará inmediatamente")
    
    st.markdown("### 💡 Tamaños recomendados:")
    st.markdown("- **14px**: Para pantallas pequeñas o mucha información")
    st.markdown("- **16px**: Tamaño estándar, buena legibilidad")
    st.markdown("- **18px**: Tamaño grande, excelente legibilidad")
    st.markdown("- **20px+**: Para presentaciones o pantallas grandes")
