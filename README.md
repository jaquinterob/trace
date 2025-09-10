# Trace - Sistema de Clasificación de Llamadas de Cobranza

## 📊 Presentación del Proyecto

**Presentación Final**: [Ver presentación en Canva](https://www.canva.com/design/DAGycW-VCJk/3pUOEWG36dACDwjP1hlQhQ/edit?utm_content=DAGycW-VCJk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

La presentación incluye:
- Resumen ejecutivo del proyecto
- Metodologías implementadas
- Resultados obtenidos
- Conclusiones y recomendaciones
- Demostración del sistema

---

## Descripción del Proyecto

**Trace** es un sistema de inteligencia artificial diseñado para analizar y clasificar automáticamente llamadas de cobranza basándose en transcripciones de audio. El proyecto utiliza técnicas avanzadas de procesamiento de lenguaje natural (NLP) y machine learning para evaluar la calidad de las llamadas según diferentes criterios de evaluación.

## Objetivo

El sistema tiene como objetivo automatizar la evaluación de llamadas de cobranza mediante la clasificación de diferentes variables de calidad, permitiendo identificar si los agentes cumplen con los estándares establecidos en cada interacción.

## Variables de Clasificación

El sistema evalúa las siguientes variables en las llamadas:

1. **1.1 Apertura de Llamada** - Evalúa si el agente realiza una apertura adecuada
2. **2.2 Alternativas de acuerdo a la necesidad** - Verifica si se ofrecen alternativas apropiadas
3. **4.1 Condiciones de incumplimiento** - Analiza si se explican las condiciones de incumplimiento
4. **4.2 Explica medios de pago** - Evalúa si se explican los medios de pago disponibles

## Estructura del Proyecto

```
trace/
├── data/                                           # Datos del proyecto
│   ├── raw/                                        # Datos originales
│   │   ├── Wolkbox_Bootcamp.xlsx
│   │   ├── Wolkbox_Bootcamp_Adicionales.xlsx
│   │   ├── Transcripciones_Variables.xlsx
│   │   └── Transcripciones_Variables_Adicionales.xlsx
│   └── processed/                                  # Datos procesados
├── notebooks/                                      # Notebooks de análisis
│   ├── data_processing/                           # Procesamiento de datos
│   │   ├── Dataset_Transcripción_Audios.ipynb
│   │   └── Transcripción_Audio_Formato_GSM.ipynb
│   ├── model_training/                            # Entrenamiento de modelos
│   │   ├── Clasificación_llamadas.ipynb
│   │   └── Lora.ipynb
│   ├── analysis/                                   # Análisis exploratorio
│   │   ├── Variable_ Condiciones de incumplimiento.ipynb
│   │   ├── Variable_ Condiciones de incumplimiento_+_Incremento_Clase_Minoritaria.ipynb
│   │   ├── Variable_ alternativas de acuerdo a la necesidad.ipynb
│   │   └── Variable_ alternativas de acuerdo a la necesidad_+_Incremento_Clase_Minoritaria.ipynb
│   └── experiments/                                # Experimentos adicionales
├── results/                                        # Resultados
│   ├── experiments/                               # Resultados de experimentos
│   └── final/                                     # Modelos y resultados finales
├── models/                                         # Modelos entrenados
├── scripts/                                        # Scripts de utilidad
├── utils/                                          # Funciones auxiliares
├── docs/                                           # Documentación adicional
└── README.md                                       # Este archivo
```

## Tecnologías Utilizadas

- **Python 3.x**
- **Pandas** - Manipulación de datos
- **NumPy** - Cálculos numéricos
- **Scikit-learn** - Machine learning tradicional
- **Transformers (Hugging Face)** - Modelos de lenguaje
- **PEFT (Parameter Efficient Fine-Tuning)** - Fine-tuning eficiente con LoRA
- **Sentence Transformers** - Embeddings semánticos
- **Faster-Whisper** - Transcripción de audio
- **LightGBM** - Algoritmos de gradient boosting
- **Matplotlib/Seaborn** - Visualización de datos

## Metodologías Implementadas

### 1. Procesamiento de Audio
- Transcripción automática de archivos de audio en formato GSM
- Conversión a texto usando Faster-Whisper
- Preprocesamiento y limpieza de transcripciones

### 2. Clasificación de Texto
- **TF-IDF + Modelos Tradicionales**: Logistic Regression, SVM, Random Forest
- **Embeddings Semánticos**: Sentence Transformers con múltiples modelos
- **Fine-tuning con LoRA**: Adaptación eficiente de modelos pre-entrenados
- **Técnicas de Balanceo**: SMOTE, Random Oversampling, Tomek Links

### 3. Optimización de Modelos
- Tuning de umbrales basado en F1-score
- Validación cruzada estratificada
- Métricas de evaluación comprehensivas (Precision, Recall, F1, PR-AUC)

## Cómo Ejecutar los Notebooks

### Prerrequisitos

1. **Instalar dependencias**:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
pip install transformers datasets peft accelerate
pip install sentence-transformers lightgbm
pip install faster-whisper librosa
pip install imbalanced-learn
```

2. **Configurar Google Colab** (si se ejecuta en Colab):
   - Montar Google Drive
   - Asegurar acceso a los archivos de datos

### Orden de Ejecución Recomendado

1. **Transcripción de Audio** (`Transcripción_Audio_Formato_GSM.ipynb`)
   - Procesa archivos de audio GSM
   - Genera transcripciones de texto
   - Calcula duración de llamadas

2. **Preparación de Dataset** (`Dataset_Transcripción_Audios.ipynb`)
   - Combina transcripciones con variables de evaluación
   - Limpia y prepara datos para entrenamiento

3. **Análisis Exploratorio** (Notebooks de variables específicas)
   - Explora distribuciones de clases
   - Genera visualizaciones
   - Identifica patrones en los datos

4. **Entrenamiento de Modelos** (`Clasificación_llamadas.ipynb`)
   - Experimentos con TF-IDF + modelos tradicionales
   - Experimentos con embeddings semánticos
   - Comparación de técnicas de balanceo

5. **Fine-tuning Avanzado** (`Lora.ipynb`)
   - Entrenamiento con LoRA para modelos de lenguaje
   - Optimización de hiperparámetros
   - Exportación de modelos finales

### Configuración de Datos

Los notebooks esperan los siguientes archivos en Google Drive:
- `Wolkbox_Bootcamp_Adicionales.xlsx` - Dataset de evaluación
- `transcripciones_gsm_adicionales.csv` - Transcripciones de audio
- Carpeta con archivos de audio `.gsm`

### Variables de Entorno

Para deshabilitar logging de WandB:
```python
import os
os.environ["WANDB_DISABLED"] = "true"
os.environ["WANDB_MODE"] = "disabled"
```

## Resultados y Modelos

El sistema genera varios tipos de salidas:

1. **Métricas de Evaluación**: Excel con resultados detallados de todos los experimentos
2. **Modelos Entrenados**: Archivos `.joblib` con los mejores modelos
3. **Configuraciones LoRA**: Adaptadores para fine-tuning eficiente
4. **Visualizaciones**: Gráficos de distribución, wordclouds, matrices de confusión

## Métricas de Evaluación

- **Accuracy**: Precisión general
- **F1-Score**: Balance entre precision y recall
- **Precision/Recall**: Por clase (0: Cumple, 1: No cumple)
- **PR-AUC**: Área bajo la curva Precision-Recall
- **Matriz de Confusión**: Detalles de clasificaciones correctas/incorrectas

## Contribuciones

Este proyecto forma parte de un bootcamp de análisis de llamadas de cobranza y representa un caso de uso real de aplicación de IA en el sector financiero.

## Notas Técnicas

- Los modelos están optimizados para texto en español
- Se utilizan técnicas de balanceo para manejar clases desbalanceadas
- El sistema es escalable y puede adaptarse a nuevas variables de evaluación
- Los modelos exportados pueden integrarse en sistemas de producción

## Contacto

Para consultas sobre el proyecto o colaboraciones, contactar al equipo de desarrollo.
