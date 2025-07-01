#
# Crea una función que reciba dos array, un booleano y retorne un array.
# - Si el booleano es verdadero buscará y retornará los elementos comunes
#   de los dos array.
# - Si el booleano es falso buscará y retornará los elementos no comunes
#   de los dos array.
# - No se pueden utilizar operaciones del lenguaje que
#   lo resuelvan directamente.
#

def buscar_comunes(array_1, array_2):
    comunes = []
    for element in array_1:
        if element in array_2:
            comunes.append(element)
    return comunes

def buscar_no_comunes(array_1, array_2):
    no_comunes = []
    for element in array_1:
        if element not in array_2:
            no_comunes.append(element)
    for element in array_2:
        if element not in array_1:
            no_comunes.append(element)
    return no_comunes

def conjuntos(array_1, array_2, booleano):
    if booleano :
        salida = buscar_comunes(array_1, array_2)
    else:
        salida = buscar_no_comunes(array_1, array_2)
    print(salida)