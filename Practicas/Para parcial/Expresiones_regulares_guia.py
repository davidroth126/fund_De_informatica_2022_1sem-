import re
#1 Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
"""def caracter_permitido(string):
    return bool(re.search("[\w]", string))

print(caracter_permitido("hola"))"""""
#2 Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
"""def todos_permitidos(string):
    return bool(re.search("[\W_]",string)) is none

print(todos_permitidos("hola"))
print(todos_permitidos("hola!"))"""""
#3Creá un programa que verifique las siguientes condiciones:

#si un string dado tiene una h seguida de ninguna o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de dos o tres e.
"""def condiciones(string):
    return bool(re.search("(he*)",string))

print(condiciones("hele"))  
print(condiciones("beleee"))  
print(condiciones("hola"))  """""

#4 Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
"""def encontrar(string):
    return re.findall("(\w*)[_](\w*)",string)

print (encontrar("david_roth"))  
print (encontrar("david_roth, el pibe de barrio, pibe_valde"))    
print (encontrar("todo bien?"))    
print (encontrar("david"))   """""

#5 Escribí un programa que diga si un string empieza con un número específico.
"""def diga(string,numero_espe):
    return bool(re.search(str(numero_espe),string))

print (diga("1hola",1))    
print (diga("2hola",1))  """

#6 no lo termine 
"""def verify(lista,frase):
    return (re.findall(lista,frase))"""""

#7 pq se usa el not bool? y el "^"

#consigna Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

"""def solamente(string):
    return not bool(re.findall("^\w\s",string))

print(solamente("hola"))"""""

#8 Escribí un programa que separe y devuelva los caracteres númericos de un string.
"""def separar(string):
    return (re.findall("\d",string))

print (separar("hola soy david, tengo 20 años hoy es 3 de mayo"))"""

#9 Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
"""def extraiga (string):
    return (re.findall("-(.*?)-",string))

print(extraiga("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))"""

#10 Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
"""def substring (string):
    lista = re.findall("[@|&](.*?)[@|&]",string)
    lista2 = []
    for i in lista:
        lista2.append(string.index(i))
    return lista,lista2

print(substring("hola @mi nombre es dav& teng&45 años@"))"""""

#11 Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
"""lista3 = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
    
def prog (lista):
    lista_pp = []
    for i in lista:
        if re.findall("(P\S*)\s(P\S*)",i):
            lista_pp.append(i)
    return lista_pp

print(prog(lista3))   """""
#12 Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).
"""def progra(string):
   return (re.sub("[\s_:]"),"|",string)


print(progra("hola_todo. bien vos:"))"""
#13 Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
def reemplazanding(string):
   print(re.sub("(\W{2+})","__",string))

print(reemplazanding("¡sos flaco?"))

#14  Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.


"""def program (string):
    return(re.sub("[\s\t]",";",string))

print(program("uno se rie pero es verdad"))"""""

#15 Realizá un programa que validar si una cuenta de mail está escrita correctamente.


"""def validar_mail (string):
    return bool(re.search("[a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]+@[a-zA-Z]{2,9}(\.[a-zA-z]{2,4})",string))

print(validar_mail("davidroth126@gmail.com"))   """"" 
