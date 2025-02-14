import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual

def multiplicar (a, b):
     
    return a * b

resultado = multiplicar (5, 3) + multiplicar (2, 4)
print(resultado)

#
print("------------------")
x = 5
y = "3"
z = x + int(y)
print(z)

print((not True) or (False and True) )