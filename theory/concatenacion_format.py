edad = 23
nombre = "Carlao"

print("Tu nombre es {0} y tienes {1} años".format(nombre, edad))

#F Strings
#Ejemplo1

print(f"El resultado de 8+58 = {8+58}")


#Ejemplo2
estatura = 1.8
edad = 23
print(f"Hola {nombre} tienes {edad} y eres {estatura}")

#Ejemplo3
nombre = input("Cual es tu nombre: ")
num_uno = int(input("Introduce un numero: "))
num_dos = int(input("Introduce un segundo numero: "))

print(f"Hola {nombre} la suma de {num_uno} y {num_dos} es {num_uno+num_dos}")
