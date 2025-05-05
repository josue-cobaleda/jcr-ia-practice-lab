class Restaurant: 

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria 
        self.__precio = precio #Default: Public, Protected (guion bajo), private (doble guion bajo)

    def mostrar_informacion(self): 
        print(f"Nombre: {self.nombre}, categoría: {self.categoria}, Precio: {self.__precio}")

    # GETTERS y SETTERS - Get = obtiene un valor, SET = Agrega un valor
    def get_precio(self):
        print(self.__precio)

    def set_precio(self, precio):
        self.__precio = precio 

#Instanciar la clase
restaurant = Restaurant("Pizzeria", "comida italiana", 50)
#restaurant.__precio = 80 #No será posible modificarlo con Private __
restaurant.mostrar_informacion()
restaurant.get_precio()

restaurant2 = Restaurant("Hamburguesería", "Comida casual", 20)
restaurant2.mostrar_informacion()
restaurant2.get_precio()

#Abstraccion: son los datos necesarios de una clase, se evitan los datos innecesarios. 

#Encapsulamiento: evita hacer modificaciones de algún tipo. Permite restringir u ocultar el acceso a los datos dentro de la misma clase en el mundo exterior. 

