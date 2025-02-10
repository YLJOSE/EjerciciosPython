# 1.	Escribe una función que, dada una lista, devuelva otra lista con
# dos elementos, el primero y el último de la lista introducida como parámetro.




def ejercicio_uno(lista):
    
    lista_return =[lista[0]]
    
    lista_return.append(lista[-1])
    
    return lista_return
    
    
print(ejercicio_uno([1,2,3,4,5]))