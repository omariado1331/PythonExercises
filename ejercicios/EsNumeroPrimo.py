#
# Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
#

def imprimirPrimos():
    for i in range(1,101):
        if(esPrimo(i)):
            print(i)

def esPrimo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True