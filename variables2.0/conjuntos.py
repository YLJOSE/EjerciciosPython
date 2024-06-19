# creando conjunto con set
# una tupla puede ir dentro de otro diccionario
conjunto = set(["dato1","dato2",("tupla1","tupla2")])
print(conjunto)
# meter un conjunto dentro de otro conjunto
conjunto_uno = frozenset(["dato1","dato2"])
conjunto_dos = {conjunto_uno,"dato3"}
print(conjunto_dos)
# teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}
# verificar si conjunto2 es subconjunto de conjunto1
resultado = conjunto2.issubset(conjunto1)
print(resultado)
# verificar si conjunto2 es superconjunto de conjunto1
resultado = conjunto2.issuperset(conjunto1)
print(resultado)
# verificar si hay un numero o valor en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)
