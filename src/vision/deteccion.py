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
"""
import cv2 
import numpy as np
import matplotlib.pyplot as plt

def Detectar_caracteristicas(Imagen_Rotada, Imagen_Limpiada):
    #Detectar bordes usando el operador de Canny
    Bordes = cv2.Canny(Imagen_Limpiada, 15, 15, apertureSize=5)
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 2, 3), plt.imshow(Bordes, cmap='gray'), plt.title('Deteccion de Bordes con Canny'), plt.axis('off')

    #Detectar esquinas usando el metodo de Harris

    #Como el metodo de Harris requiere una imagen en formato float32, convertimos la imagen a este formato.
    Harris_gray = np.float32(Imagen_Limpiada)
    Esquinas = cv2.cornerHarris(Harris_gray, blockSize=2, ksize=3, k=0.1)
    Esquinas = cv2.dilate(Esquinas, None)

    #Vamos a dilatar para que se vean mas visibles las esquinas.
    Imagen_Harris = cv2.dilate(Esquinas, None)

    #Para las lineas, utilizamos la transformada de Hough para detectar lineas rectas en la imagen.
    Lineas = cv2.HoughLinesP(
        Bordes, 
        rho = 1, 
        theta = np.pi / 180, 
        threshold=54, 
        minLineLength=30, 
        maxLineGap=10
    )

    #Dibujamos las lineas detectadas en la imagen original. Vamos a poner las lineas en rojo para que se vean mejor y de un grosor mas visible.
    Resultado = Imagen_Rotada.copy()
    if Lineas is not None:
        for linea in Lineas:
            x1, y1, x2, y2 = linea[0]
            cv2.line(Resultado, (x1, y1), (x2, y2), (0, 0, 255), 5)

    #Dibujar las esquinas detectadas en la imagen en color azul, estos com puntos azules para que se vean mejor, y con un grosor de 1 para dejar limpio el plano.
    Resultado[Esquinas > 0.05 * Esquinas.max()] = [255, 0, 0]
    indices_esquinas = np.argwhere(Esquinas > 0.05 * Esquinas.max())
    for pt in indices_esquinas:
        cv2.circle(Resultado, (pt[1], pt[0]), 1, (255, 0, 0), -1)
    return Resultado