# 5.Dados los ficheros primenumbers.txt y happynumbers.txt,
# devuelve una función que devuelva todos los números que estén en ambos ficheros.
# Cuando tengas la función, haz que se almacenen los números en otro fichero llamado overlapping.txt.

def devolver_fichero_unido(nombre_archivo,nombre_archivo_dos):
    union= ""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
            union += texto
    
        with open(nombre_archivo_dos,'r',encoding='utf-8') as archivo_dos:
            texto_dos = archivo_dos.read()
            union += texto_dos
            
        print(union) 
        with open('Ejercicios/overlapping.txt','w', encoding='utf-8') as fichero_final:
            fichero_final.write(union)
           # texto_tres = fichero_final.read()
           # print(texto_tres)
        
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    

devolver_fichero_unido("Ejercicios/primenumbers.txt","Ejercicios/happynumbers.txt")