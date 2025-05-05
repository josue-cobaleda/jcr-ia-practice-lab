#Publicar en tu muro, realizar un examen en linea, subir una foto, solicitar un taxi, crear un evento, realizar un pago, son acciones que requieren entrada de datos por parte del usuario. 
#En python se pueden solicitar datos al usuario utilizando la función input().

#nombre = input("¿Cuál es tu nombre? \r\n")
#print(f"Hola {nombre}")

 # Leer datos que sean números
edad = input("¿Cuál es tu edad? \r\n")
#convertir edad string a entero (int)
edad = int(edad) #también existe float para convertir a decimal o str para convertir a texto

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Mezclarlo con operadores 
#Díme un número y te diré si es par o impar

numero = input("Díme un número: \r\n")
numero = int(numero)

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

