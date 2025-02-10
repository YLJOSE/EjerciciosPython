#10.	Escribe una función que reciba dos listas como parámetros, y que devuelva True si tienen algún elemento en común

def tienen_elementos_comunes(lista1, lista2):

    return bool(set(lista1) & set(lista2))

# Ejemplo de uso
lista1 = [1, 2, 3, 4]
lista2 = [4, 5, 6]
print(tienen_elementos_comunes(lista1, lista2)) 

lista3 = [1, 2, 3]
lista4 = [5, 6, 7]
print(tienen_elementos_comunes(lista3, lista4))