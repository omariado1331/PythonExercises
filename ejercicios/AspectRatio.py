#Crea un programa que se encargue de calcular el aspect ratio de una
#imagen a partir de una url.
# Url de ejemplo:
#  https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
#- Por ratio hacemos referencia por ejemplo a los "16:9" de una
#  imagen de 1920*1080px.

import requests
from math import gcd
from PIL import Image
from io import BytesIO

def getAspectRatio(image_url):
    #Obtenemos la imagen de un url
    response = requests.get(image_url)
    response.raise_for_status()  # Lanza un error si falla la descarga
    image = Image.open(BytesIO(response.content))
    # sacamos el ancho y largo de la imagen
    width, height = image.size
    #calcula el maximo comun divisor entre el ancho y alto
    ratio_gcd = gcd(width, height)
    #retorna ambos valores como una tupla
    return width // ratio_gcd, height // ratio_gcd

def imprimirAspectRatio(url):
    aspectRatio = getAspectRatio(url)
    print(f"El aspect ratio de la imagen es {aspectRatio[0]}:{aspectRatio[1]}")