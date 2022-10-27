import math

"""
Completed Exercises

Ejercicio 1
Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.


num_1 = float(input("Introduzce the first number: "))
num_2 = float(input("Introduzce the second number: "))

if(num_1>num_2):
    print(f"This number  {num_1} is greater than {num_2}")
elif(num_2>num_1):
    print(f"This number {num_2} is greater than {num_1}")
else:
    print("This two numbers are equal")


********************************


Ejercicio 2
Algoritmo que pida un número y diga si es positivo, negativo o 0.
num = float(input("Introduce a number: "))
if(num>0):
    print(f"This number {num} is positive")
elif(num<0):
    print(f"This number {num} is negative")
else:
    print(f"This positive {num} is equal to 0")
*****************



Ejercicio 3
Escribe un programa que lea un número e indique si es par o impar.

value_1 = float(input("Introduce a number: "))
if(value_1 %2 ==0):
    print(f"This number {value_1} is pair")
else:
    print(f"This number is odd")
*****************


Ejercicio 4
Crea un programa que pida al
usuario dos números y muestre 
su división si el segundo no es cero, o un mensaje de aviso en caso contrario.
value_1 = float(input("Introduce the first value: "))
value_2 = float(input("Introduce the second value: "))

if(value_2!= 0.0):
    print(f"The result is {value_1 / value_2}")
else: 
    print("The second value is 0")
    
*****************    

Ejercicio 5
Escribe un programa que pida un nombre de usuario y una contraseña
y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
name = input("Introduce your name: ")
password = input("Introduce your password: ")


if(name == "pepe" and password == "asdasd"):
    print("Login succesfully")
else:
    print("ERROR: Login failed  ")

*****************

Ejercicio 6
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
cadena = input("introduce una cadena de texto: ")
if(cadena.isupper()):
    print("Is Uppercase")
else: 
    print("Is Lowercase")
*****************

Ejercicio 7
Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:

El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
base = 5 #int(input("Introduce la base"))
exp = 2#int(input("Introduce el exponente"))

if(exp==0):
    print(1)
elif(exp<0):
    print(1/math.pow(base, abs(exp)))
else:
    print(math.pow(base, exp))
*****************



Ejercicio 9
Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

nums = [1,7,5,9,3,5,4,7,5,1,1,1,4,7,78,5]
nums.sort()
print(nums)
****************
# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos 
# circunferencias y las clasifique en uno de estos estados:
# exteriores
# tangentes exteriores
# secantes
# tangentes interiores
# interiores
# concéntricas

import math

x1 = float(input("Dime coordenada x primera circunferencia:"))
y1 = float(input("Dime coordenada y primera circunferencia:"))
r1 = float(input("Dime radio primera circunferencia:"))
x2 = float(input("Dime coordenada x segunda circunferencia:"))
y2 = float(input("Dime coordenada y segunda circunferencia:"))
r2 = float(input("Dime radio segunda circunferencia:"))


distancia = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
#  circunferencias exteriores
# La distancia entre los centros, d, es mayor que la suma de los radios.
if distancia > (r1 + r2):
	print("Circunferencias exteriores")
#  circunferencias tangentes exteriores
# La distancia entre los centros es igual a la suma de los radios.
if distancia == (r1 + r2):
	print("Circunferencias tangentes exteriores")
#  circunferencias secantes
# La distancia  es menor que la suma de los radios y mayor que su diferencia.
if distancia < (r1 + r2) and distancia > abs(r1-r2):
	print("Circunferencias secantes")
#  Circunferencias tangentes interiores
# La distancia entre los centros es igual a la diferencia entre los radios.
if distancia == abs(r1-r2):
	print("Circunferencias tangentes interiores")
#  Circunferencias interiores
# La distancia entre los centros es mayor que cero y menor que la diferencia entre los radios. 
if distancia>0 and distancia<abs(r1-r2):
	print("Circunferencias interiores")
#  Circunferencias concétricas
#  La distancia = 0.
if distancia == 0:
	print("Circunferencias concétricas")

Ejercicio 11
Programa que lea 3 datos de entrada A, B y C.
Estos corresponden a las dimensiones de los lados de un triángulo.
El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
# Pitágoras
if ladoA ** 2 + ladoB ** 2 == ladoC ** 2 or ladoB ** 2 + ladoC ** 2 == ladoA ** 2 or ladoC ** 2 + ladoA ** 2 == ladoB ** 2:
	print("Triángulo Rectángulo")
# isósceles
if (ladoA == ladoB and ladoA != ladoC) or (ladoB == ladoC and ladoB != ladoA) or (ladoC == ladoA and ladoC != ladoB):
	print("Triángulo Isósceles")
else:
	# equilátero
	if ladoA == ladoB and ladoA == ladoC:
		print("Triángulo Equilátero")
	else:
		print("Triángulo Escaleno")
*****************

Ejercicio 12
Escribir un programa que
lea un año indicar si es bisiesto. 
Nota: un año es bisiesto si es un número divisible por 4, 
pero no si es divisible por 100, excepto que también sea divisible por 400.
anio = 2024
if anio %4 ==0 and anio % 100 !=0 and anio % 400 !=0:
    print("bisiesto")
else:
    print("no bisiesto")	

*****************


Ejercicio 13
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = 10
mes = 1
anio = 2022

if anio <=2022:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes ==10 or mes ==12:
        if dia<=31:
            print(f"correct {anio}, {mes}, {dia}")
    elif mes == 4 or mes == 6 or mes == 9 or mes ==11:
        if dia <=30:
            (f"correct {anio}, {mes}, {dia}")
    elif mes == 2:
        if dia <=28:
            (f"correct {anio}, {mes}, {dia}")
else:
    print("Introduce a correct year")


*****************

Ejercicio 14
La asociación de vinicultores tiene como política
fijar un precio inicial al kilo de uva, la cual se 
clasifica en tipos A y B, y además en tamaños 1 y 2.
Cuando se realiza la venta del producto, ésta es de
un solo tipo y tamaño, se requiere determinar cuánto 
recibirá un productor por la uva que entrega en un embarque, 
considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de 
tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, 
se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.


precio_inicial = float(input("Introduce el precio inicial por kilos de la UVA (centimos):"))
kilos = int(input("Introduce cuantos kilos has vendido:"))
tipo = input("Introduce el tipo de la UVA (A/B):")

if tipo.upper() != "A" and tipo.upper() != "B":
    print("Tipo incorrecto")
else:
    tamano = input("Introduce el tamaño de la UVA (1/2):")
    if tamano != "1" and tamano != "2":
        print("Tamaño incorrecto")
    else:
        if tipo.upper() == "A":
            if tamano == "1":
                precio_inicial = precio_inicial+20
            else:
                precio_inicial = precio_inicial+30
        else:
            if tamano == "1":
                precio_inicial = precio_inicial-20
            else:
                precio_inicial = precio_inicial-30
        precio_final = precio_inicial * kilos
        print("La ganancia es %.2f euros." % (precio_final/100))
        
*****************

Ejercicio 15
El director de una escuela está organizando un viaje de estudios,
y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar 
a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: 
si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 
alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30,
el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
Realice un algoritmo que permita determinar el pago a la compañía de autobuses y 
lo que debe pagar cada alumno por el viaje.
alumnos = 100
cobro_autobus = 0


if alumnos <30:
    cobro = 4000
elif alumnos >=30 and alumnos <50:
    cobro = alumnos *95
elif alumnos >49 and alumnos <100:
    cobro = alumnos * 70
elif alumnos >99:
    cobro = alumnos*65
    
print(cobro)

*****************


Ejercicio 16
La política de cobro de una compañía telefónica es: 
cuando se realiza una llamada, el cobro es por el tiempo 
que ésta dura, de tal forma que los primeros cinco minutos 
cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes
dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, 
en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo 
para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

minutes = 10
turno_tarde = False
es_domingo = False
porcentaje = 0
euro_minute =0


if es_domingo:
    porcentaje = 0.03
elif not es_domingo and not turno_tarde:
    porcentaje = 0.15
elif not es_domingo and not turno_tarde:
    porcentaje =0.1
    
if minutes<=5:
    euro_minute = 1
elif minutes > 5 and minutes < 9:
    euro_minute = .8
elif minutes>8 and minutes<10:
    euro_minute = .7
elif minutes >=10:
    euro_minute = .5

total_minutes = (euro_minute * minutes )
total_minutes = total_minutes + (total_minutes * porcentaje)
print(total_minutes)

*****************

Ejercicio 17
Realiza un programa que pida por teclado el resultado (dato entero)
obtenido al lanzar un dado de seis caras y muestre por pantalla el 
número en letras (dato cadena) de la cara opuesta al resultado obtenido.

cara = int(input("Introduce el número de la cara:"))
if cara == 1:
	print("SEIS")
elif cara == 2:
	print("CINCO")
elif cara == 3:
	print("CUATRO")
elif cara == 4:
	print("TRES")
elif cara == 5:
	print("DOS")
elif cara == 6:
	print("UNO")
else:
	print("Error: número incorrecto.")
*****************


Ejercicio 18
Realiza un programa que pida el día de la semana (del 1 al 7)
y escriba el día correspondiente. Si introducimos otro número nos da un error.

dia = int(input("Introduzca el dia de la semana: "))
if dia == 1: 
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")
else:
    print("Introduce un dia valido")
    
    
*****************


Ejercicio 19
Escribe un programa que pida un número entero entre uno y
doce e imprima el número de días que tiene el mes correspondiente.

mes = int(input("Introduce el numero del mes: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes ==10 or mes ==12:
    print("31 días")
elif mes == 4 or mes == 6 or mes == 9 or mes ==11:
    print("30 días")
elif mes == 2:
    print("28 o 29 días")
else:
    print("Introduce a correct month")
    
*****************

Ejercicio 20
Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia.
El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

Zona	Ubicación	Costo/gramo
1	América del Norte	24.00 euros
2	América Central	20.00 euros
3	América del Sur	21.00 euros
4	Europa	10.00 euros
5	Asia	18.00 euros
Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

zona = int(input("Introduce \n"+
                 "1.América del Norte.24.00 euros\n"+   
                 "2.América Central.20.00 euros\n"+
                 "3.América del Sur.21.00 euros\n"+
                 "4.Europa 10.00 euros\n"+
                 "5.Asia 18.00 euros\n"))

weight = float(input("Introduce el peso del paquete: "))


if weight > 5:
    print("El paquete a sido rechazado por sobrepeso")
elif weight<=5:
    if zona == 1:
        print(f"El total del paquete es {weight*24}")
    elif zona == 2:
        print(f"El total del paquete es {weight*20}")
    elif zona == 3:
        print(f"El total del paquete es {weight*21}")
    elif zona == 4:
        print(f"El total del paquete es {weight*10}")
    elif zona == 5:
        print(f"El total del paquete es {weight*18}")
"""