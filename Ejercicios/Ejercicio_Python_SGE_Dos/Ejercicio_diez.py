#Crea una clase Punto. Dicha clase tiene que tener:
#Un método __str__ que muestre las coordenadas de un punto
#Un método mover(x,y), que mueva las coordenadas
#Un método distancia(p,q) que muestre la distancia entre p y q.
#  Pista: La distancia entre dos puntos se representa por este ecuación

class punto:
    def __init__(self):
        self.x = 1
        self.y = 3
    def __str__(self):
        return f"Coordenadas en X= {self.x} y en Y= {self.y}"
    def mover(self,x,y):
        self.x = x
        self.y = y
        print(f"Coordenadas actualizadas en X= {self.x} y en Y= {self.y}")
    def distancia(self,p1,p2):
        print("revisar")


mi_punto = punto()

print(mi_punto.__str__())
mi_punto.mover(3,4)


