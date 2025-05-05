#operadores que se pueden utilizar para evaluar una condición: 
#== igual a 
#!= diferente de
#> mayor que
#< menor que
#>= mayor o igual que
#<= menor o igual que

#Revisar si una condición es mayor a
balance = 500
if balance > 0:
    print("Puedes pagar")

#if... else...
# Si una condición es evaluada como verdadera se ejecuta el bloque de código 
# que está debajo de la condición, si no se cumple la condición se ejecuta el
# bloque de código que está debajo de la palabra reservada else

balance = 0
if balance > 0:
    print("Puedes pagar")
else:
    print("No tienes saldo")

#Likes
likes = 200
if likes == 200:
    print("Excelente, 200 Likes")

likes = 100
if likes >= 200:
    print("Excelente, 200 Likes")
else:
    print("Casi llegas a los 200")

#If con texto 
lenguaje = "python"
if lenguaje == "python":
    print("Excelente, Python es un lenguaje de programación")

lenguaje = "PHP"
if not lenguaje == "python":
    print("Excelente, Python es un lenguaje de programación")
    
#Evaluar un Boolean 
usuario_autenticado = True
if usuario_autenticado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesión")


#Evaluar un elemento de una lista
lenguajes = ['Python', 'JavaScript', 'PHP']
if 'PHP' in lenguajes:
    print("PHP es uno de los lenguajes de programación")
else:
    print("No se encontró PHP")

#IF anidados 
usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print("Acceso total")
    else:
        print("Acceso al sistema")
else:
    print("Debes iniciar sesión")

