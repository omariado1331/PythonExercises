#
 # Escribe un programa que muestre por consola (con un print) los
 # números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión),
 # sustituyendo los siguientes:
 # - Múltiplos de 3 por la palabra "fizz".
 # - Múltiplos de 5 por la palabra "buzz".
 # - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#

for i in range(1, 101):
    divthree = i%3==0
    divfive = i%5==0
    if(divthree and divfive):
        print("fizzbuzz")
    elif(divthree):
        print("fizz")
    elif(divfive):
        print("buzz")
    else:
        print(i)