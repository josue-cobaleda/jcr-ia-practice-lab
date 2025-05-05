# Listas en Python
lenguajes = ['Python', 'C', 'Java', 'JavaScript', 'PHP', 'Ruby', 'Rust', 'Go', 'Swift', 'Kotlin']
print(lenguajes)

#Los listados en Python empiezan en la posición 0
print(lenguajes[0])

#Ordenar los elementos alfabéticamente
lenguajes.sort()
print(lenguajes)

#Ordenar los elementos alfabéticamente en reversa
lenguajes.sort(reverse=True)   
print(lenguajes)

#Acceder a un elemento dentro de un texto
lenguajes = ['Python', 'C', 'Java', 'JavaScript', 'PHP', 'Ruby', 'Rust', 'Go', 'Swift', 'Kotlin']
aprendiendo = f'Estoy aprendiendo {lenguajes[0]}'
print(aprendiendo)

#Modificando valores de una lista
lenguajes[0] = 'Python 3.13.1'
print(lenguajes)

#Agregar elementos a una lista
lenguajes.append('C#') 
print(lenguajes)

#Agregar elementos en una posición específica
lenguajes.insert(3, 'TypeScript') #Agrega TypeScript en la posición 3
print(lenguajes)

more_lenguajes = ['scala', 'Perl', 'Cobol']

#Agregar varios elementos a una lista
lenguajes.extend(more_lenguajes) #Permite agregar varios elementos de otra lista o estructura iterable.
print(lenguajes)
 
#Eliminar elementos de una lista
del lenguajes[9]
print(lenguajes)

fruits = ["apple", "banana", "cherry"] 
del fruits #Elimina la lista completa
#print(fruits) #Genera un error porque la lista ya no existe

#Eliminar el último elemento de una lista
lenguajes.pop() #Elimina el último elemento de la lista
print(lenguajes)

#Eliminar con pop una posición específica
index_php = lenguajes.index('PHP') #Obtiene la posición de PHP
removed_lenguajes = lenguajes.pop(index_php) #Elimina PHP de la lista
print(lenguajes)
print(removed_lenguajes) 

#Eliminar con remove un elemento específico
lenguajes.remove('Ruby')
print(lenguajes)


