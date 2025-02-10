# Dado el fichero sowpods.txt, crea una función que devuelva una frase del fichero al azar.
import random
def devolver_frase_fichero_azar(nombre_fichero):
    
    try:
        tipo =[]
        with open(nombre_fichero,'r',encoding='utf-8') as fichero_aleatorio:
            text = fichero_aleatorio.read()
            tipo = text.split(',')
            linea_random = random.randint(0,tipo.__len__())
            print(f"Frase: {tipo[linea_random]}")

    except FileNotFoundError:
        print("El fichero no se encontró")
        return None

devolver_frase_fichero_azar("Ejercicios/sowpods.txt")