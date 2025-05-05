#For se ejecuta determinado número de ocasiones, segun sean los elementos de una colección (como una lista)
#While se ejecuta mientras una condición sea verdadera

pregunta = "Agrega un número y te diré si es par o impar: \r\n"
pregunta += "(Escribe 'cerrar' para terminar el programa) \r\n"

preguntar = True

while preguntar:

    #Díme un número y te diré si es par o impar
    numero = input(pregunta)

    if numero == "cerrar":
        preguntar = False #Terminar el programa dado que while se ejecuta cuando una condición es verdadera
    else:
        numero = int(numero)

        if numero % 2 == 0:
            print("Es par")
        else:
            print("Es impar")
