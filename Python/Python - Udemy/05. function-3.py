#Function return value
def information (name):
    return name

employee = information("Joshua")
print(employee)
 
# return devuelve un valor, en lugar de solo imprimirlo.
# Podemos guardar ese valor en una variable para usarlo después.
# Usar return es útil cuando queremos hacer cálculos o transformar datos antes de usarlos.

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  

#Ejemplo de juntar nombres
def add_names(name, last_name):
    return name + " " + last_name

complete_name = add_names("Joshua", "García")
print(complete_name)

#
