class Dataset:
    def __init__(self, nombre, edad, enfermedad):
        self.nombre = nombre
        self.edad = edad
        self.enfermedad = enfermedad

    def mostrar_info(self):
        return f"Paciente: {self.nombre}, Edad: {self.edad}, Diagnóstico: {self.enfermedad}"

# Crear objetos (instancias) de la clase Dataset
paciente1 = Dataset("Carlos", 45, "Diabetes")
paciente2 = Dataset("Ana", 60, "Hipertensión")

# Imprimir información
print(paciente1.mostrar_info())
print(paciente2.mostrar_info())









from sklearn.linear_model import LinearRegression

# Crear un objeto (modelo de regresión lineal)
modelo = LinearRegression()

# Entrenar el modelo con datos
modelo.fit([[1], [2], [3]], [2, 4, 6])

# Hacer una predicción
prediccion = modelo.predict([[4]])

print(prediccion)  # Resultado esperado: [8]
