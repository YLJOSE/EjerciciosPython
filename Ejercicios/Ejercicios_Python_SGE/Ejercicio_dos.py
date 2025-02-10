#2.	Escribe un programa que imprima por pantalla todos los números que son divisibles por 7 y
# no por 5 entre 2000 y 3200 (ambos incluidos). Los números tienen que estar escritos en la 
# misma línea separados por comas (investiga el parámetro end de print())


def imprimir_numeros_divisibles_por_7():
    
    for i in range(2000,3200):
        
        if i % 7 == 0:
            if i % 5 !=0:
                print(i,end=" ")
            
            

imprimir_numeros_divisibles_por_7()