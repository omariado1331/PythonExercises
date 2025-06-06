#
# Escribe una función que calcule si un número dado es un número de Armstrong
# (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información
# al respecto.
# Un número de Armstrong es un entero que es igual a la suma de sus dígitos
# elevados a la potencia del número de dígitos que tiene. Por ejemplo, 153
# es un número de Armstrong porque 1³ + 5³ + 3³ = 153
#

def es_amstrong(n):
    cantDigitos = len(str(n))
    copiaN=n
    acumulador = 0
    while n > 0:
        acumulador = acumulador + (n%10)**cantDigitos
        n = n // 10
    acumulador = acumulador + (n%10)**cantDigitos
    if(copiaN == acumulador):
        print('Es un numero de Amstrong')
    else:
        print('No cumple con las condiciones de un numero de amstrong')

