import math


""" 
Ejercicio 1
Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
name = input("Please enter your name: ")
print(f"Your name is {name}")
********************************
Ejercicio 2
Calcular el perímetro y área de un rectángulo dada su base y su altura.
base = float(input("Enter the base of the triangle: "))
tall =float(input("Enter the tall of the triangle: "))

perimetro = 2 * base * tall
base = base*tall
print(f"The base of the triangle is %.2f and the perimeter is {perimetro}" % base)
*******************************
Ejercicio 3
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
cateto1 = float(input("Introduzca un cateteo: "))
cateto2 = float(input("Introduzca un cateteo: "))

hipotenusa = math.sqrt(math.pow(cateto1,2)+math.pow(cateto2,2))
print("La hipotenusa es %.2f" % hipotenusa)
*******************************

Ejercicio 4
Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
num1 = float(input("Please introduce the first number: "))
num2 = float(input("Please introduce the second number: "))

print(f"The sum is : {num1+num2}\n+"
      f"The substract is : {num1-num2}\n" +
      f"The multiplication is : {num1*num2}\n" +
      f"The Division is : {num1/num2}\n" +
      f"The Module is : {num1%num2}\n")
********************************


Ejercicio 5
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
C = (F-32)*5/9
fahrenheit = float(input("Introduce the Fahrenheit: "))

celsius = ((fahrenheit-32)*5/9)
print("The celsius are %.2f" %celsius

****************************************************************




Ejercicio 6
Calcular la media de tres números pedidos por teclado.
val1 = float(input("First value: "))
val2 = float(input("Second value: "))
val3 = float(input("Third value: "))

result = (val1+val2+val3)/3
print("The result is %.2f" % result)
*******************************






Ejercicio 7
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
Por ejemplo: 1000 minutos son 16 horas y 40 minutos.


minutes = int(input("Introduce a certain number of minutes"))

total_hours = (minutes/60)
total_minutes =int((total_hours- int(total_hours))*60)
print(f"The total of hours are: {int(total_hours)}  and the total of minutes are {total_minutes}")

********************************

Ejercicio 8
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
venta_1 = 100
venta_2 = 100
venta_3 = 100

sueldo_base = 1750

venta_1 = venta_1*.1
venta_2 = venta_2*.1
venta_3 = venta_3*.1
sueldo_total = (venta_1+venta_2+venta_3)+sueldo_base
print(f"El sueldo total es {sueldo_total}")


********************************


Ejercicio 9
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
total_sin_descuento = 100
descuento = total_sin_descuento *.15
total_con_descuento = total_sin_descuento - descuento
print(f"El total de la compra es {total_con_descuento}")
********************************


Ejercicio 10
Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.

calificacion_parcial_1 = 4
calificacion_parcial_2 = 7
calificacion_parcial_3 = 8

examen_final = 8

trabajo_final = 10

calificacion_parcial_total =( (calificacion_parcial_1*.55)+(calificacion_parcial_2*.55)+(calificacion_parcial_3*.55))/3
examen_final_total = (examen_final*.30)
trabajo_final_total = (trabajo_final*.15)
total = int(calificacion_parcial_total) + int(examen_final_total) + int(trabajo_final_total)
print(total)
*******************************

Ejercicio 11
Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).


num1 = int(input("Introduzca un numero: "))
num2 = int(input("Introduzca un numero: "))

result = abs(num1-num2)
print(result)
*******************************


Ejercicio 12
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

x1 = 5
y1 =2

x2 = 10
y2 = -2


difference_in_x = abs(x1 - x2)
difference_in_y = abs(y1 - y2)

print(f"The difference in x is {difference_in_x} and the difference in y {difference_in_y}")
*******************************

Ejercicio 13
Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?


raiz_cuadrada =math.sqrt(int(input("Introduzca la raiz cuadrada: ")))
raiz_cubica = int(input("Introduzca la raiz cubica: "))**(1/3)


print(f"La raiz cuadrada es {raiz_cuadrada} y la raiz cubica es {raiz_cubica}")
*******************************


Ejercicio 14
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

num = input("Introduzca un numero: ")
print(num[::-1])
*******************************

Ejercicio 15
Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

var_a = 5
var_b = 10

var_c = var_b
var_b = var_a
var_a = var_c

print(var_a)
print(var_b)

*******************************

Ejercicio 16
Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

distancia = 150

vehiculo_1 = 100
vehiculo_2 = 120

tiempo_1 = abs((distancia/(vehiculo_1-vehiculo_2))*6)



print(f"Tardaria {tiempo_1} min")

*******************************

Ejercicio 17
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
salida_horas =15 
salida_min = 27
salida_segundo = 00

tiempo_de_viaje_horas = 1
tiempo_de_viaje_minutos = 40
tiempo_de_viaje_segundos = 60

if(salida_horas!=23):
      salida_horas += tiempo_de_viaje_horas
else:
      salida_horas = 0
      salida_horas += tiempo_de_viaje_horas

if((salida_min + tiempo_de_viaje_minutos)<60):
      salida_min += tiempo_de_viaje_minutos
else:
      salida_min = 0
      salida_min = abs(((salida_min+tiempo_de_viaje_minutos)-60))
      salida_horas+=1
      
if((salida_segundo + tiempo_de_viaje_segundos)<60):
      salida_segundo += tiempo_de_viaje_segundos
else:
      salida_segundo = 0
      salida_segundo = abs(((salida_segundo+tiempo_de_viaje_segundos)-60))
      salida_min+=1
      
print(f"Llega a las {salida_horas} minutos {salida_min} segundos {salida_segundo}")
*******************************





Ejercicio 18
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

name = input("Introduce your name: ")
surname = input("Introduce your surname: ")

print(f"{name[0]} {surname[0]}")

*******************************


Ejercicio 19
Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.


correctas = 5
incorrectas = 2
puntos = correctas * 5 + incorrectas * (-1)
print("Puntos:",puntos)

*******************************

Ejercicio 20
Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).


two_euro =3
one_euro = 4
f_cent = 2
tw_cent =4
t_cent = 8

total_euros = (two_euro*2)+one_euro
total_cent = (f_cent*50)+(tw_cent*20)+(t_cent*10)

print(total_cent)

if(total_cent<=100):
      total_cent_temp = abs((total_cent)-100)
      total_cent = 0
      total_cent = total_cent_temp
      total_euros+=1
elif(total_cent>200):
      total_cent_temp = abs((total_cent)-200)
      total_cent = 0
      total_cent = total_cent_temp
      total_euros+=2
      
print(f"EL total de euros es {total_euros}, y el total de centimos es {total_cent}")

"""
