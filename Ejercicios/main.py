from Persona import Persona


persona = Persona("Pedro","Perez",23)

persona.saludar()

if persona.edad > 18:
    print("Eres mayor de edad broo")
elif persona.edad == 20:
    print("Eres un chucha")
else:
    print("Eres menor weon")