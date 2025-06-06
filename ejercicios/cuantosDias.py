#
# Crea una función que calcule y retorne cuántos días hay entre dos cadenas
# de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se
#   lanzará una excepción.
#
from datetime import datetime, timedelta

def cantidadDias(fechaInput1, fechaInput2):
    formatoFecha = "%d/%m/%Y"
    fecha1 = datetime.strptime(fechaInput1, formatoFecha)
    fecha2 = datetime.strptime(fechaInput2, formatoFecha)
    dias = (fecha2 - fecha1) / timedelta(days=1)
    print(f"La cantidad de dias entre las fechas es {abs(dias)} días")