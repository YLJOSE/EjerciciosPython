# lista(List) con combinacion de tipos de datos (* en java no se puede)/ se puede repetir los datos
lista = ["Juan Jose", "Manayay Rojas", True,1.70]
print(lista)
# pedir nº de elemento de la lista
print(lista[0])
# tuplas: conjunto de datos estaticos que nunca se puede modificar / se puede repetir los datos
tupla =("Jose", "Rojas", True,1.70)
print(tupla)
# lista si se puede modificar : tupla no se puede modificar
lista[3]=1.71
# conjunto(SET) es modificable / no permite repetir valores / no se accede con un indice 
# te muestra los datos de manera random
conjunto ={"Jose", "Rojas", True,1.70}
print(conjunto)
# creando un diccionario (dict) /
# se almacenan variables y valores respectivos pero con comillas simples
# como indice para solicitar un valor se brinda el nombre de la variable
diccionario={
    'nombre' : 'pedro',
    'apellido' : 'cabrera',
    'edad' : '19',
    'esta_emocionado' : True,
    'estatura' : '1.70',
    'nombre_duplicado' : 'pedro'
}
print(diccionario['nombre'])