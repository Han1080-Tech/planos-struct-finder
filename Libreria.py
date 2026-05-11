"""
====================================================================
=  PROYECTO 3                                                      =
=  DESARROLLO DE UNA LIBRERIA EN PYTHON PARA LA DETECCION DE       =
=  LINEAS, ESQUINAS E INTERSECCIONES EN PLANOS ARQUITECTONICOS     =
=                                                                  =
= Este proyecto es un detector de lineas y bordes en imagenes de   = 
= planos arquitectonicos, usa funciones de OpenCV para el          =
= procesamiento de la imagen, y esta organizado en una clase para  =
= facilitar su uso, ademas de tener un codigo limpio y facil de    =
= entender, el usuario solo tiene que cambiar el nombre del archivo= 
= de imagen que quiere analizar y ejecutar el script para ver los  =
= resultados.                                                      =
====================================================================
  INTEGRANTES:
  - HAN APESS ESPARZA
  - ARMANDO DUARTE ESPARZA
  - IKER EDUARDO FIGUEROA GARCIA
  - JOSE IVAN RODRIGUEZ VALTIERRA                                                  
"""

import cv2
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import messagebox
from vision.deteccion import ProcesadorPlanos

# ==========================================================
# 1. CONFIGURACION DE USUARIO (Cambia el nombre aqui)
# Solo debes de cambiar el # al archivu que quieras ver de ejemplo
# Asegurate que los otros tres ARCHIVO_DDE_IMAGEN esten comentados para evitar confusiones, 
# y que el que quieras usar este sin comentar
# ==========================================================
ARCHIVO_DE_IMAGEN = "Plano_1.png"                         #= <-- Cambia el # ddependiendo del plano que quieras analizar
#ARCHIVO_DE_IMAGEN = "Plano_2.jpg"   
#ARCHIVO_DE_IMAGEN = "Plano_3.jpg"   
#ARCHIVO_DE_IMAGEN = "Plano_4.png"   
# ==========================================================

#Crear pantalla de error personalizada para mostrar mensajes de error de forma mas amigable y como solucionarlo
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