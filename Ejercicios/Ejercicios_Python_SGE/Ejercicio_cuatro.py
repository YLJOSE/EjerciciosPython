#4.	Escribe una función que reciba una lista como parámetro y
# devuelva la suma de la lista, así como el número mayor y el menor.

def devolver_suma(list):
    suma =0
    for  i in list:
     suma += i
     list.sort()
    print(f"La suma total es: {suma} y el numero menor es: {list[0]} y el numero mayor es: {list[-1]}")

    
   

devolver_suma([1,2,3])
        