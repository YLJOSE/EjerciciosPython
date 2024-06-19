texto = input("Ingresa un texto cualquiera: ")
print(texto)
palabras_separadas = texto.split(" ")
cantidad_palabras = len(palabras_separadas)
print(f"dijiste {cantidad_palabras} palabras y tardarias {cantidad_palabras / 2} segundos en decirlo")
if cantidad_palabras > 120 :
    print("tranqui maquina que no te he pedido un testamento xd")
