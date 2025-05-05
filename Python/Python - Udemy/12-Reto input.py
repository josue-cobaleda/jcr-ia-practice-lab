#Realiza un examen con 3 preguntas que que desees, el usuario deberá responder con "Si" o "No" y al final otorgarle una calificación
#La calificación se logra con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1
#Al final mostrar la calificación del usuario

# Examen de 3 preguntas con respuestas "Si" o "No"

# Inicializar la calificación en 0
score = 0

# Pregunta 1
answer1 = input("¿Python es un lenguaje de programación? (Si/No): ").strip().lower()
if answer1 == "si":
    score += 1

# Pregunta 2
answer2 = input("¿El sol es un planeta? (Si/No): ").strip().lower()
if answer2 == "no":
    score += 1

# Pregunta 3
answer3 = input("¿2 + 2 es igual a 4? (Si/No): ").strip().lower()
if answer3 == "si":
    score += 1

# Mostrar la calificación final
print(f"Tu calificación final es: {score}/3")