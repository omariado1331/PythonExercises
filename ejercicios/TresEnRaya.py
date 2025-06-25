#
# Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
# y retorne lo siguiente:
# - "X" si han ganado las "X"
# - "O" si han ganado los "O"
# - "Empate" si ha habido un empate
# - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
#   O si han ganado los 2.
# Nota: La matriz puede no estar totalmente cubierta.
# Se podría representar con un vacío "", por ejemplo.
#

def conocer_ganador(tablero):
    print(verificar_ganador(tablero))

def verificar_ganador(tablero):
    #contar la cantidad de x y o
    cont_x = sum(fila.count('X') for fila in tablero)
    cont_o = sum(fila.count('O') for fila in tablero)
    #retorna nulo si la proporcion no es correcta
    if not (cont_x == cont_o or cont_x+1 == cont_o or cont_x == cont_o+1):
        return "NULO"
    #verificar si gano x o gano o
    gana_x = es_ganador('X', tablero)
    gana_o = es_ganador('O', tablero)
    #verificar si ganaron ambos
    if(gana_x and gana_o):
        return "NULO"

    if(gana_x):
        return "X"
    elif(gana_o):
        return "O"
    elif any("" in fila for fila in tablero):
        return "juego no completado"
    else:
        return "EMPATE"


def es_ganador(jugador, tablero):
    #verificar si gano en las filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] == jugador:
            return True
    #verficar si ganó en las columnas
    for column in range(3):
        if tablero[0][column] == tablero[1][column] == tablero[2][column] == jugador:
            return True
    #verficiar las diagonales
    if(tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador):
        return True
    if (tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador):
        return True
    return False