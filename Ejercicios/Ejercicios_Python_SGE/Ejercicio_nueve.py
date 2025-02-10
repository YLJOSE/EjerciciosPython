# 9.	Escribe una función llamada histograma que reciba una lista de enteros
# y dibuje un histograma en pantalla. Por ejemplo, histograma ([4,9,7]) 
# debe imprimir esto por pantalla:
# 

def histograma(lista):
    for numero in lista:
        print('*' * numero)


histograma([4, 9, 7])