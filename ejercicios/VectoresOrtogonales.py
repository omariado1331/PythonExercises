#
# Crea un programa que determine si dos vectores son ortogonales.
# - Los dos array deben tener la misma longitud.
# - Cada vector se podría representar como un array. Ejemplo: [1, -2]
#

def verificar_vectores(vector_1,vector_2):
    if len(vector_1) == len(vector_2) == 2:
       producto = vector_1[0]*vector_2[0] + vector_1[1]*vector_2[1]
    else:
        print('Vectores mal definidos no tiene la misma longitud')
        return
    if producto == 0:
        print('Los vectores son ortogonales')
    else:
        print('Los vectores NO son ortogonales')

