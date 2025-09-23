# Generador de Exámenes CEPRE-UNI

Este proyecto contiene un sistema para generar exámenes parciales para el Centro Preuniversitario de la Universidad Nacional de Ingeniería (CEPRE-UNI).

## Características principales

### ✨ Funcionalidades mejoradas
- **Preguntas completas**: Las preguntas y sus alternativas siempre se mantienen juntas en la misma página
- **Títulos optimizados**: Los títulos de secciones aparecen siempre en la parte superior de una columna
- **Formato profesional**: Layout en dos columnas con presentación mejorada
- **Generación automática**: Sistema de generación aleatoria de 4 versiones de examen (P, Q, R, S)

### 🔧 Componentes del sistema

#### `1er_parcial_cepreuni.py`
Script principal con interfaz gráfica (Tkinter) que:
- Genera automáticamente 4 versiones de examen con preguntas aleatorias
- Crea archivos LaTeX con formato optimizado
- Incluye preguntas de: Física, Química, Matemática, Razonamiento Matemático y Humanidades

#### `OCAD.sty`
Paquete LaTeX personalizado que incluye:
- Comandos matemáticos abreviados
- `\preguntacompleta{}{}{}`: Mantiene preguntas unidas en la misma página
- `\tituloseccion{}`: Posiciona títulos en la parte superior de columnas
- Configuración optimizada para exámenes

### 📁 Estructura de carpetas

```
1er_parcial_cepreuni/
├── fisica/           # Preguntas de Física
├── quimica/          # Preguntas de Química  
├── matematica/       # Preguntas de Matemática
│   ├── aritmetica/
│   ├── algebra/
│   ├── geometria/
│   └── trigonometria/
├── aptitud_academica/  # Preguntas de Razonamiento Matemático
├── humanidades/      # Preguntas de Humanidades
├── PruebaP/         # Examen versión P (con mejoras implementadas)
├── PruebaQ/         # Examen versión Q
├── PruebaR/         # Examen versión R
└── PruebaS/         # Examen versión S
```

### 🚀 Uso del sistema

1. **Ejecutar el generador**:
   ```bash
   python 1er_parcial_cepreuni.py
   ```

2. **Introducir el período** (ej: "2025-2")

3. **Generar exámenes**: El sistema creará automáticamente 4 carpetas con versiones diferentes

4. **Compilar LaTeX**: En cada carpeta generada:
   ```bash
   pdflatex PruebaX.tex
   ```

### 💡 Mejoras implementadas

#### Comando `\preguntacompleta{ruta}{archivo}{respuesta}`
- Evita que las preguntas se dividan entre páginas
- Mantiene unidas: número de pregunta + enunciado + alternativas
- Usa `\needspace` y `\samepage` para control automático

#### Comando `\tituloseccion{titulo}`
- Asegura que títulos aparezcan en la parte superior de columnas
- Fuerza salto automático si está en la mitad inferior
- Mejora significativamente la presentación del examen

### 📋 Materias incluidas
- **Física**: 6 preguntas
- **Química**: 6 preguntas  
- **Matemática**: 20 preguntas (Aritmética, Álgebra, Geometría, Trigonometría)
- **Razonamiento Matemático**: 15 preguntas
- **Humanidades**: 5 preguntas

**Total**: Aproximadamente 52 preguntas por examen

### ⚙️ Requisitos técnicos
- Python 3.x con Tkinter
- LaTeX (MiKTeX o TeX Live)
- Paquetes LaTeX: graphicx, enumerate, babel, amsmath, needspace

---

*Sistema desarrollado para la generación eficiente de exámenes parciales CEPRE-UNI con formato profesional y layout optimizado.*