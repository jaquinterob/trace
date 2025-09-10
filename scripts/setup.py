#!/usr/bin/env python3
"""
Script de configuración inicial para el proyecto Trace
Sistema de Clasificación de Llamadas de Cobranza
"""

import os
import sys
from pathlib import Path

def create_directories():
    """Crea las carpetas necesarias para el proyecto"""
    directories = [
        "data/raw",
        "data/processed", 
        "models",
        "results/experiments",
        "results/final",
        "scripts",
        "utils",
        "docs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Creada carpeta: {directory}")

def check_requirements():
    """Verifica si las dependencias están instaladas"""
    try:
        import pandas
        import numpy
        import sklearn
        import transformers
        print("✓ Dependencias principales encontradas")
        return True
    except ImportError as e:
        print(f"✗ Faltan dependencias: {e}")
        print("Ejecuta: pip install -r requirements.txt")
        return False

def main():
    """Función principal de configuración"""
    print("🚀 Configurando proyecto Trace...")
    print("=" * 50)
    
    # Crear directorios
    print("\n📁 Creando estructura de directorios...")
    create_directories()
    
    # Verificar dependencias
    print("\n🔍 Verificando dependencias...")
    deps_ok = check_requirements()
    
    print("\n" + "=" * 50)
    if deps_ok:
        print("✅ Configuración completada exitosamente!")
        print("\nPróximos pasos:")
        print("1. Coloca tus archivos de datos en data/raw/")
        print("2. Ejecuta los notebooks en notebooks/data_processing/")
        print("3. Continúa con notebooks/model_training/")
    else:
        print("⚠️  Configuración completada con advertencias")
        print("Instala las dependencias faltantes antes de continuar")

if __name__ == "__main__":
    main()
