#  Crea una clase llamada papeo. Tiene un atributo, menú, un String.
#  Crea un método llamado precio_menu, que devolverá 12.50 si el menú es “Vegetariano”,
#  9.90 si el menú es “para pobres” y 50 si el menú es “Ferrá Adriá”.
class papeo:
    def __init__(self,menu):
        self.menu = menu
    
    def precio_menu(self):
        match self.menu:
            case 'Vegetariano':
                return 12.50
            case 'Para pobres':
                return 9.90
            case 'Ferrá Adriá':
                return 50
            
mi_papeo = papeo('Vegetariano')
print(f"El precio de la comida {mi_papeo.menu} es: {mi_papeo.precio_menu()}")