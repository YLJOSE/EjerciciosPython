#11. Escribe una función que reciba una lista como parámetro y devuelva la palabra más larga de la lista
def palabra_mas_larga(lista):
    if not lista:
        return None  
    return max(lista, key=len)

# Ejemplo de uso
palabras = ["gato", "elefante", "murciélago", "perro"]
print(palabra_mas_larga(palabras)) 