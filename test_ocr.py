from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'


# Cargar la imagen
image_path = "Captura_001.PNG"  # Cambia por la ruta de tu imagen
#image_path = "Captura2.PNG"  # Cambia por la ruta de tu imagen
#image_path = "imagenes_red_n.PNG"  # Cambia por la ruta de tu imagen

image = Image.open(image_path)

# Realizar OCR
texto_extraido = pytesseract.image_to_string(image, lang="spa")  # 'spa' para español

# Imprimir el resultado
print("Texto extraído:")
print(texto_extraido)
