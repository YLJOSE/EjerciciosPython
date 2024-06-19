animales = ["perro","gato","loro","ardilla"]
# bucle forEach para iterar la lista animales
for animal in animales:
    print(animal)
numeros = [1,2,3,4]
for numero in numeros:
    resultado = numero * 10
    print(resultado)
# para realizar el for anidado las listas deben tener la miscantidad de elementos
# iterando con dos listas utilizando el metodo zip()
for numero,animal in zip(animales, numeros):
    print(numero)
    print(animal)
# iterando con for in range()
for i in range(10):
    print(i)
for i in range(5,10):
    print(i)
# recorrer lista por su indice
for i in enumerate(numeros):
    indice = i[0]
    valor = i[1]
    print(f"el indice es {indice} y el valor es {valor}")
# for con else a su altura
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual : {numero}")
else:
    print("el bucle termino")
# funciona igual con las tuplas

    