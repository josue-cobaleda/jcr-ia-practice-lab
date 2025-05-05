#IF... ELIF... ELSE...
# Se utiliza cuando se tienen varias condiciones que evaluar
# Si la primera condición es verdadera se ejecuta el bloque de código
# En python se conoce como elif, en otros lenguajes se conoce como else if

ocupacion = "Nada"

if ocupacion == "Estudiante":
    print("Tienes un 50% de descuento")
elif ocupacion == "Jubilado":
    print("Tienes un 75% de descuento")
elif ocupacion == "Desempleado":
    print("Tienes un 10% de descuento")
else:
    print("No tienes descuento")

