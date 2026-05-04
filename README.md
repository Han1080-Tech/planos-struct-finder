
# VISION ARQUITECTONICA

Análisis estructural de planos mediante Visión Artificial.

Architectural floor plan analysis using Computer Vision.

## 📝 Descripción / Description

ES: Esta librería permite procesar planos arquitectónicos escaneados para corregir su inclinación, eliminar ruido (muebles, cotas, texto) y detectar automáticamente los muros y esquinas estructurales.

EN: This library processes scanned architectural plans to correct tilt, remove noise (furniture, dimensions, text), and automatically detect structural walls and corners.

## 🛠️ Requisitos Previos / Prerequisites
#### ES: 

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

Git: Necesario para clonar el repositorio y gestionar las versiones del proyecto. Puedes descargarlo en git-scm.com.

Python 3.12+: El lenguaje base utilizado para el desarrollo de esta librería de visión artificial.

Editor de código: Se recomienda Visual Studio Code para una mejor experiencia de desarrollo.

#### EN: 

Before starting, make sure you have the following installed on your system:

Git: Required to clone the repository and manage project versions. Download it at git-scm.com.

Python 3.12+: The base language used for this computer vision library.

Code Editor: Visual Studio Code is recommended for the best development experience.
#### 

ES: Puedes verificar que tienes todo listo ejecutando estos comandos en tu terminal:

EN: You can verify everything is ready by running these commands in your terminal:

```bash
git --version
python --version
```
## 🚀 Instalación/Installation

ES: Para instalar la librería de forma local, clona este repositorio, sigue estos pasos:
EN: To install the library locally, clone this repository, follow these steps:

1. Clonar el repositorio / Clone the repository:
```bash
git clone https://github.com/Han1080-Tech/planos-struct-finder.git
```

2. Entrar a la carpeta (¡IMPORTANTE!) / Enter the folder (IMPORTANT!):

```bash
cd planos-struct-finder
```
ES: Una vez dentro de la carpeta, es fundamental activar un entorno virtual para mantener las dependencias aisladas.

EN: Once inside the folder, it is essential to activate a virtual environment to keep dependencies isolated.

1. Crear el entorno / Create environment:
```bash
python -m venv .venv
```
2. Activar el entorno / Activate environment:
```bash
.\.venv\Scripts\activate
```
3. Instalar en modo ejecutable / Install in editable mode:
```bash
pip install -e .
```
    
## 💻 Cómo usar / How to use


ES: Para que el programa encuentre tus imágenes sin errores, organiza tus archivos así:

EN: To ensure the program finds your images without errors, organize your files as follows:

```
nombre-de-tu-proyecto/ 
name-of-your-proyect/

    ├── planos-struct-finder

    │   └── vision/             <-- Código base (No tocar / Do not touch)

    ├── mi_analisis.py           <-- Tu script (Crea este archivo / Create this file)

    └── mi_plano.png             <-- Tu imagen (Ponla aquí / Place it here)

```
<img src="https://github.com/user-attachments/assets/f3bd5a2f-6f61-4059-a3c0-f7c275e26c3f" width="600">

### Nota / Note:

ES: Los nombres mi_analisis.py y mi_plano.png son ejemplos; puedes usar los nombres que prefieras. Además, puedes usar formatos como .png, .jpg, .jpeg, .webp, .bmp o .tiff.

EN: The names mi_analisis.py and mi_plano.png are examples; you can use any name you like. You can also use formats such as .png, .jpg, .jpeg, .webp, .bmp, or .tiff.

## Ejemplo de Uso / Usage Example

ES: Copia este código en tu archivo mi_analisis.py. Está diseñado para detectar automáticamente la ruta de tu imagen:

EN: Copy this code into your mi_analisis.py file. It is designed to automatically detect your image path:

```
import vision
import cv2
import os

# CONFIGURACIÓN / SETTINGS
# Cambia el nombre de la imagen que deseas analizar / Change the name of the image you want to analyze
NOMBRE_IMAGEN = "Plano_Casa.jpg"  

# LÓGICA AUTOMÁTICA / AUTOMATIC LOGIC 
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_final = os.path.join(base_path, NOMBRE_IMAGEN)

try:
    recto, limpia = vision.preparar_plano(ruta_final)
    resultado = vision.detectar_caracteristicas(recto, limpia)

    print(f"✅ Analizando / Analizing : {NOMBRE_IMAGEN}")
    cv2.imshow('Deteccion Estructural - Vision Artificial', resultado)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"❌ Error: No se pudo procesar / Error: Could not be processed '{NOMBRE_IMAGEN}'. \nDetalle: {e}")
```

## 📊 Resultados / Results 

ES:
### 🧪 Cómo probar los ejemplos incluidos
Para demostrar la versatilidad de la librería, hemos incluido 3 ejemplos de procesamiento. Estos archivos se encuentran dentro del paquete para pruebas inmediatas.

1. Abre el archivo Libreria.py.

2. En la sección de rutas (esta marcado con un comentario que es lo unico que debes modificar.) asegúrate de que solo una línea no tenga el símbolo #.

3. Guarda el archivo y ejecuta: python Libreria.py.

EN:
### 🧪 How to test the included examples
To demonstrate the library's versatility, we have included 3 processing examples. These files are included within the package for immediate testing.

1. Open the Libreria.py file.

2. In the paths section (This is marked with a comment, which is the only thing you need to modify.) ensure that only one line does not have the # symbol.

3. Save the file and run: python Libreria.py.

### Ejemplo / Example 1:
<img src="https://github.com/user-attachments/assets/cd58dd7f-d05a-4065-9e1c-4482341d42a9" width="600">

### Ejemplo / Example 2:
<img src="https://github.com/user-attachments/assets/0de732b2-50af-4b2a-af70-5f8e8c974c1d" width="600">

### Ejemplo / Example 3:
<img src="https://github.com/user-attachments/assets/429604ba-5b28-43a0-97e7-ce05679986c9" width="600">

## 👥 Equipo / Team

Han Apess Esparza

Armando Duarte Esparza

Iker Eduardo Figueroa Garcia

Jose Ivan Rodriguez Valtierra

- [@Han1080-Tech](https://github.com/Han1080-Tech)

