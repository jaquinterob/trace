#!/usr/bin/env python3
"""
Script para generar un archivo de audio de prueba para la aplicación de transcripción
"""

import numpy as np
import soundfile as sf
import os

def generate_test_audio():
    """Genera un archivo de audio de prueba con una frase en español"""
    
    # Parámetros del audio
    sample_rate = 16000  # 16kHz para mejor compatibilidad con Whisper
    duration = 5  # 5 segundos
    
    # Generar señal de audio simple (tono sinusoidal)
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    # Crear un tono que simule habla (frecuencias variables)
    frequency = 200 + 100 * np.sin(2 * np.pi * 0.5 * t)  # Frecuencia variable
    audio = 0.3 * np.sin(2 * np.pi * frequency * t)
    
    # Agregar algo de ruido para simular audio real
    noise = 0.01 * np.random.randn(len(audio))
    audio = audio + noise
    
    # Normalizar audio
    audio = audio / np.max(np.abs(audio))
    
    # Guardar como WAV
    filename = "test_audio_espanol.wav"
    sf.write(filename, audio, sample_rate)
    
    print(f"✅ Archivo de audio de prueba generado: {filename}")
    print(f"📊 Características:")
    print(f"   - Duración: {duration} segundos")
    print(f"   - Frecuencia de muestreo: {sample_rate} Hz")
    print(f"   - Tamaño: {os.path.getsize(filename) / 1024:.1f} KB")
    print(f"")
    print(f"🎯 Este archivo se puede usar para probar la transcripción en la aplicación.")
    print(f"   Nota: Como es un tono sintético, la transcripción puede no ser perfecta,")
    print(f"   pero servirá para verificar que la funcionalidad básica funciona.")

if __name__ == "__main__":
    generate_test_audio()
