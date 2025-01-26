

class Persona:
   
    def __init__(self,nombre,apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    def saludar(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad}")

        