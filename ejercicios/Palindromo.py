# Escribe una función que reciba un texto y retorne verdadero o
# falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee
# de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.
import string
import unicodedata
def es_palindromo(texto):
    print(palindromo(texto))
def palindromo(texto):
    texto_minusculas = texto.lower()
    texto_sin_acento = unicodedata.normalize('NFD', texto_minusculas)
    texto_limpio = texto_sin_acento.encode('ascii', 'ignore').decode('utf-8')
    punctuation = string.punctuation
    for signo in punctuation:
        texto_limpio = texto_limpio.replace(signo, '')
    texto_limpio = texto_limpio.replace(' ', '')
    text_limpio_inv = texto_limpio[::-1]
    print(texto_limpio)
    print(text_limpio_inv)
    if(texto_limpio == text_limpio_inv):
        return True
    else:
        return False