#1.	Crea una función que lea un fichero plano y devuelva el número de palabras que empiezan por ‘A’ o ‘W’.

def contar_palabras_aw(nombre_archivo, letra1,letra3):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            palabras = texto.split()  
            
            contador = sum(1 for palabra in palabras if palabra.startswith((letra1,letra3)))
        
        return contador
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None


archivo = "fichero.txt"  
resultado = contar_palabras_aw(archivo,'A','W')
if resultado is not None:
    print(f"Número de palabras que empiezan por 'A' o 'W': {resultado}")