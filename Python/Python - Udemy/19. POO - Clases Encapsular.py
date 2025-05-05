class Restaurant: 

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria 
        self._precio = precio #Default: Public, Protected (guion bajo), private (doble guion bajo)

    def mostrar_informacion(self): 
        print(f"Nombre: {self.nombre}, categoría: {self.categoria}, Precio: {self._precio}")

#Instanciar la clase
restaurant = Restaurant("Pizzeria", "comida italiana", 50)
print(restaurant._precio) 
restaurant._precio = 80 
restaurant.mostrar_informacion()

restaurant2 = Restaurant("Hamburguesería", "Comida casual", 20)
print(restaurant2._precio)
restaurant2._precio = 40 
restaurant2.mostrar_informacion()

#Abstraccion: son los datos necesarios de una clase, se evitan los datos innecesarios. 

#Encapsulamiento: evita hacer modificaciones de algún tipo. Permite restringir u ocultar el acceso a los datos dentro de la misma clase en el mundo exterior. 
