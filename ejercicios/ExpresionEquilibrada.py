 # Crea un programa que comprueba si los paréntesis, llaves y corchetes
 # de una expresión están equilibrados.
 # - Equilibrado significa que estos delimitadores se abren y cieran
 #   en orden y de forma correcta.
 # - Paréntesis, llaves y corchetes son igual de prioritarios.
 #   No hay uno más importante que otro.
 # - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 # - Expresión no balanceada: { a * ( c + d ) ] - 5 }

pares_agrupacion= {')': '(', ']' :'[', '}':'{'}
def es_equilibrada(expresion):
    pila = []
    for char in expresion:
        if char in '{[(':
            pila.append(char)
        elif char in '}])':
            if(not pila or pila[-1] != pares_agrupacion[char]):
                return False
            pila.pop()
    return not pila

def expresion_equilibrada(expresion):
    if(es_equilibrada(expresion)):
        print('Expresion equilibrada')
    else:
        print('Expresion no equilibrada')


