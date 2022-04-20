"""#ejercicio1 
palabra = input("Decir Cadena por teclado: ")
cap = palabra.capitalize()
if palabra == cap: 
     print ("Empieza con Mayuscula")
else:
     print ("empieza con minuscula")"""
     
"""   # ejercicio 2    
numero = int(input("Escribi un numero"))
if numero > 0:
  print ("El numero es positivo")
  if numero % 2 == 0 :
       print ("Es numero par")
  else:
       print ("Es impar")
elif numero < 0 :
  print ("es negativo")
  if numero % 2 == 0 :
   print ("Es numero par")
  else:
       print ("Es impar")
else:
       print ("es 0 y par")     """
"""#ejercicio 3
numero = int(input("Elegi un numero del 1 al 6: "))
if 1 <= numero or numero <=6:
     print("La cara opuesta del dado  es : " + str(7 - numero))
else:
     print("numero ingresado incorrecto")"""
""" # ejercicio 4
paquete = int(input("Ingrese peso del paquete: "))
lugar = input("ingrese zona de entrega: ")
costos_ubicacion = {"America del sur" : "10usd","America Central": "15usd","America del Norte": "18usd","Europa":"24usd","Asia":"30"}
if paquete >5:
     print("Paquete rechazado")
else :
     print ("El costo de entrega es: " + costos_ubicacion[lugar]) """
     #ejercicio 5
numero = int(input("Deci un numero del 1 al 7: ")) 
dias_de_semana = {1 :"Lunes", 2: "Martes", 3 : "Miercoles",4:"Jueves", 5 : "Viernes", 6 :"Sabado",7 : "Domingo"}

if numero >=1 or numero <= 7:
     print(dias_de_semana[numero])
else:
     print("Numero incorrecto")