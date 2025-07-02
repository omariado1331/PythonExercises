#
# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "R" (piedra), "P" (papel)
#   o "S" (tijera).
# - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
#

def calcular_partidas(juegos):
    player_1 = 0
    player_2 = 0
    for juego in juegos:
        ganador = calcular_ganador(juego[0], juego[1])
        if ganador == 1:
            player_1 += 1
        elif ganador == 2:
            player_2 += 1
    if player_1 == player_2:
        print("Empate")
    elif player_1 > player_2:
        print("Player 1")
    elif player_2 > player_1:
        print("Player 2")
    else:
        print("Juego no concluido")


def calcular_ganador(jugada_1, jugada_2):
    jugadas = {"R": "S", "S": "P", "P": "R"}
    if jugada_1 == jugada_2:
        return 0
    elif jugadas[jugada_1] == jugada_2:
        return 1
    elif jugadas[jugada_2] == jugada_1:
        return 2
    else:
        return 3
