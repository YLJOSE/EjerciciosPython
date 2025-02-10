#Crea una clase canción que tenga un atributo, letra (el cual es una lista). 
# Crea un método cantamelo, que devuelva cada elemento de letra en una línea.

class cancion:
    def __init__(self,letra):
        self.letra = letra
    
    def cantamelo(self):

        for letras in self.letra:
            print(letras, end=" ")

mi_cancion = cancion(["hola como estas","hace tiempo que no se de tí"])
mi_cancion.cantamelo()