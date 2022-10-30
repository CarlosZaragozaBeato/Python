import math
import random

""" 
Ejercicio 1
Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean
desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

numero = int(input("Introduce un numero: "))
diccionario = {}


for i in range(0, numero):
    diccionario[i] = {i:math.pow(i,2)}

print(diccionario)
********************************

Ejercicio 2
Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

cadena = input("Introduce una cadena de texto: ")
dic = {}

for i in cadena:
    num = cadena.count(i)
    dic[i] = {num}

print(dic)

*****************

Ejercicio 3
Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar
los precios de las distintas frutas. El programa pedirá el nombre de la fruta y la 
cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los 
datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada 
consulta el programa nos preguntará si queremos hacer otra consulta.

frutas = {}

nombre = ["Manzana", "Melon", "Sandia", "Pera"]
precio = [2,1,2,3,4]
cantidades = [5,6,4,7,8]

precio_dic = {}

dic_frutas = {}

for i in range(0, len(nombre)):
    dic_frutas[i] = {nombre[i]: precio[i]}
    

for i in range(0, len(dic_frutas)):
    precio_dic[i] = {nombre[i]: dic_frutas[i].get(nombre[i])*cantidades[i]}

print(precio_dic)
    
*****************

Ejercicio 4
Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase
y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre 
e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el 
programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

nombre_alumnos = ["Carlos","Carlos2","Carlos3","carlos4"]
alumnos = {}
notas = []
for i in range(0, len(nombre_alumnos)):
    total_notas = random.randint(1,10)
    for notas_ in range(0, total_notas):
        num_nota = random.randint(1,10)
        notas.append(num_nota)
    alumnos[i] = {nombre_alumnos[i]: notas[:]}
    notas.clear()



print(alumnos)

*****************
Ejercicio 5
Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:

Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo
si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
Listar: Nos muestra todos los contactos de la agenda.
Implementar el programa con un diccionario.


agenda = {}
while True:
    print("\n")
    print("1. Añadir/modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")
    
    opcion = int(input("Dime opcion: "))
    if opcion == 1:
        nombre = input("Nombre Contacto: ")
        if nombre in agenda:
            print("%s ya existe su numero de telefono es %s" %(nombre, agenda[nombre]))
            opcion = input("Pulsa s si quieres modificarlo!!. Otra tecla para continuar: ")
            if opcion == "s":
                numero = input("Numero de telefono: ")
                agenda[nombre] = numero
        else:
            numero = input("Numero de telefono: ")
            agenda[nombre] = numero
    elif opcion == 2:
        cadena = input("Nombre del contacto a buscar: ")
        for nombre, numero in agenda.items():
            if nombre.startswith(cadena):
                        print("El número de teléfono de %s es el %s" % (nombre,agenda[nombre]))
    elif opcion == 3:
        nombre = input("Nombre del contacto para borrar: ")
        if nombre in agenda:
            opcion = input("Pulsa s si quieres borrarlo. Otra tecla para continuar. ")
            if opcion == "s":
                del agenda[nombre]
        else:
            print("No existe el contacto")
    elif opcion == 4:
        for nombre, numero in agenda.items():
            print(nombre,"->", numero)
    elif opcion == 5:
        break
    else:
        print("Opcion incorrecta")        
"""