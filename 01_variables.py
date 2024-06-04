#My variables
#Python no compila interpreta
MyVariable = "My String Variable"
print(MyVariable)

#snake case, manera correcta
my_variable = "string"

my_int_variable= 6
my_bool_variable = False
print(type(my_int_variable))

#Print puede llevar diferentes argumentos, Concatenacion de variables
print(MyVariable, my_variable)

print(my_variable, str(my_int_variable))
print("Este es el valor de:", my_variable)

# Algunas Funciones del sistema
print(len(my_variable)) # muestra 6 caracteres

#Variables en una sola linea . Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Ale", "Ocampo", "aleocampodev", 8
print("Me llamo:", name, surname, "Mi edas es:", age,"Y mi alias es:", alias)


#Example vaiable en una sola linea
"""
first_name= input('What is your name?')
age = input('how old are you? ')

print(first_name)
print(age)
"""

#Forzamos el tipo.. Python siempre se queda con el ultimo valor
address: str = "Mi direccion" # Esto esta mal, solo es un ejemplo
address: int = 32 # Aca le cambio el tipo
address= 67.8
print(address)