playlist = {} #Diccionario vacío
playlist['canciones'] = [] #Lista vacía de canciones

#Función principal
def app():
    #Agregar playlist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input("¿Cómo deseas nombrar la playlist? \r\n")
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            #Ya tenemos el nombre de la playlist, desactivar el true
            agregar_playlist = False #Esto se conoce como bandera, comienza el código con True y termina con False

            #Ahora llamar la función de agregar canciones
            agregar_cancion()

def agregar_cancion():
    #Bandera para agregar canciones
    agregar_cancion = True

    while agregar_cancion: 
        #Preguntar al usuario qué canciones desea agregar
        nombre_playlist = playlist["nombre"]
        pregunta = f"\r\n Agrega canciones para la playlist {nombre_playlist}: \r\n"
        pregunta += 'Escribe "X" para dejar de agregar canciones \r\n'

        cancion = input(pregunta)

        if cancion == "X":
            #Dejar de agregar canciones
            agregar_cancion = False

            #mostrar resumen de la playlist
            mostrar_resumen()

        else:
            #Agregar las canciones a la playlist
            playlist["canciones"].append(cancion)

def mostrar_resumen():
    nombre_playlist = playlist["nombre"] 
    print(f"Playlist: {nombre_playlist} \r\n")
    print ("canciones: \r\n")
    for cancion in playlist["canciones"]:
        print(cancion)

app()

