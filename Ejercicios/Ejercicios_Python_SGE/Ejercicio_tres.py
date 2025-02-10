#3.	Escribe un programa que le pida al usuario 3 enteros y devuelva el mayor de los 3


def devuelve_numero_mayor():
    list=[]
    for i in range(3):
        numero = input("Ingresa un numero:")
        list.append(numero)
    list.sort()
    return list[-1]
    
print(f"El numero mayo es: {devuelve_numero_mayor()}")
    