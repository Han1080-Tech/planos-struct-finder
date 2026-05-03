
# VISION ARQUITECTONICA

Análisis estructural de planos mediante Visión Artificial.

Architectural floor plan analysis using Computer Vision.





## 📝 Descripción / Description

ES: Esta librería permite procesar planos arquitectónicos escaneados para corregir su inclinación, eliminar ruido (muebles, cotas, texto) y detectar automáticamente los muros y esquinas estructurales.

EN: This library processes scanned architectural plans to correct tilt, remove noise (furniture, dimensions, text), and automatically detect structural walls and corners.

## Versión necesaria de Pyhton / Required version of Python

3.12+

## 🚀 Instalación/Installation

ES: Para instalar la librería de forma local, clona este repositorio y ejecuta:

EN: To install the library locally, clone this repository and run:

```bash
pip install -e .
```
    
## 💻 Cómo usar / How to use

ES: Para que el programa encuentre tus imágenes sin errores, organiza tus archivos así:

EN: To ensure the program finds your images without errors, organize your files as follows:

```
nombre-de-tu-proyecto/ 
name-of-your-proyect/

    ├── src/

    │   └── vision/             <-- Código base (No tocar / Do not touch)

    ├── mi_analisis.py           <-- Tu script (Crea este archivo / Create this file)

    └── mi_plano.png             <-- Tu imagen (Ponla aquí / Place it here)

```

### Nota / Note:

ES: Los nombres mi_analisis.py y mi_plano.png son ejemplos; puedes usar los nombres que prefieras. Además, puedes usar formatos como .png, .jpg, .jpeg, .webp, .bmp o .tiff.

EN: The names mi_analisis.py and mi_plano.png are examples; you can use any name you like. You can also use formats such as .png, .jpg, .jpeg, .webp, .bmp, or .tiff.

## Ejemplo de Uso / Usage Example

ES: Copia este código en tu archivo mi_analisis.py. Está diseñado para detectar automáticamente la ruta de tu imagen:

EN: Copy this code into your mi_analisis.py file. It is designed to automatically detect your image path:

```
import vision
mport cv2
import os

# CONFIGURACIÓN / SETTINGS
NOMBRE_IMAGEN = "mi_plano.png" 

# LÓGICA AUTOMÁTICA / AUTOMATIC LOGIC 
base_path = os.path.dirname(os.path.abspath(__file__))
ruta_final = os.path.join(base_path, NOMBRE_IMAGEN)

try:
    recto, limpia = vision.preparar_plano(ruta_final)
    resultado = vision.detectar_caracteristicas(limpia, recto)

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

