# Resultados

Esta carpeta contiene todos los resultados de experimentos y modelos finales.

## Estructura

### `experiments/`
Resultados de experimentos organizados por fecha y variable:

#### `Previo a muestras adicionales/`
- Resultados con el dataset original
- Organizados por variable de evaluación

#### `Posterior a muestras adicionales/`
- Resultados con datos adicionales
- Comparaciones de rendimiento

### `final/`
- Modelos finales entrenados
- Resultados consolidados
- Métricas de rendimiento final

## Tipos de Archivos

- **`resultados_*.xlsx`**: Resultados de experimentos TF-IDF + modelos tradicionales
- **`resultados_embeddings_*.xlsx`**: Resultados de experimentos con embeddings semánticos
- **`resultados_lora_*.xlsx`**: Resultados de fine-tuning con LoRA

## Métricas Incluidas

- Accuracy, Precision, Recall, F1-Score
- PR-AUC (Precision-Recall Area Under Curve)
- Matrices de confusión
- Thresholds óptimos
- Configuraciones de hiperparámetros
