import math 
import random

"""
Current Exercise
"""

cadena = input("Introduce una cadena: ")

cadena_reversed = ""

for i in reversed(range(0,len(cadena))):
    cadena_reversed +=cadena[i]
    
print(cadena)
print(cadena_reversed)
    

if cadena_reversed == cadena: 
    print(f"{cadena} es palindromo")
else:
    print(f"{cadena} no es un palindromo")    



""" 
Ejercicio 10
Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma 
es aquella que se lee igual adelante que atrás.

"""


"""
Exercises Completed

Ejercicios cadena de caracteres
Ejercicio 1
Escribir por pantalla cada carácter de una cadena introducida por teclado.

cadena = input("Introduce una cadena de caracteres: ")

for i in range(0, len(cadena)):
    print(cadena[i])


**************************


Ejercicio 2
Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.


cadena = input("Introduce una primera cadena: ")
segunda_cadena = input("Introduce una segunda cadena: ")

if cadena.startswith(segunda_cadena):
    print(True)
else: 
    print(False)

**************

Ejercicio 3
Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

cadena = input("Introduce una cadena por consola: ")
caracter = input("Introduce un caracter a buscar: ")


acu = 0
for i in range(0, len(cadena)):
    if cadena[i].upper == caracter.upper:
       acu +=1
print(f"El total de repeticiones del caracter es: {acu}") 

**************


Ejercicio 4
Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.
cadena = input("Introduce una cadena: ")
acu = 0
for i in range(0, len(cadena)):
    if cadena[i] != " ":
        if i<len(cadena)-1:
            if cadena[i+1] ==" ":
                acu+=1
print(f"El total de palabras es {acu}")


**************

Ejercicio 5
Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.

cadena = input("Introduce tu nombre y apellidos: ")

nombre = cadena.split(" ")
print(f"Iniciales: {nombre[0][0].upper()} {nombre[1][0].upper()} {nombre[2][0].upper()}")

**************


Ejercicio 6
Realizar un programa que dada una cadena de caracteres por caracteres, genere otra cadena 
resultado de invertir la primera.

cadena = input("Introduce una cadena de caracteres: ")

cadena_invertida = ""

for i in reversed(range(0,len(cadena))):
    cadena_invertida+=cadena[i]
    
print(cadena_invertida)

**************

Ejercicio 7
Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la 
aparición del primer carácter en la cadena por el segundo carácter.

cadena = input("Introduzca una cadena: ")

while True:
    primer_caracter = input("Introduzca un caracter: ")
    if len(primer_caracter) ==1:break

while True:
    segun_caracter = input("Introduzca un caracter: ")
    if len(segun_caracter) ==1:break

nueva_cadena = cadena.replace(primer_caracter,segun_caracter)



print(f"La cadena es {nueva_cadena}")
**************


Ejercicio 8
Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a 
minúsculas y viceversa.

cadena = input("Introduce una cadena: ")
print(cadena.swapcase())

**************


Ejercicio 9
Realizar un programa que compruebe si una cadena contiene una subcadena. 
Las dos cadenas 
se introducen por teclado.



cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")

if subcadena in cadena:
    print(f"La {subcadena} esta en la cadena")
else: 
    print(f"La {subcadena} no esta en la cadena")
    
**************
"""