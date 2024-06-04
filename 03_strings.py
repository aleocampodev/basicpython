my_string= "my string"
my_order_string = "my order string"

print(len(my_string))
print(len(my_order_string))

print(my_string + " " + my_order_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un string con \\n escapado" #\\t no quiere que ejecute tabulacion le agrego doble linea
print(my_scape_string)

#Formateo
name, surname, age = "Brais", "Moure", 35
#print("Mi nombre es %s %s y mi edad es %s".format(name, surname, age))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #manera correcta
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) #%d es para enteros
print(f"Mi nombre es {name} {surname} y mi edad es {age}") #f sirve para formatear

#Desempaquetado de caracteres
language = "python"
#a,b = language
#print(a) -> muestra error
a, b, c, d, e, f = language
print(f)
print(e)
print(d)
print(c)
print(b)
print(a)

#Division
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:2:4] #[start: stop: step]
print(language_slice,"ju")

language_slice = language[0:6:2] #[start: stop: step]
print(language_slice)

#Reverse
reversed_language = language[::-1]
print(reversed_language) #nohtyp el final empieza por -1 ya q no hay un -0 como tal

#Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric()) #False
print("1".isnumeric()) #True
print(language.lower()) 
print(language.lower().isupper()) #isupper es para comprobar si esta en mayuscula
print(language.startswith("py")) 
print("Py" == "py") #False




