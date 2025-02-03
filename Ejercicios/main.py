from Persona import Persona


persona = Persona("Pedro","Perez",23)

persona.saludar()

if persona.edad > 18:
    print("Eres mayor de edad broo")
elif persona.edad == 20:
    print("Eres un chucha")
else:
    print("Eres menor weon")

# nuevo
print("nuevo\n" * 3)

luchador = """el primo"""

print(luchador)
print(luchador[3])
print(luchador[3:7])
print(luchador[2:])
print(luchador[:5])
print(luchador[-1])
print(luchador.upper())
print(luchador.lower())


print("Examen de marlene es el 21!!!")

nombre= "carlos"
nombre = nombre + "sds"
print(nombre)

#combinacion de datos
list =[1,2,"Once",True,False]
print(list)

list[0]= "uno"

list.append(False)

print(list)

list.remove(False)
print(list)

list.pop()
print(list)

# pedir datos usuario y castear 

edad = input("Ingresa tu edad bro?")

int_edad = int(edad)

if persona.edad > 18:
    print("Eres mayor de edad broo")
elif persona.edad == 20:
    print("Eres un chucha")
else:
    print("Eres menor weon")
valor =0
numero=10
#while
while valor < numero:
    print("Hello world!!")
    valor +=10

for i in range(10):
    print(i)
    
    
list2 = ["uno","dos", "Tres","cuatro"]
for text in list2:
    print(text)
    print( "El texto anterior tiene: ", len(text) , " caracteres")
    
for i in range(10,15):
    print(i)

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} es igual a {x} * {n//x}")
            break
    else:
        print(f"{n} es primo")


for n in range(2,10):
    if n % 2 == 0:
        print(f"el numero {n} es par")
        continue
    print(f"{n} es primo")