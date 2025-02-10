#16.Escribe una función que cuente el número de minúsculas de las frases introducidas por el usuario
def contar_minusculas(frase):
    return sum(1 for letra in frase if letra.islower())

frase = input("Introduce una frase: ")
num_minusculas = contar_minusculas(frase)
print(f"Número de minúsculas en la frase: {num_minusculas}")