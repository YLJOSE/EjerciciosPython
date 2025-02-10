# 13.	Escribe un programa que reciba una lista como parámetro y
# devuelva que tenga únicamente los elementos no duplicados de la recibida como parámetro.

def eliminar_duplicados(lista):
    elementos_unicos = []
    vistos = set()
    
    for elemento in lista:
        if elemento not in vistos:
            elementos_unicos.append(elemento)
            vistos.add(elemento)
    
    return elementos_unicos

lista = [1, 2, 3, 2, 4, 1, 5, 6, 3, 7]
resultado = eliminar_duplicados(lista)
print(resultado)