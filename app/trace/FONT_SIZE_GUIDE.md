# 🎨 Guía para Cambiar el Tamaño de Fuente

## 🚀 **Métodos Disponibles**

### **Método 1: CSS Personalizado (Recomendado)**

El archivo `app.py` ya incluye CSS personalizado que cambia el tamaño de fuente. Puedes modificar estos valores:

```css
/* En app.py, línea ~20 */
.stApp {
    font-size: 18px !important;  /* Cambia este valor */
}
```

**Tamaños disponibles:**
- `14px` - Pequeño, para pantallas pequeñas
- `16px` - Estándar, buena legibilidad
- `18px` - Grande, excelente legibilidad (actual)
- `20px` - Muy grande, para presentaciones
- `24px` - Extra grande, para pantallas grandes

### **Método 2: Archivo de Configuración**

El archivo `.streamlit/config.toml` permite configurar el tema global:

```toml
[theme]
fontSize = "18px"  # Cambia este valor
```

### **Método 3: Script Interactivo**

Usa el archivo `apply_font_size.py` para cambiar el tamaño dinámicamente:

```bash
streamlit run apply_font_size.py
```

## 🔧 **Cambios Rápidos**

### **Para hacer la fuente más pequeña:**
```css
.stApp {
    font-size: 16px !important;
}
```

### **Para hacer la fuente más grande:**
```css
.stApp {
    font-size: 20px !important;
}
```

### **Para hacer solo los títulos más grandes:**
```css
h1, h2, h3 {
    font-size: 2.2rem !important;  /* Aumenta de 1.8rem */
}
```

## 📱 **Tamaños Recomendados por Uso**

| Uso | Tamaño Recomendado | Razón |
|-----|-------------------|-------|
| **Pantallas pequeñas** | 14px | Ahorra espacio |
| **Uso general** | 16px | Balance perfecto |
| **Presentaciones** | 18px | Excelente legibilidad |
| **Accesibilidad** | 20px+ | Para usuarios con problemas de vista |
| **Pantallas grandes** | 22px+ | Aprovecha el espacio |

## 🎯 **Elementos Específicos**

### **Cambiar solo el texto del sidebar:**
```css
.css-1d391kg {
    font-size: 18px;  /* Cambia este valor */
}
```

### **Cambiar solo los botones:**
```css
.stButton > button {
    font-size: 1.1rem !important;  /* Cambia este valor */
}
```

### **Cambiar solo las métricas:**
```css
.stMetric {
    font-size: 1.1rem !important;  /* Cambia este valor */
}
```

## 🚀 **Implementación Paso a Paso**

### **Paso 1: Editar app.py**
1. Abre `app.py` en tu editor
2. Busca la sección `<style>` (línea ~20)
3. Cambia `font-size: 18px` por el tamaño deseado
4. Guarda el archivo

### **Paso 2: Reiniciar la aplicación**
```bash
# Detén la aplicación actual (Ctrl+C)
# Luego ejecuta:
streamlit run app.py
```

### **Paso 3: Verificar cambios**
- Los cambios se aplican inmediatamente
- Si no ves cambios, recarga la página del navegador

## 💡 **Consejos de Diseño**

### **Proporciones recomendadas:**
- **Texto principal**: 18px
- **Títulos**: 1.8rem (aproximadamente 29px)
- **Labels**: 16px (90% del texto principal)
- **Botones**: 16px (90% del texto principal)

### **Para mejor legibilidad:**
- Usa tamaños de 16px o mayores
- Mantén proporciones consistentes
- Considera el contraste con el fondo

## 🐛 **Solución de Problemas**

### **Los cambios no se aplican:**
1. Verifica que guardaste el archivo
2. Reinicia la aplicación Streamlit
3. Recarga la página del navegador
4. Verifica que no hay errores de sintaxis CSS

### **El texto se ve muy grande/pequeño:**
1. Ajusta gradualmente (2px a la vez)
2. Prueba diferentes tamaños
3. Considera el tamaño de tu pantalla

### **Algunos elementos no cambian:**
1. Usa `!important` en el CSS
2. Verifica que las clases CSS sean correctas
3. Algunos elementos de Streamlit pueden requerir estilos específicos

## 📋 **Ejemplos Completos**

### **Fuente pequeña (14px):**
```css
.stApp {
    font-size: 14px !important;
}

h1, h2, h3 {
    font-size: 1.6rem !important;
}

.stButton > button {
    font-size: 13px !important;
}
```

### **Fuente grande (22px):**
```css
.stApp {
    font-size: 22px !important;
}

h1, h2, h3 {
    font-size: 2.2rem !important;
}

.stButton > button {
    font-size: 20px !important;
}
```

## 🎨 **Personalización Avanzada**

### **Fuentes personalizadas:**
```css
.stApp {
    font-family: 'Arial', sans-serif !important;
    font-size: 18px !important;
}
```

### **Colores personalizados:**
```css
.stApp {
    font-size: 18px !important;
    color: #333333 !important;
}
```

### **Espaciado personalizado:**
```css
.stMarkdown {
    font-size: 18px !important;
    line-height: 1.6 !important;
}
```

¡Con estos métodos puedes personalizar completamente el tamaño de fuente de tu aplicación!
