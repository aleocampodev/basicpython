### Tuples ### si escribimos solo parentesis es una tupla, si escribimos solo corchetes es una lista, list() es una lista
### Una Tupla es un conjunto de valores 
my_tuple = tuple()
my_other_tuple = ()

my_tuple =(35, 1.77, "Brais", "Moure", "Brais")

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count('Brais'))
print(my_tuple.index("Moure"))

my_tuple[1 ] = 1.80 # UN atupla es inmutable a lo cual se pueden guardar datos en ellos
print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

#Si usamos una tupla es or que queremos lo valores dentro de ella constante, cuando los datos son inmutables mejor

my_tuple = list(my_tuple)
print(type(my_tuple)) 

my_tuple[4] = "Alejadev"
my_tuple.insert(1,"Rosado")
print(tuple(my_tuple))
#del my_tuple[1] # Esto seri un error
#Para eliminar la tupla, del es tipico de cualquier variable que le pasemos
del my_tuple
print(my_tuple)