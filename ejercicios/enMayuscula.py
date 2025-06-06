#
# Crea una función que reciba un String de cualquier tipo y se encargue de
# poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que
#   lo resuelvan directamente.
#

def convertirMayusculas(c):
    if 'a' <= c <= 'z' or 'á' <= c <= 'ú':
        return chr(ord(c)-32)
    return c

def enMayusculas(texto):
    palabra = ''
    textoConvertido = ''
    for char in texto:
        if(char == ' '):
            textoConvertido += palabra+' '
            palabra = ''
        else:
            if(palabra == ''):
                palabra += convertirMayusculas(char)
            else:
                palabra += char
    textoConvertido += palabra
    print(textoConvertido)
