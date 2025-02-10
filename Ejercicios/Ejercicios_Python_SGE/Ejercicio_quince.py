#15.	Escribe una función que cuente el número de mayúsculas de las frases introducidas por el usuario
def contar_mayusculas(frase):
    return sum(1 for letra in frase if letra.isupper())

frase = input("Introduce una frase: ")
num_mayusculas = contar_mayusculas(frase)
print(f"Número de mayúsculas en la frase: {num_mayusculas}")