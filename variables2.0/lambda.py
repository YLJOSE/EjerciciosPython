# Funciones sin nombre definidas en una sola línea.
# Se utilizan comúnmente para funciones pequeñas y concisas.
cuadrado = lambda x: x**2

print(cuadrado(5)) # Imprime 25
# Funciones que acepten un número variable de argumentos.
# Esto se logra utilizando el operador * antes del nombre del parámetro.
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22