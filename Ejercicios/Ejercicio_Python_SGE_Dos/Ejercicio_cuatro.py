#4.	Crea una función que lea un fichero de texto y
# muestre por pantalla dicho texto pero un ‘#’ entre cada letra. Por ejemplo:
# REAL ZARAGOZA se transforma en R#E#A#L #Z#A#R#A#G#O#Z#A. Pista: busca como usar el parámetro end de print

def mostrar_texto_reemplazado(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
           
            for letra in texto:
                print(letra, end="#")
            
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None


mostrar_texto_reemplazado("C:/Users/ALUMNO CCC - TARDE/Desktop/AD/fichero.txt")