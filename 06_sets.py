### sets##
### Un set de base tiene un array, en python no existen arrays como tal si no listas directamente

### set es un tipo de dato
#No hay un tipado fuerte
my_set = set()
my_other_set = {} #Inicialmente es un diccionario

print(my_set)
print(my_other_set)
my_other_set = { "Aleja", "Ocampo", 77}

print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("aleocampodev")
print(my_other_set) #Un set no es una estructura ordenada, de acceder en el elemento 0, 1, etc, en los sets ya no se tienen

my_other_set.add("aleocampodev")
print(my_other_set) #Un set no admite datos repetidos

print("Ocampo" in my_other_set)
print("Ocampe" in my_other_set)

my_other_set.remove("Aleja")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set #elimina la variable
#print(my_other_set) NameError

my_set = {"Aleja", "Ocampo", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"key", "value"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "c#"}))

print(my_new_set.difference(my_set))