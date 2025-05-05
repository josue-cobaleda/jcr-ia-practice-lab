#1. Crea una función llamada greet() que devuelva "Hello, world!" y luego imprímelo.
def greet():
    print("Hello, World!")

greet()

#2. Crea una función llamada favorite_food(food) que reciba un nombre de comida y devuelva una frase diciendo cuál es tu comida favorita.
def favorite_food(food_name):
    return f"My favorite food is {food_name}"

print(favorite_food("pizza"))

def favorite_food(food_name):
    print(f"My favorite food is {food_name}")

favorite_food("pizza")

#3. Crea una función llamada double_number(number) que reciba un número, lo duplique y devuelva el resultado.
def double_number(number):
    return number * 2

print(double_number(5))

#4. Crea una función llamada full_name(first_name, last_name) que reciba un nombre y un apellido, los junte en una sola cadena y los devuelva.
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(full_name("Josué", "Cobaleda"))


def full_name(first_name, last_name):
	return first_name + " " + last_name

print(full_name("Josué","Cobaleda Rosero"))

#5. Crea una función llamada age_in_dog_years(age) que reciba una edad y la convierta a años perrunos (multiplicando por 7) antes de devolverla.
def age_in_dog_years(age):
	return age * 7

print(age_in_dog_years(13))

#6.Crea una función llamada add_three_numbers(a, b, c) que reciba tres números, los sume y devuelva el resultado.
def add_three_numbers(a, b, c): 
	return a + b + c

print(add_three_numbers(5, 6, 7))

#7. Crea una función que reciba tres números y devuelva el promedio de esos números.
def average(a, b, c): 
	return (a + b + c) / 3

print(average(50,10,2))

#8. Crea una función llamada shout(phrase) que reciba una frase y la devuelva en mayúsculas.   
def shout(phrase):
    return phrase.upper()

print(shout("hello, world!"))

#9. Crea una función llamada whisper(phrase) que reciba una frase y la devuelva en minúsculas.
def whisper(phrase):
    return phrase.lower()

print(whisper("HELLO, WORLD!"))

#10. Crea una función llamada is_even(number) que reciba un número y devuelva True si el número es par o False si es impar.
def is_even(number):
    return number % 2 == 0

print(is_even(8))

def is_even(number):
    return number % 2 == 1

print(is_even(7))

#11. Crea una función llamada repeat_word(word) que reciba una palabra y la devuelva tres veces repetida en una misma cadena.
def repeat_word(word):
    return word * 3 

print(repeat_word("hello "))

#12.  Crea una función llamada currency_converter(dollars) que reciba una cantidad en dólares y la convierta a pesos colombianos (usa una tasa de cambio fija).
def currency_converter(dollars):
    return dollars * 3800

print(currency_converter(100))

#13. Crea una función llamada multiply_string(text, times) que reciba un texto y un número, y devuelva ese texto repetido la cantidad de veces indicada.    
def multiply_string(text, times):
    return text * times

print(multiply_string("hello ", 5))

#Ejercicios con Números

#14.  Crea un programa que pida al usuario dos números, los sume y muestre el resultado.
def suma(a, b):
    return a + b

print(suma(5, 6))

#15. Escribe una función es_par(n) que devuelva True si el número es par y False si es impar.
def es_par(n):
    return n % 2 == 0

print(es_par(8))

#16. Escribe una función es_impar(n) que devuelva True si el número es impar y False si es par.
def es_impar(n):
    return n % 2 == 1

print(es_impar(6))

#17. Crea un programa que multiplique un número por sí mismo 3 veces 
def potencia(number): 
	return number**3

print(potencia(4))

#18.  Crea una función que reciba un número y devuelva su factorial (ej.: 5! = 5x4x3x2x1).
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

#19. Crea una función que reciba un número y devuelva True si es primo o False si no lo es.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))

#20. Escribe un programa que convierta grados Celsius a Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

print(celsius_to_fahrenheit(0))

#21. Pide un número al usuario y muestra la tabla de multiplicar del 1 al 10.
def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

tabla_multiplicar(1993)

#22.  Crea una función que reciba dos números y devuelva el mayor de ellos.
def mayor(a, b):
    if a > b:
        return a
    else:
        return b

print(mayor(5, 6))

#23. Crea una función que reciba dos números y devuelva el menor de ellos.
def menor(a, b):
    if a < b:
        return a
    else:
        return b

print(menor(5, 6))

#24. Crea una función que reciba un número y devuelva True si es positivo, False si es negativo.
def is_positive(n):
    return n > 0

print(is_positive(5))

#25. Crea una lista con 5 nombres y usa un print() para mostrar el tercer nombre.
nombres = ['Josué', 'Pastor', 'Eduardo', 'Jorge', 'Luis']
print(nombres[2])

#26. Crea una lista con 5 nombres y usa un for para mostrar cada uno de los nombres.
nombres = ['Josué', 'Pastor', 'Eduardo', 'Jorge', 'Luis']
for nombre in nombres:
    print(nombre)

#27. Añade un nuevo elemento a la lista anterior con .append() y muéstrala.
nombres = ['Josué', 'Pastor', 'Eduardo', 'Jorge', 'Luis']
nombres.append('Carlos')
print(nombres)

#28. Añade un nuevo elemento a la lista anterior en la posición 2 y muéstrala.
nombres = ['Josué', 'Pastor', 'Eduardo', 'Jorge', 'Luis']
nombres.insert(2, 'Ana')
print(nombres)

#29. Usa .remove() para eliminar un elemento específico de la lista.
nombres = ['Josué', 'Pastor', 'Eduardo', 'Jorge', 'Luis']
nombres.remove('Jorge')
print(nombres)

#30. Ordena una lista de números de menor a mayor usando .sort().
numeros = [5, 3, 8, 1, 2]
numeros.sort()
print(numeros)

#31.  Crea una función que reciba una lista y devuelva el número más grande.
def max_number(numbers):
    return max(numbers)

print(max_number([5, 3, 8, 1, 2]))

#32. Crea una función que reciba una lista y devuelva el número más pequeño.
def min_number(numbers):
    return min(numbers)

print(min_number([5, 3, 8, 1, 2]))

#33. Crea un programa que cuente cuántas veces aparece un número en una lista.
def count_number(numbers, number):
    return numbers.count(number)

print(count_number([5, 3, 8, 1, 2, 5, 5], 5))

#34. Elimina el último elemento de una lista y guárdalo en una variable.
nombres = ['Josué', 'Pastor', 'Eduardo', 'Jorge', 'Luis']
ultimo_nombre = nombres.pop(4)
print(nombres)

#35. Crea un programa que reciba una lista de números y devuelva una nueva lista con solo los pares.
def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

print(even_numbers([5, 3, 8, 1, 2, 5, 5]))
