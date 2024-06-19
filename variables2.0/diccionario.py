# crear diccionario con dict()
diccionario = dict(nombre="juanjo", apellido="rojas")
print(diccionario)
# otra forma de crear diccionario es:
#{
#    'nombre' : 'juanjo'
#    'apellido' : 'rojas'
#}
# las listas no pueden ser claves, las tuplas si

# crear diccionarios, las listas no pueden ser claves y usamosfrozemset para meter cnjuntos 
diccionario_dos = {frozenset(["junjo", "rojas"]) ,"jajaja"}
print(diccionario_dos)
# diccionario fromkeys() con valor por defecto : none
diccionario_tres = dict.fromkeys(["nombre","apellidio"])
print(diccionario_tres)
# diccionario fromkeys() con valor por defecto : "no se"
diccionario_cuatro = dict.fromkeys(["nombre","apellido"], "no se")
print(diccionario_cuatro)

