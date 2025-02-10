# Crea la clase triangulo con los atributos angulo1, angulo2 y angulo3.
#Crea una variable llamada num_lados y haz que sea 3.
#Crea un método llamado comprobar_angulos, que devolverá True si la suma de los ángulos es 180, y Falso en caso contrario
#Crea una variable llamada mi_triangulo, cuya función comprobar_angulos sea cierta.

class triangulo:
    
    def __init__(self,angulo1,angulo2,angulo3):
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3
        self.NUM_LADOS = 3

    def comprobar_angulos(self):
        if self.angulo1 + self.angulo2 + self.angulo3 == 180:
            return True
        else:
            return False


mi_triangulo = triangulo(60,60,60)

if mi_triangulo.comprobar_angulos():
    print("La suma de todos los angulos es 180º !!!")
else:
    print("La suma de todos los angulos no es correcta!!")