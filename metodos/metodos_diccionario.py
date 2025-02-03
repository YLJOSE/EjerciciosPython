diccionario = {
    "nombre" : "juanjo",
    "apellido" : "rojas",
    "edad" : 20
}
# devuelve las claves y tambien nos sirve para iterar
claves = diccionario.keys()
print(claves)
# devuelve el contenido dandole el nombre del elemento
contenido = diccionario.get("nombre")
print(contenido)
# obtener un elemento dict_items iterables
diccionario_iterable = diccionario.items()
print(diccionario_iterable)
# eliminar un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)
# eliminar todos los elementos del diccionario o lista
diccionario.clear()
print(diccionario)
 