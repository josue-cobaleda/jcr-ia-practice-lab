#Qué son los objetos
#Los objetos son una colección de datos y funciones que actúan sobre esos datos.
#En python se utiliza algo llamado diccionarios, que son objetos que contienen datos y funciones.
#Un diccionario es una colección de datos que se accede por medio de una llave.

#Creando un diccionario simple
cancion = {
    'artista': 'Metallica', # llave: valor
    'cancion': 'Enter Sandman',
    'lanzamiento': 1991,
    'likes': 3000
}

print(cancion)

#Accediendo a los valores de un diccionario
print(cancion['artista'])

#Mezclar con un string
print(f"Estoy escuchando {cancion['cancion']} de {cancion['artista']}")

#Agregar nuevos valores 
#Si no exite lo agregará
cancion['playlist'] = 'Heavy Metal' #Al agregar se usa el = y no el :
print(cancion)

#Reemplazar valor existente
#Si existe lo reemplazará
cancion['cancion'] = 'Seek & Destroy'
print(cancion)

#Eliminar un valor
del cancion['lanzamiento']
print(cancion)

