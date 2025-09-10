#!/usr/bin/env python3
"""
Script de verificación para TRACE
Verifica que todas las dependencias estén instaladas correctamente
"""

import sys
import importlib
import subprocess

def verificar_python():
    """Verifica la versión de Python"""
    version = sys.version_info
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("⚠️  Advertencia: Se recomienda Python 3.8 o superior")
        return False
    return True

def verificar_dependencia(nombre, import_name=None):
    """Verifica si una dependencia está instalada"""
    if import_name is None:
        import_name = nombre
    
    try:
        importlib.import_module(import_name)
        print(f"✓ {nombre}")
        return True
    except ImportError:
        print(f"✗ {nombre} - NO INSTALADO")
        return False

def verificar_dependencias():
    """Verifica todas las dependencias principales"""
    print("\n🔍 Verificando dependencias...")
    
    dependencias = [
        ("streamlit", "streamlit"),
        ("requests", "requests"),
        ("faster-whisper", "faster_whisper"),
        ("torch", "torch"),
        ("torchaudio", "torchaudio"),
        ("numpy", "numpy"),
        ("librosa", "librosa"),
        ("soundfile", "soundfile"),
    ]
    
    todas_instaladas = True
    for nombre, import_name in dependencias:
        if not verificar_dependencia(nombre, import_name):
            todas_instaladas = False
    
    return todas_instaladas

def verificar_archivos():
    """Verifica que los archivos necesarios existan"""
    print("\n📁 Verificando archivos...")
    
    archivos_requeridos = [
        "app.py",
        "custom_styles.css",
        "requirements.txt",
        "images/logo.jpeg"
    ]
    
    import os
    todos_presentes = True
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            print(f"✓ {archivo}")
        else:
            print(f"✗ {archivo} - NO ENCONTRADO")
            todos_presentes = False
    
    return todos_presentes

def main():
    """Función principal de verificación"""
    print("🎵 TRACE - Verificador de Instalación")
    print("=" * 40)
    
    # Verificar Python
    python_ok = verificar_python()
    
    # Verificar archivos
    archivos_ok = verificar_archivos()
    
    # Verificar dependencias
    deps_ok = verificar_dependencias()
    
    print("\n" + "=" * 40)
    print("📊 RESUMEN:")
    print(f"Python: {'✓' if python_ok else '✗'}")
    print(f"Archivos: {'✓' if archivos_ok else '✗'}")
    print(f"Dependencias: {'✓' if deps_ok else '✗'}")
    
    if python_ok and archivos_ok and deps_ok:
        print("\n🎉 ¡Todo está listo! Puedes ejecutar la aplicación con:")
        print("   streamlit run app.py")
        return True
    else:
        print("\n⚠️  Hay problemas que resolver antes de ejecutar la aplicación.")
        if not deps_ok:
            print("   Instala las dependencias con: pip install -r requirements.txt")
        return False

if __name__ == "__main__":
    main()
