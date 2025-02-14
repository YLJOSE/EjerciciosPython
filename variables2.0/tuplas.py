# creando tupla con tuple
tupla = tuple(["dato1", "dato2"])
# creando tupla sin parentesis
tupla2 = "juanjo","rojas",20
# creando tupla sin parentesis con un solo dato
tupla3 = "causa",

#  verificar
print(tupla)
print(tupla2)
print(tupla3)
print("------------------------------")

# Tuplas
# Las tuplas son inmutables, no se puedenmodificar despues de ser creadas es decir no se pueden hacer operaciones CRUD a la misma despues de ser creadas
punto = (3,3,4,5,6,7,8,9,10)
print(punto[0]) # Imprime 3
print(punto.count(3)) # Devuelve el numero de apariciones del dato brindado
print(punto.index(10)) # Devuelver el indice del dato brindado
print(punto.__len__()) # Devuelve la longitud de la tupla