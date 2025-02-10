#7.	Escribe una función que reciba una lista y un número como parámetro de entrada
# y escriba por pantalla todos aquellos que sean menor que el número, el cual será
# dado por el usuario.
#################
# Modifica la función para que almacene todos estos valores en una 
# lista nueva y la devuelva

def devolver_menor_que(list,numero):
    
    for i in list:
        if i < numero:
            print(i)
    
    
def devolver_menor_que_lista(list,numero):
    list2 = []
    for i in list:
        if i < numero:
         list2.append(i)  
    return list2

numero = input("Ingresa un numero: ")

devolver_menor_que([1,2,3,4,5,10],int(numero))

numero2 = input("Ingresa un numero: ")
print(devolver_menor_que_lista([1,2,3,4,5,10],int(numero2)))