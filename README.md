
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

ES: Para instalar la librería de forma local, sigue estos pasos:
EN: To install the library locally, follow these steps:

1. Clonar el repositorio / Clone the repository:
```bash
git clone https://github.com/Han1080-Tech/planos-struct-finder.git
```
ES: Activa un entorno virtual para mantener las dependencias aisladas.

EN: It is essential to activate a virtual environment to keep dependencies isolated.

2. Crear el entorno / Create environment:
```bash
python -m venv .venv
```
3. Activar el entorno / Activate environment:
```bash
.\.venv\Scripts\activate
```
### 💡 Nota para usuarios de Spyder:
Para que la librería funcione correctamente, debes vincular el entorno virtual del proyecto:

Ve a Tools -> Preferences -> Python interpreter.

Selecciona Use the following Python interpreter.

Busca la ruta de tu carpeta: planos-struct-finder/.venv/Scripts/python.exe.

Reinicia la consola de Spyder.

### 💡 Note for Spyder users:
To ensure the library works correctly, you must link the project's virtual environment:

Go to Tools -> Preferences -> Python interpreter.

Select Use the following Python interpreter.

Browse to your project folder and select the environment's executable: planos-struct-finder/.venv/Scripts/python.exe.

Restart the Spyder console.

4. Entrar a la carpeta (¡IMPORTANTE!) / Enter the folder (IMPORTANT!):

```bash

cd planos-struct-finder
```

5. Instalar en modo ejecutable / Install in editable mode:
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
<img src="https://github.com/user-attachments/assets/c4ff78ad-3e4b-4a79-a539-bff92d9e5267" width="600">

### Nota / Note:

ES: Los nombres mi_analisis.py y mi_plano.png son ejemplos; puedes usar los nombres que prefieras. Además, puedes usar formatos como .png, .jpg, .jpeg, .webp, .bmp o .tiff.

EN: The names mi_analisis.py and mi_plano.png are examples; you can use any name you like. You can also use formats such as .png, .jpg, .jpeg, .webp, .bmp, or .tiff.

## Ejemplo de Uso / Usage Example

ES: Copia este código en tu archivo mi_analisis.py. Está diseñado para detectar automáticamente la ruta de tu imagen:

EN: Copy this code into your mi_analisis.py file. It is designed to automatically detect your image path:

### ES: (Cambia el nombre de la imagen si es necesario)
### EN: (Change the image name if necessary)

```
import cv2
import matplotlib.pyplot as plt
import os
import tkinter as tk
import os
from tkinter import messagebox
from vision.deteccion import ProcesadorPlanos

# Esto detecta automáticamente la carpeta donde está guardado este script
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))

# ==========================================================
# 1. CONFIGURACION DE USUARIO (Cambia el nombre aqui)
# No necesitas cambiar nada mas, el codigo esta diseñado para 
# ser lo mas automatico posible, solo asegurate de que el nombre 
# del archivo sea correcto y que la imagen este en la misma 
# carpeta que este script   
# ==========================================================
NOMBRE_IMAGEN = "Plano_4.png"                         #= <-- Cambia el nombre del archivo de imagen aqui (ejemplo: "Plano_1.png")
# ==========================================================

ARCHIVO_DE_IMAGEN = os.path.join(DIRECTORIO_ACTUAL, NOMBRE_IMAGEN)
#Crear pantalla de error personalizada para mostrar mensajes de error de forma mas amigable y como solucionarlo
if not os.path.exists(ARCHIVO_DE_IMAGEN):
    def mostrar_error(mensaje):
        root = tk.Tk()
        root.withdraw() 
        messagebox.showerror("Error de Archivo", mensaje)
        root.destroy()

def ejecutar_analisis():
    # Verificar si el archivo existe
    if not os.path.exists(ARCHIVO_DE_IMAGEN):
        mensaje = (f"No se encontro la imagen: '{ARCHIVO_DE_IMAGEN}'\n\n"
                   "Por favor, revisa:\n"
                   "1. Que el nombre este bien escrito.\n"
                   "2. Que la imagen este en la misma carpeta que este script.\n"
                   "3. Que la extension sea la correcta.")
        mostrar_error(mensaje)
        return

    try:
        # Procesamiento de la imagen usando la clase ProcesadorPlanos, esto hace que el codigo principal sea mas limpio
        procesador = ProcesadorPlanos(ARCHIVO_DE_IMAGEN)
        final = procesador.ejecutar()

        # Configurar la ventana de visualización
        fig = plt.figure(figsize=(10, 10))
        
        # Título de la ventana
        fig.canvas.manager.set_window_title(f"Visualizador de Planos: {ARCHIVO_DE_IMAGEN}")
        
        # Enseñar la imagen procesada con un título que incluya el nombre del archivo
        plt.imshow(cv2.cvtColor(final, cv2.COLOR_BGR2RGB))
        plt.title(f"IMAGEN PROCESADA CON LOS BORDES Y ESQUINAS", fontsize=18, fontweight='bold', color='Purple')
        plt.axis('off')
        plt.show()
        

    except Exception as e:
        mostrar_error(f"Ocurrio un error inesperado al procesar la imagen:\n{str(e)}")

if __name__ == "__main__":
    ejecutar_analisis()
```

⏳ ES: Nota sobre el tiempo de carga
Al abrir el proyecto por primera vez, es normal que tu editor (VS Code/Spyder) muestre advertencias o subrayados en el código. Esto se debe a que las librerías de visión artificial (opencv, numpy) son pesadas y el sistema está terminando de indexarlas. No te preocupes, el programa funcionará correctamente una vez finalizada la configuración inicial.

⏳ EN: Note on Loading Time
When opening the project for the first time, your editor (VS Code/Spyder) might show warnings or underlines in the code. This is normal, as computer vision libraries (opencv, numpy) are large, and the system is finishing their indexing. Do not worry; the program will work correctly once the initial setup is complete.


### ES: Solución de Problemas (Pantalla Emergente)
Si el sistema no logra detectar la imagen, se desplegará automáticamente un asistente visual que te sugerirá lo siguiente:

Ubicación: Verifica que la imagen esté en el mismo directorio que el script de pruebas.

Sintaxis: Asegúrate de que el nombre esté escrito exactamente igual en el código (respetando mayúsculas y guiones).

Existencia: Confirma que el archivo realmente existe y no ha sido movido o borrado.

### EN:Troubleshooting (Popup Window)
If the system fails to detect the image, a visual assistant will automatically appear, suggesting the following:

Location: Verify that the image is in the same directory as the test script.

Syntax: Ensure the filename is written exactly as it appears in the code (respecting case and hyphens).

Existence: Confirm that the file actually exists and hasn't been moved or deleted.

<img src="https://github.com/user-attachments/assets/21feb454-d780-4faf-b341-bab20e43f68b" width="600">

## 📊 Resultados / Results 

ES:
### 🧪 Cómo probar los ejemplos incluidos
Para demostrar la versatilidad de la librería, hemos incluido 4 ejemplos de procesamiento. Estos archivos se encuentran dentro del paquete para pruebas inmediatas.

1. Abre el archivo Libreria.py que se encuentra dentro de planos-struct-finder.

2. En la sección de rutas (esta marcado con un comentario que es lo unico que debes modificar.) asegúrate de que solo una línea no tenga el símbolo #.

3. Guarda el archivo y ejecuta: python Libreria.py.

EN:
### 🧪 How to test the included examples
To demonstrate the library's versatility, we have included 3 processing examples. These files are included within the package for immediate testing.

1. Open the Libreria.py file which is found within planes-struct-finder..

2. In the paths section (This is marked with a comment, which is the only thing you need to modify.) ensure that only one line does not have the # symbol.

3. Save the file and run: python Libreria.py.

### Ejemplo / Example 1:
<img src="https://github.com/user-attachments/assets/fe09e972-049a-44e7-a73d-c67ee2330a78" width="600">

### Ejemplo / Example 2:
<img src="https://github.com/user-attachments/assets/bc1b9a89-d6e3-4649-a6da-bfd5765b1173" width="600">

### Ejemplo / Example 3:
<img src="https://github.com/user-attachments/assets/db38553e-1a44-43c5-9237-1a8714e72e49" width="600">

### Ejemplo / Example 4:
<img src="https://github.com/user-attachments/assets/b1c814c6-0388-4e56-be66-4c61e8324d7f" width="600">

## 👥 Equipo / Team

Han Apess Esparza

Armando Duarte Esparza

Iker Eduardo Figueroa Garcia

Jose Ivan Rodriguez Valtierra

- [@Han1080-Tech](https://github.com/Han1080-Tech)

