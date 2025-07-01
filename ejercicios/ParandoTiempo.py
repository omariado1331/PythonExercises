#
# Crea una función que sume 2 números y retorne su resultado pasados
# unos segundos.
# - Recibirá por parámetros los 2 números a sumar y los segundos que
#   debe tardar en finalizar su ejecución.
# - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#   asíncrona, es decir, sin detener la ejecución del programa principal.
#   Se podría ejecutar varias veces al mismo tiempo.
#
import asyncio
#inicia las sumas asincronas
def iniciar():
    asyncio.run(ejecutar_sumas())

#funcion asincrona para sumar
async def sumar(a,b,segundos):
    await asyncio.sleep(segundos)
    resultado = a+b
    print(resultado)
    return resultado

# se ejecutan las sumas, se ingresa los valores a sumar y los segundos
# que debe esperar para realizar la suma
async def ejecutar_sumas():
    sumas = [
        sumar(5, 6, 4),
        sumar(10, 12, 1),
        sumar(8, 6, 5)
    ]
    resultados = await asyncio.gather(*sumas)

