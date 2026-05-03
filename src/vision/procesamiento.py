"""
==================================================================
=  PROYECTO 3                                                    =
=  DESARROLLO DE UNA LIBRERIA EN PYTHON PARA LA DETECCION DE     =
=  LINEAS, ESQUINAS E INTERSECCIONES EN PLANOS ARQUITECTONICOS   =
=                                                                =
==================================================================
  INTEGRANTES:
  - HAN APESS ESPARZA
  - ARMANDO DUARTE ESPARZA
  - IKER EDUARDO FIGUEROA GARCIA
  - JOSE IVAN RODRIGUEZ VALTIERRA

  DESCRIPCION:
  El presente proyecto tiene como objetivo desarrollar una libreria en Python 
  que permita la detección de lineas, esquinas e intersecciones en planos arquitectonicos. 
  Esto se lograra solo usando funciones basicas de procesamiento de imágenes, 
  sin recurrir a librerias especializadas.                                                    
"""
import cv2 
import numpy as np

def Preparar_Plano(ruta):
    #Importamos la imagen y la convertimos a escala de grises
    Imagen = cv2.imread(ruta)
    Imagen_gris = cv2.cvtColor(Imagen, cv2.COLOR_BGR2GRAY)

    #Detectar bordes usando el operador de Canny
    Bordes = cv2.Canny(Imagen_gris, 150, 150)

    #Buscar las lineas usando la transformada de Hough solo para calcular el angulo de inclinacion
    lineas = cv2.HoughLinesP(Bordes, 1, np.pi / 180, threshold=20, minLineLength=100, maxLineGap=30)

    #Si el plano esta chueco usaremos una matriz de transformacion afin para derectar esquinas a 90°
    angulos = []
    if lineas is not None:
        for l in lineas:
            x1, y1, x2, y2 = l[0]
            # Calculamos el angulo en grados
            angulo = np.degrees(np.arctan2(y2 - y1, x2 - x1))
            
            # Como nos interesan las desviaciones pequeñas del eje los marcaremos a 0 o 90
            # Filtramos para quedarnos con lo que no sea perfectamente recto
            if abs(angulo) < 45: # Lineas horizontales
                angulos.append(angulo)
            elif abs(angulo) > 45: # Lineas verticales 
                #Hacemos que queden a 90° 
                angulos.append(angulo - 90 if angulo > 0 else angulo + 90)
    Angulo_Final = np.median(angulos) if angulos else 0

    #Rotar la imagen para corregir la inclinacion
    rows, cols = Imagen_gris.shape[:2]
    Matriz_Transformacion = cv2.getRotationMatrix2D((cols / 2, rows / 2), Angulo_Final, 1)
    Imagen_Rotada = cv2.warpAffine(Imagen, Matriz_Transformacion, (cols, rows))

    #Convertimos la imagen a escala de grises
    Imagen_gris = cv2.cvtColor(Imagen_Rotada, cv2.COLOR_BGR2GRAY)

    #Normalizamos la imagen
    #Esto es importante para mejorar el contraste y facilitar la deteccion de lineas y esquinas, evitando lass iluminaciones desiguales.
    Imagen_Normalizada = (Imagen_gris - Imagen_gris.min()) / (Imagen_gris.max() - Imagen_gris.min()) * 255
    Imagen_Normalizada = Imagen_Normalizada.astype(np.uint8)

    #Filtro de Blur Gausssiano
    #Este filtro ayuda a reducir el ruido en la imagen, lo que facilita la deteccion de lineas y esquinas.
    Imagen_Gaussiana = cv2.GaussianBlur(Imagen_Normalizada, (11, 11), 0)

    #Umbralizacion por Otsu
    #Este metodo encuentra automaticamente el umbral para separar el fondo de los objetos.
    _, Imagen_Binaria = cv2.threshold(Imagen_Gaussiana, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    #Este es un filtro que ayuda a quitar y separar ruidos pequeños, ademas de separar los objetos que esten muy juntos, lo que facilita la deteccion de lineas y esquinas.
    limpieza = np.ones((5, 5), np.uint8)
    Imagen_Limpiada = cv2.morphologyEx(Imagen_Binaria, cv2.MORPH_OPEN, limpieza, iterations=1)
    #Aplicamops una erosion para eliminar pequeños ruidos y adelgazar los muros antes de pasarlo al proceso de Canny
    erosion = np.ones((7, 7), np.uint8)
    Imagen_Limpiada = cv2.erode(Imagen_Limpiada, erosion, iterations=1)

    return Imagen_Rotada, Imagen_Limpiada