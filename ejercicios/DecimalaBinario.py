#
# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#

def convertir_binary(num):
    resultado = convertir(num)
    print(resultado)


def convertir(num):
    if(num == 0):
        return ""
    else:
        return convertir(num//2)+str(num%2)
