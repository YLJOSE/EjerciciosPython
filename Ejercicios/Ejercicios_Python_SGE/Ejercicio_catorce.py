#14.	Escribe un programa que reciba frases del usuario y las pase a mayúsculas.

def convertir_a_mayusculas():
    while True:
        frase = input("Escribe una frase (o 'SALIR' para terminar): ")
        if frase.upper() == "SALIR":
            print("Programa terminado.")
            break
        print(frase.upper())
convertir_a_mayusculas()