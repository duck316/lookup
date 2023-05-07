import ebay
import amazone
from amazone import depure_conten as amazone_articulos
from ebay import depure_conten as ebay_articulos

arti = input("Que Articulo buscas: ")
ebay = ebay.ebayscrao(arti)
amazone.amascrap(arti)


amazone_items = amazone_articulos
ebay_items = ebay_articulos

print("Articulos Ebay")
for show in ebay_items:
    print(show)

print("Articulos Amazone")
for show in amazone_items:
    print(show)
