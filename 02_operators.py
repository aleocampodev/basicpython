### Operadores Aritmeticos ###
##print sirve para ver datos por consola
print(3 + 4)
print (3 - 4)
print (3 * 4)
print (3 / 4)
print(3 % 4)
print( 3 // 4) # siempre va a dar un numero entero
print (2 ** 3) # Para calcular un exponente

print("Hola" + "Python")
print ("Hola" + str(5))
print("Hola" * 5)
print("Hola" * (2 ** 3))
my_float = 2.5 * 2
print("Hola")

###Operadores Comparativo ###
print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 2)

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") #Ordenacion alfabetica por ASCII
print(len("aaaa") <= len("abaa")) #Cuenta con caracteres
print("Hola" == "Python")
print("Hola" != "Python")

###Operadores Logicos ###

print(3 > 4 and "Hola" > "Python")
print(3 < 4 or "Hola" > "Python")
print(3 > 4 and ("Hola" > "Python" and 4 == 4)) #Si quiero que primero se haga una operacion agrego parentesis
print(not(3>4)) #not es un negacion y not false es true