#
# Escribe una función que calcule y retorne el factorial de un número dado
# de forma recursiva.
#

def imprimirFactorial(n):
    print(f"El factorial de {n} es {factorial(n)}")

def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)