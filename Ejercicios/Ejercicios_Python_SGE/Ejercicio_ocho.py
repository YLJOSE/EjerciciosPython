#8.	Escribe una función que reciba una lista como parámetro e indique 
# si es un palíndromo (es decir, que se lea igual del derecho y
# del revés, como No subas, abusón o level)

def devolver_si_es_palindromo(palabra):
    nueva = palabra[::-1]
    
    if nueva == palabra:
        print(f"Esta palabra: {nueva}, es palindroma!!")
    
    
devolver_si_es_palindromo("level")


