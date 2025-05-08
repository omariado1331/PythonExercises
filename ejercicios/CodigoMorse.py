#
# Crea un programa que sea capaz de transformar texto natural a código
# morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar
#   la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#   o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en
#   https://es.wikipedia.org/wiki/Código_morse.
#
import string

#diccionario de para convertir de texto a morse
texto_a_morse = {"a" : ".-", "b": "-...", "c": "-.-.", "d" : "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
         "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.","ñ": "--.--", "o": "---",
         "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
         "x": "-..-", "y": "-.--", "z": "--..", "0": "----", "1": ".----", "2": "..---", "3": "...--",
         "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", ".": ".-.-.-",
         ",": "--..--", "?": "..--..", " \" ": ".-..-.", "/": "-..-.", " ": " " }
#diccionario para convertir de morse a texto inviritiendo valor por key y key por valor del diccionario morse
morse_a_texto = {v: k for k, v in texto_a_morse.items()}

#verifica si el texto insertado esta en lenguaje natural
def es_txtnatural(cadena):
    for c in cadena:
        if c in list(string.ascii_letters):
            return True
    return False
#transforma de lenguaje natural a codigo morse
def transformar_a_cmorse(cadena):
    texto_cmorse= ""
    texto = cadena.lower().strip()
    for c in texto:
        if c == " ":
            texto_cmorse += " "
        else:
            texto_cmorse += texto_a_morse[c]+ " "
    print(texto_cmorse)

#transforma de codigo morse a lenguaje natural
def transformar_a_lnatural(morse):
    #arreglo de texto en lenguaje natural
    texto_lnatural = []
    palabras = morse.strip().split("  ")
    for palabra in palabras:
        letras = []
        for simbolo in palabra.split(" "):
            if simbolo in morse_a_texto:
                letras.append(morse_a_texto[simbolo])
        #une todas las letras del arreglo letras en una sola cadena sin espacios entre ellas
        #y la agrega al arreglo texto_lnatural
        texto_lnatural.append("".join(letras))
    #une todos los elementos de la lista texto_lnatural en una sola cadena con un espacio entre ellas
    print(" ".join(texto_lnatural))

def transformar_texto(texto):
    if (es_txtnatural(texto)):
        transformar_a_cmorse(texto)
    else:
        transformar_a_lnatural(texto)