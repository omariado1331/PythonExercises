# Crea una función que reciba dos cadenas como parámetro (str1, str2)
# e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO
#   estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO
#   estén presentes en str1.

def eliminar_caracteres(str1, str2):
    out1 = ''
    out2 = ''
    for char in str1:
        if char not in str2:
            out1 += char
    for char in str2:
        if char not in str1:
            out2 += char
    print(f"cadena 1: {out1}, cadena 2: {out2}")