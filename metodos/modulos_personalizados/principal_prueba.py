import modulos
# de este paquete importamos los modulos o clases
from mi_paquete import modulo1, modulo2


modulo1.funcion1()
modulo2.funcion2()

#import operaciones
#import utilidades


#resultado = operaciones.sumar(5, 3)
#utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


#nombre = utilidades.obtener_nombre_usuario()
#utilidades.imprimir_mensaje(f"Hola, {nombre}!")

modulos.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = modulos.calcular_suma(5, 3)
print(resultado)  # Imprime 8