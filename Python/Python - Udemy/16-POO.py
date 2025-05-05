#Programación orientada a objetos (POO) 
#La Programación Orientada a Objetos (POO) es un estilo de programación en el que organizamos el código en objetos, los cuales tienen características (atributos) y acciones (métodos o comportamientos).

#Clase: Es el molde o plano de un objeto. Define qué características y comportamientos tendrá.
    #Ejemplo: Car define que todos los carros tendrán color, marca y pueden acelerar().

#Objeto: Es una "cosa" creada a partir de una clase. 
    #Ejemplo: carro1 = Car("Rojo", "Toyota"), carro2 = Car("Azul", "Ford").

#Instancia de una clase: Es cuando creamos un objeto basado en una clase.
    #Ejemplo: mi_coche = Car("Negro", "Tesla") crea una instancia de Car.

#Atributos: Son las características de un objeto (variables dentro de la clase).
    #Ejemplo: color, marca, velocidad del carro.

#Métodos (Comportamientos): Son las acciones que puede hacer el objeto (funciones dentro de la clase).
    #Ejemplo: acelerar(), frenar(), pitar().

class Restaurant: 

    def agregar_restaurant(self, nombre):
        self.nombre = nombre #Atributo

    def mostrar_informacion(self): 
        print(f"Nombre: {self.nombre}")

#Instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant("Pizzeria")
restaurant.mostrar_informacion() 

restaurant2 = Restaurant()
restaurant2.agregar_restaurant("Hamburguesería")
restaurant2.mostrar_informacion()

print(f"Nombre Restaurant: {restaurant.nombre}")
print(f"Nombre Restaurant: {restaurant2.nombre}")