 #
 # Escribe un programa que imprima los 50 primeros números de la sucesión
 # de Fibonacci empezando en 0.
 # - La serie Fibonacci se compone por una sucesión de números en
 #   la que el siguiente siempre es la suma de los dos anteriores.
 #   0, 1, 1, 2, 3, 5, 8, 13...
 #/

def fibonacci():
    a = 0
    b = 1
    sum=0
    for i in range(51):
        print(a, end=',')
        sum=a+b
        a=b
        b=sum

