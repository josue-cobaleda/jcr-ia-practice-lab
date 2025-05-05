class Restaurant: 

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria 
        self.precio = precio 

    def mostrar_informacion(self): 
        print(f"Nombre: {self.nombre}, categoría: {self.categoria}, Precio: {self.precio}")

#Instanciar la clase
restaurant = Restaurant("Pizzeria", "comida italiana", 50)
print(restaurant.precio)
restaurant.precio = 80 
restaurant.mostrar_informacion()

restaurant2 = Restaurant("Hamburguesería", "Comida casual", 20)
print(restaurant2.precio)
restaurant2.precio = 40 
restaurant2.mostrar_informacion()

#Abstraccion: son los datos necesarios de una clase, se evitan los datos innecesarios. 

