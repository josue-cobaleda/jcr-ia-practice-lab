#Iniciar un diccionario vacio
Jugador = {}
print(Jugador)

#Se une un jugador
Jugador["Nombre"] = "Lionel Messi"
Jugador["Puntaje"] = 0
print(Jugador)

#Incrementar el puntaje
Jugador["Puntaje"] = Jugador["Puntaje"] + 100
print(Jugador)

#Incrementar el puntaje
Jugador["Puntaje"] += 100
print(Jugador)

#Acceder a un valor
print(Jugador.get("consola", "No existe ese valor"))

#Iterador en el diccionario
for key, value in Jugador.items():
    print(key, value)

#Eliminar jugador y puntaje
del Jugador["Nombre"]
del Jugador["Puntaje"]
print(Jugador)
