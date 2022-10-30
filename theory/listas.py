import math 
import random


""" 
Exercises completed 

Ejercicio 1
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

lista = []

for i in range(0,10):
    lista.append(random.randint(1,10))
    
print(f"Los numeros aleatorios son {lista}")

********************************


Ejercicio 2
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.


lista = []
lista2 = []
for i in range(0,4):
    cadena = input("Introduce una cadena: ")
    lista.append(cadena)
    
lista.reverse()

lista2 = lista[:]

lista.append(5)
print(lista2)

********************************


Ejercicio 3
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
(comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

lista = []
sum = 0
avg = 0
for i in range(0,4):
    nota = random.randint(0,10)
    lista.append(nota)
    sum += nota

avg = sum/len(lista)
print(f"La nota media del curso es {avg}, la nota maxima es {max(lista)}")
print(f"Las notas son {lista}")

********************************


Ejercicio 4
Programa que declare una lista y la vaya llenando de números hasta que 
introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).



lista = []

while True:
    numero = int(input("Introduce un numero: "))
    if numero <0:break
    lista.append(numero)
    
for i in lista:
    print(i," ", end = "")
    
    
    
*******************************

Ejercicio 5
Hacer un programa que inicialice una lista de números 
con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.

lista = []
for i in range(0,11):
    numero = random.randint(0,10)
    lista.append(numero)
    
lista.sort()

for i in lista:
    print(i," ", end ="")


*******************************


Ejercicio 6
Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) 
y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas.
Para simplificarlo vamos a suponer que febrero tiene 28 días.
lista = [31,28,31,30,31,30,31,31,30,31,30,31]
nombre_mes = ""
mes = int(input("Introduce un numero de mes: "))



match mes :
    case 1:
        nombre_mes = "Enero"
    case 2:
        nombre_mes = "Febrero"
    case 3: 
        nombre_mes = "Marzo"
    case 4: 
        nombre_mes = "Abril"
    case 5:
        nombre_mes = "Mayo"
    case 6:
        nombre_mes = "Junio"
    case 7:
        nombre_mes = "Julio"
    case 8:
        nombre_mes = "Agosto"
    case 9:
        nombre_mes = "Septiembre"
    case 10:
        nombre_mes = "Octubre"
    case 11:
        nombre_mes = "Noviembre"
    case 12:
        nombre_mes = "Diciembre"


print(f"El mes seleccionado tiene {lista[mes-1]}, y el mes es {nombre_mes}")

*******************************



Ejercicio 7
Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ 
de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

lista_1 = []
lista_2 = []
lista_3 = []

for i in range(0,4):
    numero_random_1 = random.randint(0,150)
    numero_random_2 = random.randint(0,150)
    lista_1.append(numero_random_1)
    lista_2.append(numero_random_2)


for i,x in zip(lista_1, lista_2):
    lista_3.append(i+x)
    
print(lista_1)
print(lista_2)
print(lista_3)

*******************************


Ejercicio 8
Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. 
El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:

Todos lo alumnos mayores de edad.
Los alumnos mayores (los que tienen más edad)

lista_alumnos = []

while True:
    
    nombre = input("Introduce el nombre de un alumno: ")
    if nombre == "*":break
    edad = int(input("Introduce la edad del alumno:"))
    
    lista_alumnos.append((nombre, edad))
    
    
lista_alumnos.sort(reverse=True)


for i in lista_alumnos:
        print(i[0],":",i[1]," " ,end ="")
        
        
*******************************


Ejercicio 9
Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:

La temperatura media de cada día
Los días con menos temperatura
Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un mensaje de información.

dias_semana = []

for i in range(0,8):
    temp_max = random.randint(15,30)
    temp_min = random.randint(0,15)
    dias_semana.append((temp_min, temp_max))


media_semana = []
for i in dias_semana:
    media_semana.append((i[0]+i[1])/2)


dia_con_menor_temp = ()
dia = 0
acu = 100
for i in range(0,len(dias_semana)):
    if acu > dias_semana[i][0]:     
        acu = dias_semana[i][0]
        dia = i  
dia_con_menor_temp = (dia, acu)



temp_cadena = int(input("introduzca un dia de la semana: "))
temp_repetida = []
for i in range(0,len(dias_semana)):
    if temp_cadena == dias_semana[i][0] or temp_cadena == dias_semana[i][1]:
        temp_repetida.append((i,temp_cadena))



print(f"La media de la semana es {media_semana}")
print(f"El dia con menor temperatura son {dia_con_menor_temp}")
print(f"Los dias con temperatura repetida son {temp_repetida}")


*******************************

Ejercicio 10
Diseñar el algoritmo correspondiente a un programa, que:


lista = [[],[]]
lista3 =[]

for i in range(0,5):
    numero_random_1 = random.randint(0,15)
    numero_random_2 = random.randint(15,30)

    lista[0].append(numero_random_1)
    lista[1].append(numero_random_2)

for i in range(0,len(lista[0])):
    lista3.append(lista[0][i] + lista[1][i])


print(lista[0])
print(lista[1])
print(lista3)

Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
Carga la tabla con valores numéricos enteros.
Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

*******************************
Ejercicio 11
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
Muestra el contenido de la tabla en pantalla.



tabla = []

for i in range(0,5):
    fila = []
    for i_columna in range(0,5):
        if i == i_columna or i == 4 - i_columna:
            fila.append(1)
        else: 
            fila.append(0)
    tabla.append(fila)

for fila in tabla:
    for elemento in fila:
        print(elemento, " ", end="")
    print()

*******************************


Ejercicio 12
Diseñar el algoritmo correspondiente a un programa, que:

Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla,
es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
  111111111111111
  100000000000001
  100000000000001
  100000000000001
  111111111111111




tabla = []

for i in range(0,5):
    fila = []

    for j in range(0,15):
        if i == 0 or i== 4:
            fila.append(1)
        elif j == 0 or j == 14:
            fila.append(1)
        else:
            fila.append(0)
    tabla.append(fila)


for i in tabla:
    for j in i:
        print(j, " ", end="" )
    print()
    
******************************* 

Ejercicio 13
De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.

Para guardar esta información se van a utilizar dos arreglos:

Nombre: Lista para guardar los nombres de los conductores.
kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.

Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.



import random


lista_dias_semana = []

total_km = []

nombre_conductores = []


for i in range(0,7):
    km = random.randint(0,400)
    lista_dias_semana.append(i)
    nombre_conductores.append(input("Introduce el nombre del conductor: "))
    total_km.append(km)


for i in range (0,7):
    print(f"El dia de la semana {lista_dias_semana[i]+1}: el conductor {nombre_conductores[i]}, ha conducido {total_km[i]}\n")



*******************************


Ejercicio 14
Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:

Las cantidades totales de cada articulo.
La cantidad de artículos en la sucursal 2.
La cantidad del articulo 3 en la sucursal 1.
La recaudación total de cada sucursal.
La recaudación total de la empresa.
La sucursal de mayor recaudación.


precios = []
cantidades = []
num_articulos = 5
num_sucursales = 3
# Leer Precios
for indice_art in range(0, num_articulos):
   precios.append(float(input('Ingrese Precio Articulo %d:' % (indice_art+1))))

# Leer Cantidades


for indice_sucursal in range(0, num_sucursales):
    cant_art = []
    for indice_art in range(0, num_articulos):
        cant_art.append(int(input('Ingrese Cant. de Articulo %d, en sucursal %d:' % (indice_art+1,indice_sucursal+1))))
    cantidades.append(cant_art)
   
## Sumar cantidades por artículos
print('Cantidades por artículos:')
for indice_art in range(0, num_articulos):
    suma = 0
    for cant_sucursal in cantidades:
        suma = suma + cant_sucursal[indice_art]
    print('Total articulo %d: %d' % (indice_art + 1,suma))

# Informar Total de artículos Sucursal 2

print('Total Sucursal 2: %d' % sum(cantidades[1]))

# Informar Sucursal 1, Articulo 3:
print('Sucursal 1, Articulo 3: %d' % cantidades[0][2])

# Guardo en una lista las recaudaciones de cada sucursal
total_por_sucursal = []
for precio,cant_sucursal in zip(precios,cantidades):
    total_por_sucursal.append(sum(cant_sucursal) * precio)
# Calculo el máximo que se ha vendido
mayorrec = max(total_por_sucursal)   
indice_sucursal = 1
for cant_sucursal in cantidades:
    print('Recaudaciones Sucursal %d: %f' % (indice_sucursal,sum(cant_sucursal)))
    indice_sucursal += 1

# Calculo la sucursal con mayor recaudación
indice_sucursal = 1
for cant_sucursal in total_por_sucursal:
    if cant_sucursal == mayorrec: break
    indice_sucursal += 1

print('Recaudación total de la empresa: %f' % sum(total_por_sucursal))
print('Sucursal de Mayor Recaudación: %d' % indice_sucursal)

*******************************

Ejercicio 15
Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:

Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
de la tabla anterior, y en la segunda los goles del otro equipo.
El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.

¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?


num_equipos = 5
equipos = []
resultados = []

for i in range(0, num_equipos):
    partido = []
    partido.append(f"Equipo {i}")
    partido.append(f"Equipo {i+1}")
    
    equipos.append(partido)
    
    goles = []
    goles.append(f"Goles {i}")
    goles.append(f"Goles {i+1}")
    
    resultados.append(goles)
    
print("------------")

for partido, goles in zip(equipos, resultados):
    print(partido[0], "-", partido[1], ":",end="")
    if goles[0] > goles[1]:
        print("->1")
    else: 
        if goles[0]<goles[1] :
            print("-> 2") 
        else :
            print("-> X")          
*******

Ejercicio 16
Vamos a crear un programa que tenga el siguiente menú:

Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
Longitud de la lista: te muestra el número de elementos de la lista.
Eliminar el último número: Muestra el último número de la lista y lo borra.
Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
Mostrar números: Muestra los números de la lista
Salir



lista = []

while True:
    print("\n")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    
    opcion = int(input("Íntroduce una opcion: "))
    if opcion == 1:
        num = int(input("Dime un numero: "))
        lista.append(num)
    elif opcion == 2:
        num = int(input("Dime un numero: "))
        posicion = int(input("Dime una posicion: "))
        if posicion >len(lista):   
            print("posicion incorrecta")
        else:
            lista.insert(posicion-1, num)
    elif opcion == 3:
        print("Longitud de la lista: %d" % len(lista))
    elif opcion == 4:
        if len(lista)>0:
            print("El ultimo elemento es %d y lo borramos." % lista.pop())
        else:
            print("La lista esta vacia")
    elif opcion == 5:
        posicion = int(input("Dime una posicion (empezando por 1): "))
        if posicion > len(lista):
            print("Posicion incorrecta")
        else:
            print("El elemento es %d y lo borramos."%lista.pop(posicion-1))
    elif opcion == 6:
        numero = int(input("Dime un numero: "))
        print("El numero %d aparece %d veces en la lista" % (num, lista.count(lista)))
    elif opcion == 7:
        num = int(input("Dime un numero: "))
        indice_buscar = 0
        print("Posicion: ", end ="")
        for indice in range(0,lista.count(num)):
            indice_buscar = lista.index(num, indice_buscar)
            indice_buscar += 1    
            print(indice_buscar, " ", end = "")
        print()
    elif opcion == 8:
        for num in lista:
            print(num," ", end ="")
        print()
    elif opcion == 9:
        break
    else:
        print("Opcion incorrecta")


*******************************

Ejercicio 17
Crear un programa que añada números a una lista hasta que 
introducimos un número negativo. A continuación debe crear 
una nueva lista igual que la anterior pero eliminando los números duplicados. 
Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.


lista = []
lista_sin_duplicados = []


num = int(input("Introduce un numero. Negativo para terminar: "))
while num>0:
    lista.append(num)
    num = int(input("Introduce un numero. Negativo para terminar: "))


for num in lista:
    if num not in lista_sin_duplicados:
        lista_sin_duplicados.append(num)

for num in lista_sin_duplicados:
    print(num," ", end="")
print()
********************************



Ejercicio 18
Escriba un programa que permita crear una lista de palabras y que, 
a continuación de tres opciones:

Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
Modificar: Me pide una cadena, y otra cadena a modificar, y 
modifica todas alas apariciones de la primera por la segunda en la lista.
Eliminar: Me pide una cadena, y la elimina de la lista.
Mostrar: Muestra la lista de cadenas
Terminar

lista = []
cadena = input("Introduce una cadena. (* para terminar): ")

while cadena!="*":
    lista.append(cadena)
    cadena = input("Introduce una cadena. (* para terminar): ")
while True:
    print("\n")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Salir")
    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        cadena = input("Introduce una cadena a buscar: ")
        print("La cadena aparece %d veces" % lista.count(cadena))
    elif opcion == 2:
        cadena = input("Introduce una cadena a buscar: ")
        cadena2 = input("Introduce una cadena a modificar: ")
        indice = 0
        for elemento in lista:
                if elemento == cadena:
                    lista[indice] = cadena
                indice +=1
    elif opcion == 3:
        cadena = input("Introduce una cadena a eliminar: ")
        if cadena in lista:
            lista.remove(cadena)
        else:
            print("No existe la cadena en la lista.")
    elif opcion == 4:
        for elemento in lista:
            print(elemento, " ", end ="")
    elif opcion == 5:
        break
    else: 
        print("Opcion incorrecta")
********************************
"""
