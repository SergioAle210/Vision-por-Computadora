# HDT 1: Introducción a Visión por Computadora

Este repositorio contiene la primera Hoja de Trabajo (HDT1) del curso de Visión por Computadora. El proyecto se enfoca en el procesamiento básico de imágenes utilizando Python, OpenCV y Matplotlib.

##  Contenido 

El repositorio está organizado de la siguiente manera:

-   **`HDT1_Practica.ipynb`**: Notebook principal con la implementación de los ejercicios prácticos:
    -   Ajuste manual de contraste y brillo de forma vectorizada.
    -   Corrección Gamma manual.
    -   Segmentación cromática en espacio de color HSV (detección de colores específicos).
-   **`HDT1_Teoría.ipynb`**: Notebook con la resolución de problemas teóricos.
-   **`lab_semana1.py`**: Script de Python con las funciones base utilizadas en la práctica.

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto, se recomienda utilizar un entorno virtual de Python 3.13 (versión estándar).

1.  **Clonar el repositorio:**
    ```powershell
    git clone <url-del-repo>
    cd HDT1
    ```

2.  **Crear y activar el entorno virtual:**
    ```powershell
    python -m venv .hdt
    .\.hdt\Scripts\Activate.ps1
    ```

3.  **Instalar dependencias:**
    ```powershell
    pip install -r requirements.txt
    ```

## 🧠 Conceptos Implementados

### 1. Ajuste de Contraste y Brillo
Se implementó la fórmula:
$$g(x) = \alpha \cdot f(x) + \beta$$
De forma segura (clipping) y vectorizada para optimizar el rendimiento.

### 2. Corrección Gamma
Uso de la transformación de potencia para ajustar la luminancia de las imágenes:
$$V_{out} = V_{in}^{\gamma}$$

### 3. Segmentación HSV
Detección de objetos basada en color. Se implementaron filtros para:
-   **Rojo**: Manejando la naturaleza circular del canal Hue en OpenCV.
-   **Amarillo y Naranja**: Rangos personalizados para segmentación precisa.
-   **Verde y Azul**: Combinación de máscaras mediante operaciones bitwise.

## 👥 Integrantes
- Sergio Orellana 221122
- Rodrigo Mansilla 22611
- Ricardo Chuy 221007
