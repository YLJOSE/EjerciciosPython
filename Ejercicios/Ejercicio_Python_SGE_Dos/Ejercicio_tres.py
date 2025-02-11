#3.	Crea una función que lea un fichero plano y devuelva el número de minúsculas, mayúsculas y vocales.

def contar_letras_y_vocales(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            
            num_minusculas = sum(1 for letra in texto if letra.islower())
            num_mayusculas = sum(1 for letra in texto if letra.isupper())
            num_vocales = sum(1 for letra in texto if letra.lower() in 'aeiouáéíóúü')

        return num_minusculas, num_mayusculas, num_vocales

    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None

archivo = "Ejercicios\primenumbers.txt" 
resultado = contar_letras_y_vocales(archivo)
if resultado:
    minusculas, mayusculas, vocales = resultado
    print(f"Número de minúsculas: {minusculas}")
    print(f"Número de mayúsculas: {mayusculas}")
    print(f"Número de vocales: {vocales}")
