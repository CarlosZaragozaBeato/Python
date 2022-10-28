import math
import random


"""
Current exercise
Ejercicio 16
Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además,
calcule cuánto pagó la empresa por los N empleados.
"""

sueldo_por_hora = random.randint(5,15)
horas_trabajas_por_dia = random.randint(4,10)
horas_trabajas_por_semana = horas_trabajas_por_dia*6

total_de_trabajadores = random.randint(5,150)

total = total_de_trabajadores * (horas_trabajas_por_semana*sueldo_por_hora)
print(total)


    

"""
Ejercicios estructuras repetitivas

Ejercicio 17
Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

Ejercicio 18
Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

Ejercicio 19
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que seleccionamos la opción de “Salir”.

Ejercicio 20
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de números primos que queremos mostrar.
"""


""" 
Completed 
Ejercicio 1
Crea una aplicación que pida un número y calcule su factorial (El factorial de un número
es el producto de todos los enteros entre 1 y el propio número y se representa por el número 
seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120),
num = 5 
factorial = 1

for i in range(1,num+1):
    factorial = factorial*i
print(factorial)

*****************

Ejercicio 2
Crea una aplicación que permita adivinar un número.
La aplicación genera un número aleatorio del 1 al 100. 
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando 
se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos 
te muestra el número que había generado.


num = int(input("Introduce un numero: "))
aleatorio = random.randint(0,100)
limite = 10
counter = 0

while True:
    if num > aleatorio:
        print("Mas bajo")
    elif num<aleatorio:
        print("Mas alto")
    else:
        break
    counter +=1
    if counter == limite:
        break
    
    num = int(input("Introduce un numero: "))
    
if counter == limite:
    print(f"You lose and the number was {aleatorio}")
else:
    print(f"YOU WIN in {counter} times")

********************************

Ejercicio 3
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

media = 0
total = 0
counter = 0
value = int(input("Introduce un numero: "))

while True:
    if value == 0:
        break
    
    total +=value
    counter +=1
    value = int(input("Introduce un numero: "))

print(f"El total es {total} y la media es {total/counter}")

*****************

Ejercicio 4
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

num = int(input("Introduce un numero: "))
cantidad_num = int(input("Cantidad de numeros: "))

counter_0 = 0
counter_minus = 0
counter_plus = 0

for i in range(1,cantidad_num):
    if num == 0:
        counter_0 += 1
    if num<0:
        counter_minus+=1
    if num>0:
        counter_plus+=1
    num = int(input("Introduce un numero: "))
    
print(f"Cantidad de 0 {counter_0}, Plus {counter_plus}, Minus {counter_minus}")
*****************

Ejercicio 5
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ 
en caso contrario, el programa termina cuando se introduce un espacio.

cadena = input("Introduzca una cadena: ")

for i in range(0, len(cadena)):
    if cadena[i] == " ":
        break
    if cadena[i] == "a" or cadena[i] == "e" or cadena[i] == "i" or cadena[i] == "o" or cadena[i] == "u":
        print(f"VOCAL; {cadena[i]}")
    else: 
        print(f"NO VOCAL {cadena[i]}")

*****************

Ejercicio 6
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.


num_1 = int(input("Introduce el numero menor: "))
num_2 = int(input("Introduce el numero mayor: "))

for i in range(num_1, num_2+1):
    print(i)

*****************

Ejercicio 7
Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

num = int(input("Introduce un numero: "))

for i in range(0,11):
    print(f"{i}:{i*num}")
    
*****************


Ejercicio 8
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:
La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
He informa si hemos introducido algún número igual a los límites del intervalo.

intervalo_1 = int(input("Introduce el primer intervalo: "))
intervalo_2 = int(input("Introduce el segundo intervalo: "))

suma = 0
fuera_de_rango = 0

numero_intervalo = 0

while True:
    while intervalo_1 >= intervalo_2:
        intervalo_1 = int(input("Introduce el primer intervalo: "))
        intervalo_2 = int(input("Introduce el segundo intervalo: "))
    numero_intervalo = int(input("Introduce numero intervalo: "))
    if numero_intervalo >= intervalo_1 and numero_intervalo =< intervalo_2:
        suma += numero_intervalo
    else:
        fuera_de_rango += 1
    if numero_intervalo == 0:
        break
    
print(f"El intervalo es entre {intervalo_1} y {intervalo_2}")
print(f"La suma de los intervalos es {suma}, y los intervalos fuera de rango son {fuera_de_rango}")

*****************
Ejercicio 9
Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

base = int(input("Introduce una base: "))
exponente = int(input("Introduce un exponente: "))

contador = 0

resultado = 0
while contador <=exponente:
    resultado = base * base
    contador +=1

print(resultado)
****************
















Ejercicio 11
Escribe un programa que diga si un número introducido por
teclado es o no primo. Un número primo es aquel que sólo es 
divisible entre él mismo y la unidad. Nota: Es suficiente probar
hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

def es_primo(n):
    for i in range(2,int(n/2)):
        if (n%i) == 0:
            return False
        return True

print(es_primo(n))
****************
Ejercicio 10
Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

multiplicacion_1  = []
multiplicacion_2  = []
multiplicacion_3  = []
multiplicacion_4  = []
multiplicacion_5  = []


for i in range(0, 11):
    multiplicacion_1.append(1*i)
    multiplicacion_2.append(2*i)
    multiplicacion_3.append(3*i)
    multiplicacion_4.append(4*i)
    multiplicacion_5.append(5*i)


print(multiplicacion_1)
print(multiplicacion_2)
print(multiplicacion_3)
print(multiplicacion_3)
print(multiplicacion_4)
print(multiplicacion_5)
****************


Ejercicio 12
Realizar un algoritmo para determinar cuánto ahorrará una persona 
en un año, si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.


ahorro = 0
for i in range(1,13):
    ahorro += int(input(f"Cantidad ahorrada en el mes {i}: "))
    
print(f"Total ahorrado {ahorro}")

*****************


Ejercicio 13
Una empresa tiene el registro de las horas que trabaja diariamente un empleado
durante la semana (seis días) y requiere determinar el total de éstas, así como el 
sueldo que recibirá por las horas trabajadas.

sueldo_por_hora = 10

horas = 0

for i in range(1,7):
    horas += random.randint(1,10)
    
print(f"El total del sueldo de la semana es {horas*sueldo_por_hora}")
*****************


Ejercicio 14
Una persona se encuentra en el kilómetro 70 de una carretera, 
otra se encuentra en el km 150, los coches tienen sentido opuesto y 
tienen la misma velocidad. Realizar un programa para determinar en qué 
kilómetro de esa carretera se encontrarán.

primera_persona = 70 
segunda_persona = 150

while True:
    primera_persona +=1
    segunda_persona -=1 
    if(primera_persona == segunda_persona):
        break
    
print(f"{primera_persona} {segunda_persona}")
*****************

Ejercicio 15
Una persona adquirió un producto para pagar en 20 meses. 
El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de
lo que pagó después de los 20 meses.


producto = 6200
total_pagado = 0
pago = 10


for i in range(1,21):
    total_pagado +=  pago
    pago = pago*2
print(f"El total pagado es {total_pagado} y la cantidad restante {abs(total_pagado-producto)}")






"""