import cv2
import numpy as np
from src.vision.procesamiento import Preparar_Plano
from src.vision.deteccion import Detectar_caracteristicas
import os

#Mandamos a llamar la funcion para que cualquier persona pueda usar el codigo sin importar su sistema operativo o donde lo tenga guardado
#We called the function so that anyone can use the code regardless of their operating system or where they have it stored.
Directorio_Actual = os.path.dirname(os.path.abspath(__file__))




# Definir la ruta de la imagen uniendo el directorio actual con la ubicación interna
# Define the image path by joining the current directory with the internal location
"""
SOLO MUEVE AQUI / ONLY MOVE HERE 

Solo quita el '#' de la línea que quieras probar, requerda que solo se puede usar una imagen a la vez, 2 de ellas ocupan el #:
Just remove the '#' from the line you want to test. Remember that only one image can be used at a time; two images occupy the #:
"""
ruta = os.path.join(Directorio_Actual, "src", "vision", "Plano_1.png")
# ruta = os.path.join(Directorio_Actual, "src", "vision", "Plano_2.jpg")
# ruta = os.path.join(Directorio_Actual, "src", "vision", "Plano_3.jpg")




#Mandamos a llamar la primera funcion, que nos va a devolver las dos imagenes limpias que necesitamos para la segunda funcion
#We called the first function, which will return the two clean images we need for the second function.
Imagen_Rotada, Imagen_Limpiada = Preparar_Plano(ruta)

#Ahora que ya existen, se las pasamos a la segunda función que se encarga de detectar las caracteristicas estructurales del plano.
#Now that they already exist, we pass them to the second function that is responsible for detecting the structural characteristics of the plan.
resultado = Detectar_caracteristicas(Imagen_Rotada, Imagen_Limpiada)

#Mensaje para confirmar que todo se ha importado correctamente.
#Message to confirm that everything has been imported correctly.
print("Importacion y exitosa.")

#Usamos np.hstack para poner las comparaciones juntos.
#We use np.hstack to put the comparisons together.
comparativa = np.hstack((Imagen_Rotada, resultado))

#Mostrar la ventana
#Show the window
cv2.imshow('Proyecto Final: Deteccion Estructural', comparativa)
cv2.waitKey(0) 
cv2.destroyAllWindows()