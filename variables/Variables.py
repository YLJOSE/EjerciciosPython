a=4
b=5
c= a+ b
print(c)
# en este caso se ha modificado la variable de tipo string hasta que su valor final es "carlitos"
nombre="JuanJo"
nombre="Pedro"
nombre="Carlitos"
print(nombre)
# resultado final despues de modificar la variable es 20
numero=5
numero=10 + 1
numero=15
numero +=5
print(numero)
# concatenar variable string
nombrePersona="Jose"
bienvenida="Hola " + nombre + " Cómo estás?"
print(bienvenida)
# concatenar variable string con int dentro se utilizaria el formato FSTRING para que int se pueda leer
# el dato concatenado dentro del string se convierte a texto
edad =20
decirEdad=f"Hola tu edad es: {edad} verdad?."
print(decirEdad)
# eliminar variables
edad=15
del edad
# buscar texto en una variable string : el resultado será boolean
texto="Hola como estas?"
print("ola" in texto) # true
print("pero" not in texto) # true
# variable con camelCase
nuevaVariable="pedro"
# variabale con snake_case
nueva_variable="carlitos"
