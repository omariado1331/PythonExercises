#
# Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
# resultado e imprímelo.
# - El .txt se corresponde con las entradas de una calculadora.
# - Cada línea tendrá un número o una operación representada por un
#   símbolo (alternando ambos).
# - Soporta números enteros y decimales.
# - Soporta las operaciones suma "+", resta "-", multiplicación "*"
#   y división "/".
# - El resultado se muestra al finalizar la lectura de la última
#   línea (si el .txt es correcto).
# - Si el formato del .txt no es correcto, se indicará que no se han
#   podido resolver las operaciones.
#

def calcular_archivo():
    try:
        with open("Challenge21.txt", "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip() != ""]

        if len(lineas) < 1 or len(lineas) % 2 == 0:
            print("Formato Incorrecto")
            return

        resultado = None
        i=0

        while i < len(lineas):
            if i % 2 == 0:
                try:
                    numero = int(lineas[i])
                except ValueError:
                    print("Formato incorrecto")
                    return

                if resultado is None:
                    resultado = numero
                else:
                    if operacion == '+':
                        resultado += numero
                    elif operacion == '-':
                        resultado -= numero
                    elif operacion == '*':
                        resultado *= numero
                    elif operacion == '/':
                        if numero == 0:
                            print("error division entre cero")
                            return
                        resultado /= numero
            else:
                if lineas[i] not in ['+','-','*','/']:
                    print("Formato incorrecto")
                    return
                operacion = lineas[i]

            i+=1

        print(f"el resultado es {resultado}")

    except FileNotFoundError:
        print("El archivo no se encuentra")



