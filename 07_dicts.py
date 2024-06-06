## Diccionaries ##
my_dict = dict()
my_other_dict = {} # Parece un set pero en realidad lo que se tiene es un diccionario

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre": "Aleja",
    "Apellidos": "Ocampo",
    "Edad": 15,
    1: "Python"
}

my_dict = {
    "Nombre": "Aleja",
    "Apellidos": "Ocampo",
    "Edad": 15,
    "lenguajes":{"Python", "Javascript", "Java"},
    1: 1.77
}

print(my_dict["Nombre"])

my_dict["Nombre"] = "Sofia"
print(my_dict["Nombre"] )

print(my_dict[1])

print("Moure" in my_dict) #false
print("Apellido" in my_dict) #true

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
my_list = ["Nombre", 1, "Piso"]
#my_new_dict = dict.fromkeys(['Nombre', 1, "piso"])
my_new_dict = dict.fromkeys(my_list)
#my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
