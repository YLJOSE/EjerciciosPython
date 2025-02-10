# 12.	Escribe una función que reciba una lista y un número como parámetro, y 
# que devuelva una lista formada por las palabras que tengan menos letras que el número pasado como parámetro

def palabras_mas_cortas(lista, n):
    return [palabra for palabra in lista if len(palabra) < n]

palabras = ["gato", "elefante", "murciélago", "perro"]
longitud_maxima = 6
resultado = palabras_mas_cortas(palabras, longitud_maxima)
print(resultado)