#Revisando 2 o más condiciones
#if y elif revisarán que se cumpla una condición
#Algunas veces requieres código que se cumplan 2 o más condiciones, o que se cumpla al menos una de ellas

#Operadores AND y OR
#AND: Revisa que se cumplan todas las condiciones
#OR: Revisa que se cumpla al menos una condición

usuario_logueado = True
usuario_admin = False 

if usuario_logueado and usuario_admin:
    print("Administrador logueado")
elif usuario_logueado: 
    print("Usuario logueado")
else:
    print("Debes iniciar sesión como administrador")

usuario_logueado = False
usuario_admin = False


if usuario_logueado or usuario_admin:
    print("Administrador logueado")
elif usuario_logueado: 
    print("Acceso al sistema")
else:
    print("Debes iniciar sesión")