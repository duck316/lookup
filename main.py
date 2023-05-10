import amazone
import ebay
import random
from amazone import depure_conten as amazone_articulos
from ebay import depure_conten as ebay_articulos

# Funcion para mezclar el orden de los articulos
def mezclador_articulos(lista_original):
    orden = list()
    for i in range(len(lista_original)):
        orden.append(i)
    print(orden)
    random.shuffle(orden)
    print(orden)

    lista_mezclada = list()
    for x in orden:
        lista_mezclada.append(lista_original[x])

    return lista_mezclada

# Entrada del Usuario
arti = input("Que Articulo buscas: ")

# Ejecutando el llamado de los articulos
ebay.ebayscrao(arti)
amazone.amascrap(arti)

# Fucionando las Diccionarios para luego mezclar el orden de presentación
show_articulos = amazone_articulos + ebay_articulos

# Diccionario Final
final_list = mezclador_articulos(show_articulos)

# Prueba de Orden
for x in final_list:
    print(x)



