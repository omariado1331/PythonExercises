#
# Crea una función que reciba días, horas, minutos y segundos (como enteros)
# y retorne su resultado en milisegundos.
#

def convertir(dias, horas, minutos, segundos):
    dias_mil = dias * 24 * 60 *60 * 1000
    horas_mil = horas * 60 * 60 * 1000
    minutos_mil = minutos * 60 * 1000
    segundos_mil = segundos * 1000

    print(dias_mil + horas_mil + minutos_mil + segundos_mil)