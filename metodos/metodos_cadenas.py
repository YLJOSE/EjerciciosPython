cadena1 = "Hola soy JuanJo"
cadena2 = "Bienvenido maquina"
# dir nos brinda los metodos que podemos utilizar por cada tipo de dato
resultado = dir(cadena1)
# print(resultado)
# convertir cadena en mayusculas como en java .toUpperCase()
resultado = cadena1.upper()
print(resultado)
# convertir cadena en minusculas como en java .toLowerCase()
resultado = cadena1.lower()
print(resultado)
# convertir primera letra en mayuscula y el resto en minuscula
resultado = cadena1.capitalize()
print(resultado)
# buscar un cadena en otra cadena, te retorna -1 cuando no encuentra algo
resultado = cadena1.find("Hola")
# tambien se utiliza pero si no encuentra algo te da una excepcion
# resultado = cadena1.index("9")
print(resultado)
# si es numerico retorna true
resultado = cadena1.isnumeric()
print(resultado)
# si es alfanumerico retorna true
resultado = cadena1.isalpha()
print(resultado)
# buscar una cadena en otra cadena y devuelve la cantidad de veces que se repite
resultado = cadena1.count("a")
print(resultado)