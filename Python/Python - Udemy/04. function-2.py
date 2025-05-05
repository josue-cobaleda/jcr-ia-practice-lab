# Description: Funciones en Python
def information(nombre):
    print(f"soy {nombre}")

information("Ana Margarita Bustamante")

def information(Cargo):
    print(f"Soy {Cargo}")

information("ML engineer")

#Funciones con varios parámetros
def information(name):
    print(f"I am {name}")

information("Joshua")
information("Natalia")
information("Jonathan")

def information(name,position):
    print(f"I am {name} and I am {position}")

information("Joshua","Leader")
information("Natalia","Secretary")
information("Jonathan","Seller")

def information(name,position,age,place):
    print(f"I am {name} and I am {position}. I am {age}, and I live in {place}")

information("Joshua","a leader","31","Bogotá")
information("Natalia","a financial","27","Pradera")
information("Jonathan","a engineer","25","Florida")


#Parámetros por default
def information(name,position = "Unknown"):
    print(f"I am {name} and I am {position}")

information("Joshua","Leader")
information("Natalia","Secretary")
information("Jonathan")

mi_variable = "Sebastian" 
print("Hola", mi_variable)

