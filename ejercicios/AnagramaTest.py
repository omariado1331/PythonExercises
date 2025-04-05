 # Escribe una función que reciba dos palabras (String) y retorne
 # verdadero o falso (Bool) según sean o no anagramas.
 # - Un Anagrama consiste en formar una palabra reordenando TODAS
 #   las letras de otra palabra inicial.
 # - NO hace falta comprobar que ambas palabras existan.
 # - Dos palabras exactamente iguales no son anagrama.

def isAnagram(cad1, cad2):
    if (cad1.lower() == cad2.lower()):
        return False
    return sorted(cad1.lower()) == sorted(cad2.lower())

