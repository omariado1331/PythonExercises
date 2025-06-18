#
# Crea una función que evalúe si un/a atleta ha superado correctamente una
# carrera de obstáculos.
# - La función recibirá dos parámetros:
#      - Un array que sólo puede contener String con las palabras
#        "run" o "jump"
#      - Un String que represente la pista y sólo puede contener "_" (suelo)
#        o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#        será correcto y no variará el símbolo de esa parte de la pista.
#      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#      - Si hace "run" en "|" (valla), se variará la pista por "/".
# - La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista.

def obstaculos(lista_acciones_atleta, pista ):
    if(len(lista_acciones_atleta) != len(pista)):
        print('la cantidad de acciones no corresponde con la pista')
        return
    c=0
    pista_terminada=''
    pista_superada = True
    for accion in lista_acciones_atleta:
        if accion == 'run' and pista[c] == '_':
            pista_terminada += pista[c]
        elif(accion == 'jump' and pista[c] == '|'):
            pista_terminada += pista[c]
        else:
            pista_terminada += 'x'
            pista_superada = False
        c += 1
    if(pista_superada):
        print(f"{pista_superada} superó la pista {pista_terminada}")
    else:
        print(f"{pista_superada} no supero la pista {pista_terminada}")
