#6.	Escriba una función que devuelva el factorial de un número pasado como parámetro. 
#Dicho número se le tiene que pedir al usuario. (Pista: el factorial de un número es la 
# multiplicación de todos los números hasta él. El factorial de 5 es 5 * 4* 3 * 2 * 1)



def devolver_factorial(numero):
    i =0
    while i <= numero:
        if numero - i > 0 :
            print(numero - i,end=" * ")
        i=i+1

numero = input("Ingresa el numero para obtener el factorial: ")

devolver_factorial(int(numero))
    