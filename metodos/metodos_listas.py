lista = list(["Hola soy","Juanjo" ,20])
print(lista)
# devuelve la cantidad de elementos de la lista
resultado = len(lista)
print(resultado)
# agregar elemento a la lista
lista.append("Nueva inserccion")
print(lista)
# agregar elemento a la lista con un indice especifico
lista.insert(2,"inserccion con indice")
print(lista)
# agregar varios elementos a la lista
lista.extend([2024,True])
print(lista)
# eliminar un elemento de la lista por un indice
lista.pop(0)
# eliminar el ultimo elemento de la lista se utiliza el -1
lista.pop(-1)
print(lista)
# remover un elemento de la lista por su valor(nombre)
lista.remove(20) # si no encuentra el valor te dara una excepcion
print(lista)
# ordenar los elementos de la lista de forma ascendente 
# la lista se ordena si los elementos no son strings
lista2 = list([3,2,1,4,6,5])
lista2.sort()
print(lista2)
# ordenar la lista al revez
lista.reverse()
print(lista)
# eliminar todos los elementos de la lista
lista.clear()
print(lista)
