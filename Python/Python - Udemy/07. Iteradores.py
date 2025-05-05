lenguajes = ['Python', 'C', 'Java', 'JavaScript', 'PHP', 'Ruby', 'Rust', 'Go', 'Swift', 'Kotlin']

print(lenguajes[0])
print(lenguajes[1])
print(lenguajes[2])
print(lenguajes[3])
print(lenguajes[4])

#Cuando consultas una base de datos y tienes 100 o 500 productos, lo más probable es usar un iterador. 

#Iterador
for lenguaje in lenguajes:
    print(lenguaje)

#Ejemplo con string
for lenguaje in lenguajes: 
    print(f'Estoy aprendiendo {lenguaje}')

#For que escriba números
for numero in range(10): #Empieza en 0 y termina en 9
    print(numero)

#For que escriba números de 2 en 2
for numero in range(1, 10, 2): #Empieza en 1, termina en 10 y va de 2 en 2 
    print(numero)  


