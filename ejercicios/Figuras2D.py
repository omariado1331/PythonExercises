#
# Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
# - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
# - EXTRA: ¿Eres capaz de dibujar más figuras?
#

def dibujar_forma(n, figura):
    if figura == 'cuadrado':
        cuadrado(n)
    elif figura == 'triangulo':
        triangulo(n)
    elif figura == 'rombo':
        rombo(n)
    elif figura == 'piramide':
        piramide(n)
    elif figura == 'flecha':
        flecha(n)
    else:
        print('valores no validos')

def cuadrado(n):
    for i in range (0,n):
        print('*'*n)

def triangulo(n):
    for i in range(1, n+1):
        print('*'*i)

def rombo(n):
    if n%2 == 0:
        print('El valor ingresado debe ser un numero impar')
        return
    i = 1
    j = n//2
    while i <= n-2:
        print(' '*j+'*'*i)
        i += 2
        j -= 1
    print('*'*n)
    j = 1
    i = n-2
    while i > 0:
        print(' '*j+'*'*i)
        j += 1
        i -= 2

def piramide(n):
    if n%2 == 0:
        print('El valor ingresado debe ser un numero impar')
        return
    i = 1
    j = n//2
    while i <= n-2:
        print(' '*j+'*'*i)
        i += 2
        j -= 1
    print('*'*n)

def flecha(n):
    if n%2 == 0:
        print('El valor ingresado debe ser un numero impar')
        return
    i = 1
    j = n//2
    while i <= n-2:
        print(' '*j+'*'*i)
        i += 2
        j -= 1
    print('*'*n)
    i = 1
    j = n//2
    while i <= n-2:
        print(' '*j+'*')
        i += 2