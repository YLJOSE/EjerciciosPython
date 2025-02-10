#5.	Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def devolver_media(list):
    media =0
    
    for i in enumerate(list):
        indice = i[0]
        valor = i[1]
        media += valor   
    print(f"La media es: {media / (indice + 1)}")

devolver_media([5,5,10])
