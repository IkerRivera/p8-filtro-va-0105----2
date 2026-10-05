import cv2
import os
# Iker Montoya 0105
# Cargar la imagen
ruta = os.path.join(os.path.dirname(__file__), "pinguino.jpg")
imagen = cv2.imread(ruta)

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(imagen, 5)

# Mostrar imagen original
cv2.imshow("pinguino original 0105", imagen)

# Mostrar imagen filtrada
cv2.imshow("pinguino filtrado 0105", imagen_filtrada)

# Guardar resultado
cv2.imwrite("pinguino_filtrado.jpg", imagen_filtrada)

print("Filtro de mediana aplicado correctamente.")
print("pinguino 0105")
print("Resultado guardado en: pinguino_filtrado.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Iker Montoya 0105")