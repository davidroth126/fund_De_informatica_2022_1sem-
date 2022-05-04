""""".read() Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.

.readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa.

.readlines() Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista."""

#ej1 Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
"""def ocu(letra):
    ocurrencias=[]                  
    with open("david.txt", "r") as file:
        for linea in file.readlines():
            if linea[0] != letra:           
                ocurrencias.append(linea)  
    print(len(ocurrencias))  

print (ocu("P"))"""""
#ej 2  Escribí un programa que lea un archivo e imprima las primeras n líneas.
"""def imprimir_n(archivo,n):
    with open(archivo,"r") as file:
      for linea in range(n):
        print(file.readline())

print(imprimir_n("david.txt",2))"""
#ej 3  Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas
"""def leer_ar(archivo,n):
    with open (archivo,"r") as file:
      print(file.readlines()[-n:])      

print(leer_ar(".\david.txt",2))"""""
#ej 4 Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
"""def leer_pala(archivo):
    with open(archivo,"r") as file:
        linea = file.read()
        palabras = linea.split()
        return len(palabras)

print(leer_pala("david.txt"))"""""
#ej 5 Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.
"""def reemplaz(archivo,letra):
    import re
    with open (archivo,"r") as file:
        linea = file.read()
        lineas = linea.replace(letra,letra + "\n")
        with open("archivo_2","w")as file2:
         file2.write(lineas)
print(reemplaz("david.txt","P"))         
"""""
#ej 6 Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.


"""def elimin_esp (archivo):
    import re 
    with open (archivo,"r") as file:
        leer = file.read()
        eliminar_salt = leer.replace(" ","")
        with open("archivo2","w") as file2:
            file2.write(eliminar_salt)
print (elimin_esp("david.txt"))     """""

#ej7 Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.



"""def palabra_larga(archivo):
    with open(archivo,"r") as file:
        palabra = file.read().split()
        longest = max(palabra,key=len)
        return print ("la lapabra mas larga es: ",longest, " con ", len(longest),"caracteres.")
print(palabra_larga("david.txt"))"""
#ej 8 Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.


"""def abrir_dos (archivo1,archivo2,archivo3):
    with open (archivo1,"r") as file1:
        leer1 = file1.read()
    with open (archivo2,"r") as file2:
        leer2 = file2.read()

    with open(archivo3,"a") as file3:
        file3.write(leer1) + file3.write(leer2)

print(abrir_dos("david.txt","archivo_2","archivo2"))"""
#ej 9 Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.


"""def frecuencia (archivo,palabra):
    with open(archivo,"r") as file:
        leer = file.read()
        palabras = leer.split()
        contador = 0 
        for i in range (len(palabras)):
            if palabras [i] == palabra:
                contador +=1
        return contador/len(palabras)    

print(frecuencia(".\david.txt","god"))"""""
#ej10 Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.
import os
import glob
def unir():
    os.chdir("..\Practicas") #para ir a la carpeta "practicas"
    lista_txt = glob.glob("*.txt") #para ir a todos los archivos que terminen en txt de la carpeta
    with open("./documento.txt","a") as salida: #abrimos un archivo que esta vacio en este caso.
        for txt in lista_txt:                   #para cada archivo que termina .txt en la carpeta.
            with open (txt,"r") as archivo:     #abrir el archivo,leerlo.
                salida.write(archivo.read())    #y lo escribimos en el doc vacio.
print(unir())                


# para abrir archivo y se cierra solo "with open("".\davidroth.txt", "r")as file:
# para leer un archivo : linea = "file.read()""
# para dividir un archivo por los espacios y te de la lista de las palabras,estas como elementos. : "palabras = linea.split()"

# .read() Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.

# .readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa.

#.readlines() Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista.

