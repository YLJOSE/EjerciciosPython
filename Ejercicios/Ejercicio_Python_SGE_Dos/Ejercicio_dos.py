#2.	Crea una función que lea un fichero plano y devuelva el número de palabras que terminan por ‘e’ o ‘o’.

def contar_palabras_eo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            palabras = texto.split()  
            
            contador = sum(1 for palabra in palabras if palabra.endswith(('e', 'o')))
        return contador
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None


archivo = "Ejercicios\sowpods.txt"  
resultado = contar_palabras_eo(archivo)
if resultado is not None:
    print(f"Número de palabras que terminan por 'e' o 'o': {resultado}")