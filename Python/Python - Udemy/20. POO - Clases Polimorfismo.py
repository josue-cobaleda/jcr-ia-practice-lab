class Restaurant: 

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #Atributo
        self.categoria = categoria 
        self.precio = precio #Default: Public, Protected (guion bajo), private (doble guion bajo)

    def mostrar_informacion(self): 
        print(f"Nombre: {self.nombre}, categoría: {self.categoria}, Precio: {self.precio}")

    # GETTERS y SETTERS - Get = obtiene un valor, SET = Agrega un valor
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio 

# Crear una clase hijo de restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, __categoria, precio)
        self.alberca = alberca

    #Reescribir un método:
    def mostrar_informacion(self): 
        print(f"Nombre: {self.nombre}, categoría: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}")


    #Agregar un método que solo exista en hotel
    def get_alberca(self):
        return self.alberca 

hotel = Hotel("Hotel POO", "5 Estrellas", 200, "Si")
hotel.mostrar_informacion()
alberca = hotel.get_alberca()
print(alberca)


#Herencia: puedes crear una clase que sea hijo o una copia de otra, al hereedar una clase tendrás todos los métodos y atributos de la clase padre en el hijo, y podrás modificarlos en caso de ser necesario.

#Polimorfismo: es la habilidad de tener diferentes comportamientos basado en qué subclase se está utilizando. 

