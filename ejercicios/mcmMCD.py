#
# Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
# que calcule el mínimo común múltiplo (mcm) de dos números enteros.
# - No se pueden utilizar operaciones del lenguaje que
#   lo resuelvan directamente.
#

def mcm_mcd(a,b):
    print(f"Maximo comun divisor: {maximo_comun_divisor(a, b)}")
    print(f"Minimo comun multiplo: {minimo_comun_multiplo(a, b)}")
def maximo_comun_divisor(a, b):
    if a > b:
        while b != 0:
            a, b = b, a % b
        return abs(a)
    else:
        while a != 0:
            b, a = a, b % a
        return abs(b)
def minimo_comun_multiplo(a, b):
    mcd = maximo_comun_divisor(a, b)
    return abs(a*b) // mcd
