#
# Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
# ¿De cuántas maneras eres capaz de hacerlo?
# Crea el código para cada una de ellas.
#

def imprimir():
    print("**1** Recursivo")
    contar_recursivo(1)
    print()
    print("**2** Ciclo For")
    contar_for()
    print()
    print("**3** Ciclo While")
    contar_while()
    print()
    print("**4** Ciclo Do While")
    contar_do_while()
    print()
    print("**5** Usando map")
    contar_map()
    print("**6** Usando join")
    contar_join()
    print("**7** Usando foreach")
    contar_foreach()

def contar_recursivo(n):
    if n > 100:
        return
    print(n, end=" ")
    contar_recursivo(n+1)

def contar_for():
    for n  in range(1,101):
        print(n, end=" ")

def contar_while():
    n = 1
    while n <= 100:
        print(n, end=" ")
        n+=1

def contar_do_while():
    n=1
    while True:
        print(n, end=" ")
        if(n>=100):
            break
        n += 1

def contar_map():
    print(*map(str, range(1,101)), sep=" ")

def contar_join():
    print(" ".join(str(i) for i in range(1,101)))


def contar_foreach():
    list(map(lambda x : print(x, end=" "), range(1, 101)))