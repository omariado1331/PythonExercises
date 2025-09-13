
 #* Simula el funcionamiento de una máquina expendedora creando una operación
 #* que reciba dinero (array de monedas) y un número que indique la selección
 #* del producto.
 #* - El programa retornará el nombre del producto y un array con el dinero
 #*   de vuelta (con el menor número de monedas).
 #* - Si el dinero es insuficiente o el número de producto no existe,
 #*   deberá indicarse con un mensaje y retornar todas las monedas.
 #* - Si no hay dinero de vuelta, el array se retornará vacío.
 #* - Para que resulte más simple, trabajaremos en céntimos con monedas
 #*   de 5, 10, 50, 100 y 200.
 #* - Debemos controlar que las monedas enviadas estén dentro de las soportadas.

def validarm(monedas):
  for moneda in monedas:
    if moneda not in [5,10,50,100,200]:
      return False
  return True

def comprar(monedas, seleccionp):
  if not validarm(monedas):
    print('monedas no soportadas')
    return
  productos =[{"nombre":"papas fritas", "id":11,"precio":205},
              {"nombre":"chocolate","id":8,"precio":450},
              {"nombre":"galletas","id":6,"precio":50},
              {"nombre":"chiles","id":4,"precio":5}]
  switch = True
  precio_producto=0
  nombre_producto=""
  for p in productos:
    if seleccionp == p["id"]:
      precio_producto =p["precio"]
      nombre_producto=p["nombre"]
      switch = False
  if switch:
    print ('id de prod no existente')
    return
  pagot= sum(monedas)
  if pagot < precio_producto:
    print('trae dinero la sgte')
    return
  cambio=pagot-precio_producto
  print(cambio)
  print(nombre_producto)
  cambioarray=[]

  for corte in [5,10,50,100,200][::-1]:
    nro_rep_corte=cambio//corte
    if nro_rep_corte>0:
      aux_lista_cambio=[corte]*nro_rep_corte#nro de veces q se repite algo
      cambioarray.extend(aux_lista_cambio)#añadimos un elemento a un array
      cambio= cambio%corte
  print(cambioarray)

