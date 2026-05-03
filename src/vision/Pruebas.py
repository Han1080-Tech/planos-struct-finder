import vision
import cv2
import numpy as np

# 1. Procesar
ruta = r"C:\vision\src\vision\Plano_1.png"
original_recto, limpia = vision.preparar_plano(ruta)

# 2. Detectar
resultado = vision.detectar_caracteristicas(limpia, original_recto)

# 3. Mostrar (Antes/Despues) 
comparacion = np.hstack((original_recto, resultado))
cv2.imshow('Libreria Vision: Antes vs Despues', comparacion)
cv2.waitKey(0)
cv2.destroyAllWindows()