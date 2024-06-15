otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
prueba_curso = 1.5
# crudos
crudo_promedio = 5
crudo_prueba = 3.5
# diferencias de duracion
diferencia_min = 100 - prueba_curso / otros_cursos_min * 100
diferencia_max = 100 - prueba_curso * 1000 // otros_cursos_max / 10
diferencia_promedio = 100 - prueba_curso / otros_cursos_promedio * 100
print(f"El curso de prueba dura: {diferencia_min}% menos que el mas rapido")
print(f"El curso de prueba dura: {diferencia_max}% menos que el mas rapido")
print(f"El curso de prueba dura: {diferencia_promedio}% menos que el mas rapido")
# tiempo vacio promedio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio /10
print(f"un curso promedio elimina un{ tiempo_vacio_promedio}% de tiempo vacio")
