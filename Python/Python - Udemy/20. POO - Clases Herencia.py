class Restaurant: 

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria 
        self.__precio = precio #Default: Public, Protected (guion bajo), private (doble guion bajo)

    def mostrar_informacion(self): 
        print(f"Nombre: {self.nombre}, categoría: {self.categoria}, Precio: {self.__precio}")

    # GETTERS y SETTERS - Get = obtiene un valor, SET = Agrega un valor
    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio 

# Crear una clase hijo de restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel("Hotel POO", "5 Estrellas", 200)
hotel.mostrar_informacion()


#Herencia: puedes crear una clase que sea hijo o una copia de otra, al hereedar una clase tendrás todos los métodos y atributos de la clase padre en el hijo, y podrás modificarlos en caso de ser necesario.

#Polimorfismo: es la habilidad de tener diferentes comportamientos basado en qué subclase se está utilizando. 

