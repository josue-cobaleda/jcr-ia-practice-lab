def information(): 
     print("Hello, world! I am a data scientist and Machine Learning Engineer")
     print("I am a entrepreneur leader")

information()
information()
information()

#¿Cómo se lee el código?
#1. Voy a crear una función llamada information (que en este caso no recibe ningún parámetro o variable)
#2. Dentro de la función, escribo con print lo que tiene que ejecutar ya sea una operación matemática, una cadena de texto, etc.
#3. Al llamar la función le estoy indicando que ejecute lo que está dentro de ese llamado. 
#4. Al llamar la función 3 veces, se ejecutará las veces que solicito. 

#Función sin parámetros. Una función puede no tener parátros y aún así ejecutar una acción.
def say_hello():
     print("Hello, world!")

say_hello()

#Función con un parámetro. 
def say_hello(name):
     print(f"Hello, {name}!")

say_hello("Pastor")

