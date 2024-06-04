### lists ### Una lista es un conjunto de un arreglo 
my_lists = list()

my_other_lists = []

print(len(my_lists))

my_list = [36, 30, 26, 77, 66, 90]

print(my_list)

print(len(my_list))

my_other_list = ["Aleja", "Ocampo", 1, 2]

print(my_other_list[0])
print(my_other_list[-1])
print(my_other_list[1])
print(my_other_list[-4])
#print(my_other_list[4]) IndexError
#print(my_other_list[5]) IndexError

my_count = [15,46, 30,40,28, 28 ]
print(my_count.count(28))

name, height, age, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age) #aunque esto es complicarse el codigo

print(my_count + my_other_list)

print([1,2,3,4])

my_other_list.append("aledev")

my_other_list.insert(1, "Azul")

my_list.remove(30)
my_list.pop()

my_list[1] = 4

my_pop_element = my_list.pop(2)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()
print(my_new_list,'ji')

my_new_list.reverse()

my_new_list.sort()

my_list.clear()

#Sublistas
print(my_new_list[1:4])