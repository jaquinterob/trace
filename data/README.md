# Datos

Esta carpeta contiene todos los datasets utilizados en el proyecto.

## Estructura

### `raw/`
Datos originales sin procesar:
- **`Wolkbox_Bootcamp.xlsx`**: Dataset original de evaluación de llamadas
- **`Wolkbox_Bootcamp_Adicionales.xlsx`**: Dataset con muestras adicionales
- **`Transcripciones_Variables.xlsx`**: Transcripciones combinadas con variables
- **`Transcripciones_Variables_Adicionales.xlsx`**: Transcripciones con datos adicionales

### `processed/`
Datos procesados y listos para entrenamiento (se generan automáticamente)

## Descripción

Los datasets contienen:
- Transcripciones de llamadas de cobranza
- Variables de evaluación (0: Cumple, 1: No cumple)
- Metadatos de las llamadas (duración, agente, fecha, etc.)
- IDs de conexión para unir transcripciones con evaluaciones
