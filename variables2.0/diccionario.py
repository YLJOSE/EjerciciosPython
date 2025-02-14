# crear diccionario con dict()
diccionario = dict(nombre="juanjo", apellido="rojas")
print(diccionario)
# otra forma de crear diccionario es:
#{
#    'nombre' : 'juanjo'
#    'apellido' : 'rojas'
#}
# las listas no pueden ser claves, las tuplas si

# crear diccionarios, las listas no pueden ser claves y usamosfrozemset para meter conjuntos 
diccionario_dos = {frozenset(["junjo", "rojas"]) ,"jajaja"}
print(diccionario_dos)
# diccionario fromkeys() con valor por defecto : none
diccionario_tres = dict.fromkeys(["nombre","apellidio"])
print(diccionario_tres)
# diccionario fromkeys() con valor por defecto : "no se"
diccionario_cuatro = dict.fromkeys(["nombre","apellido"], "no se")
print(diccionario_cuatro)

print("----------------------------")
# Diccionario

persona = {"nombre":"Jose","edad":"23","ciudad":"Madrid"}
# Para acceder a los valores del diccionario se utiliza la clave correspondiente entre corchetes
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
# Metodo para solo obtener el valor de la clave brindada
print(persona.get("nombre"))

# Metodos del diccionario
print(persona.keys()) # Retorna las claves del diccionario
print(persona.values()) # Devuelve los valores del diccionario
print(persona.items()) # Imprime clave : valor respectivamente
persona.update({"profesion":"desarrollador"}) # Actualiza el diccionario al final 
print(persona) # Imprime el diccionario completo