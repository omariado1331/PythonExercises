 #
 # Crea un programa que cuente cuantas veces se repite cada palabra
 # y que muestre el recuento final de todas ellas.
 # - Los signos de puntuación no forman parte de la palabra.
 # - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 # - No se pueden utilizar funciones propias del lenguaje que
 #   lo resuelvan automáticamente.
 #
def contar_palabras():
    texto = ('En el corazón de un denso bosque, donde los rayos del sol apenas besaban '
              'el suelo, vivía un pequeño zorro llamado Kael. A diferencia de sus hermanos, '
              'Kael no era astuto ni especialmente rápido. Su mayor pasión eran las estrellas. '
              'Cada noche, mientras los demás zorros soñaban con gallinas y conejos, Kael se '
              'escabullía a un claro del bosque y se tumbaba boca arriba, maravillado por el '
              'manto brillante que se extendía sobre él. Una noche, mientras observaba el cielo, '
              'una estrella fugaz cruzó el firmamento con una estela deslumbrante. Kael, sin pensarlo, '
              'cerró los ojos y deseó con todas sus fuerzas poder tocar una estrella. Al abrir los '
              'ojos, un pequeño guijarro luminoso yacía a su lado. No era una estrella, pero brillaba '
              'con una luz propia, cálida y reconfortante.Intrigado, Kael tomó el guijarro con su '
              'hocico. Al hacerlo, sintió una extraña energía recorrer su cuerpo. De repente, las '
              'constelaciones que tanto había admirado ya no eran solo puntos de luz lejanos; '
              'podía sentir sus historias, sus nombres antiguos susurrados por el viento. '
              'El pequeño zorro, que antes se sentía insignificante, descubrió que llevaba un universo '
              'de conocimiento dentro de sí. A partir de esa noche, Kael ya no solo miraba las estrellas. '
              'Las entendía. Compartía sus historias con los demás animales del bosque, que escuchaban '
              'embelesados los relatos del firmamento. El pequeño zorro que soñaba con tocar las estrellas, '
              'había encontrado la manera de traer su magia a la tierra, no con sus patas, sino con su corazón '
              'y sus palabras. Y así, el bosque, antes solo iluminado por la luna, también brillaba con la '
              'sabiduría de las estrellas.')

    #poner el texto en minusculas y elminar acentos
    t_minuscules = ""
    for c in texto:
        if 'A'<= c <= 'Z' or 'Á' <= c <='Ú':
            #ord(c) convierte el caracter a codigo ASCII
            #se suma 32 para obtener su equivalente en minuscula
            #chr() convierte el caracter que esta codigo ASCII nuevamente a caracter
            t_minuscules += chr(ord(c)+32)
        else:
            t_minuscules += c

    #eliminar signos de puntuacion
    signos_puntuacion = ['.', ',', ':', ';', '!', '¡', '?', '¿', '"', '(', ')']
    texto_limpio = ""
    for c in t_minuscules:
        if c not in signos_puntuacion:
            texto_limpio += c

    #construir las palabras y agregarlas en un arreglo de palabras
    palabras = []
    palabra = ""
    for c in texto_limpio:
        if c != ' ':
            palabra += c
        else:
            if palabra != "":
                palabras.append(palabra)
                palabra = ""
    if palabra != "":
        palabras.append(palabra)

    #crear el diccionario conteo con clave que sera la palabra y el valor el numero de veces
    # que se repite la palabra
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    #ordenar el diccionario de acuerdo a las veecs que se repite en forma descendente
    conteo = dict(sorted(conteo.items(), key=lambda item: item[1], reverse=True))
    #imprimir todas las palabras agregadas al diccionario
    for palabra in conteo:
        print(f"'{palabra}' se repite {conteo[palabra]} veces")

