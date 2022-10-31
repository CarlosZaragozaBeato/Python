from random import randint
import math
"""
Current Exercises
"""





"""

"""

""" Completed

Ejercicio 1
Crea un función EscribirCentrado, que reciba como parámetro un texto y 
lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; 
pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.

def EscribirCentrado(texto):
    print(" "* int(40-(len(texto))/2), texto)
    print(" "* int(40-(len(texto))/2)),"="*(len(texto))

EscribirCentrado("Texto")
********************************


Ejercicio 2
Crea un programa que pida dos número enteros al usuario y 
diga si alguno de ellos es múltiplo del otro. Crea una 
función EsMultiplo que reciba los dos números, y 
devuelve si el primero es múltiplo del segundo.

def esMultiplo(valor1, valor2):
    if int(valor1) % int(valor2) ==0:
        return "Es Multiplo"
    else: 
        return "No es multiplo"
    
print(esMultiplo(4,2))

********************************


Ejercicio 3
Crear una función que calcule la temperatura media de
un día a partir de la temperatura máxima y mínima.
Crear un programa principal, que utilizando la función anterior, 
vaya pidiendo la temperatura máxima y mínima de cada día y vaya 
mostrando la media. El programa pedirá el número de días que se van a introducir.

medias_semana = []

dias_media = int(input("Introduce el total de dias: "))

def calcularMedia():
    min = int(input("Introduce el valor minimo: "))
    max = int(input("introduce el valor maximo: "))
    return (max+min)/2

for i in range(0, dias_media):
    medias_semana.append(calcularMedia())


print(medias_semana)

*******************************
Ejercicio 4
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y 
devuelve una cadena con un espacio adicional tras cada letra. 
Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa 
principal donde se use dicha función.

def ConvertirEspaciado(texto):
    nueva_cadena = ""
    for i in texto:
        nueva_cadena += " "+i
    return nueva_cadena

print(ConvertirEspaciado("Hola, tu"))

*******************************



Ejercicio 5
Crea una función “calcularMaxMin” que recibe una lista 
con valores numéricos y devuelve el valor máximo y el mínimo.
Crea un programa que pida números por teclado y muestre el máximo y el mínimo, 
utilizando la función anterior.

lista_valores = [1,2,3,45,58,74,1,26,844,551,36,-5]


def calcularMaxMix(lista):
    min = lista[0]
    max = lista[0]
    for i in lista:
        if i < min:
            min = i
        if i > max:
            max = i
    return [min, max]

print(calcularMaxMix(lista_valores))

*******************************

Ejercicio 6
Diseñar una función que calcule el área y el perímetro de 
una circunferencia. Utiliza dicha función en un programa principal
que lea el radio de una circunferencia y muestre su área y perímetro.

def calcularAreaPerimetro(radio):
    area = math.pi * math.pow(radio,2)
    perimetro = 2 * math.pi * radio
    return area, perimetro

area, perimetro = calcularAreaPerimetro(5)

print(f"El area es {area}, y el perimetro {perimetro}")

*******************************

Ejercicio 7
Crear una subrutina llamada “Login”, que recibe 
un nombre de usuario y una contraseña y te devuelve
Verdadero si el nombre de usuario es “usuario1” y 
la contraseña es “asdasd”. Además recibe el número de
intentos que se ha intentado hacer login y si no se ha 
podido hacer login incremente este valor.

Crear un programa principal donde se pida un nombre de usuario y 
una contraseña y se intente hacer login, solamente tenemos tres
oportunidades para intentarlo.

num_valor = 0
def Login(usuario, password, num_valor):
    if usuario == "usuario1" and password == "asdasd":
        return True
    else :
        num_valor +=1
        return False


while True:
    name = input("Introduce el nombre de usuario: ")
    password = input("Introduce la contraseña: ")
    if Login(name, password, num_valor):
        break
    else:
        if num_valor == 3:
            print("No puedes volver a intentarlo.")
            break
        else:
            print("Vuelve a intentarlo.")
*******************************


Ejercicio 8
Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.

def factorial(num):
    if num ==0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(5))

*******************************
Ejercicio 9
Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:

Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD.


def Intercambiar(mayor, menor):
    if mayor < menor:return menor, mayor
    else : return mayor, menor

def CalcularMCD(num1, num2):
    num1, num2 = Intercambiar(num1, num2)
    resto = num1 % num2
    if resto == 0: return num2
    else: return CalcularMCD(num2, resto)
    
numero1 = int(input("Introduce el numero uno: "))
numero2 = int(input("introduce el numero dos: "))
print("MCD: ", CalcularMCD(numero1, numero2))
*******************************



Ejercicio 10
Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.


def ConvertirSegundos(h,m,s):
    return h*3600+m*60+s

def Convertir_HMS(seg):
    h = seg/3600
    seg = seg -h*3600
    min = seg//60
    seg = seg - min*60
    s = seg
    return h,min,s

while True:
    print("1.- Convertir a segundos.")
    print("2.- Convertir a horas, minutos y segundos.")
    print("3.- Salir.")
    opcion = int(input())
    if opcion == 1:
        hor = int(input("Horas: "))
        min = int(input("Minutos: "))
        seg = int(input("Segundos: "))
        print("Corresponde a",ConvertirSegundos(hor,min,seg)," segundos.")
    elif opcion == 2:
        segund = int(input("Segundos: "))
        hor, min, seg = Convertir_HMS(segund)
        print("Corresponde a", hor,":", min,":",seg)
    elif opcion == 3:
        break
    else: 
        print("Opcion Incorrecta")
*****************************
Ejercicio 11
El día juliano correspondiente a una fecha es un número entero que indica los días que han
 transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que 
 al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
EsBisiesto: Recibe un año y nos dice si es bisiesto.
Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.


try:
    fecha = input("Introduce una fecha (##/##/####): ")

    trozos = fecha.split("/")
    dia = trozos[0]
    mes = trozos[1]
    anio = trozos[2]
except:
    print("ERROR")




def bisiesto(anio):
    if anio % 4 == 0 and anio %100==0 and anio % 400 ==0:
        return True
    else: return False



def Dias_Mes(mes, anio):
    if mes == 1:
        return 31
    elif mes == 2:
        if bisiesto(anio):
            return 29
        else:
            return 29
    elif mes == 3:
        return 31
    elif mes == 4:
        return 30
    elif mes == 5:
        return 31
    elif mes == 6:
        return 30
    elif mes == 7:
        return 31
    elif mes == 8:
        return 31
    elif mes == 9:
        return 30
    elif mes == 10:
        return 31
    elif mes == 11:
        return 30
    elif mes == 12:
        return 31
    else:
        return "Introduce un mes correcto."
print(Dias_Mes(2, 2016))


def CalcularDiaJuliano(anio, mes, dia):
    
    total_dias = dia
    for i in range(1,mes+1):
        total_dias+=Dias_Mes(i, anio)
    return total_dias

print(CalcularDiaJuliano(2008, 2,0))
**********************************
Ejercicio 12
Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer una fecha se asegura que es válida.
*****************************************
Current Exercise
Ejercicio 13
Queremos crear un programa que trabaje con fracciones a/b. 
Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.

Vamos a crear las siguientes funciones para trabajar con funciones:

Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1,
 se muestra sólo el numerador.
Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.

Restar_fracciones: Función que resta dos fracciones: Se debe simplificar la fracción resultado.

Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2.
 Se debe simplificar la fracción resultado.
Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.
Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:

Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
Salir

Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra 
fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.

def Leer_Fraccion():
    numerador = int(input("Introduzca el numerador: "))
    denominador = int(input("Introduzca el denominador: "))
    return numerador, denominador

def Mostrar_Fraccion(numerador, denominador):
    if denominador == 1:
        return numerador
    else:
        return numerador,"/",denominador

def Intercambiar(num1, num2):
    if num1<num2:
        return num2, num1
    else: return num1, num2

def CalcularMCD(num1, num2):
    num1, num2 = Intercambiar(num1, num2)
    resto = num1 % num2
    if resto == 0: return num2
    else: return CalcularMCD(num2, resto)

def Simplificar_Fraccion(numerador, denominador):
    MCD = CalcularMCD(numerador, denominador)
    numerador = numerador/MCD
    denominador = denominador/MCD
    return numerador, denominador

def Sumar_Fracciones(n1, n2, d1,d2):
    n_total = n1+n2
    d_total = d1+d2
    return  n_total, d_total

def Restar_Fracciones(n1,n2,d1,d2):
    valor_numerador = (n1*d2) - (d1,n2)
    valor_denomindor = d1*d2
    return valor_numerador, valor_denomindor

def Multiplicar_Fracciones(n1,n2,d1,d2):
    numerador = n1 * n2
    denominador = d1 * d2
    return Simplificar_Fraccion(numerador, denominador)
*******************************
Ejercicio 14
Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables.
La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar.

Para representar una pila vamos a utilizar una lista de cadenas de caracteres.

Vamos a crear varias funciones para trabajar con la pila:

LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.
EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.
EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.
AddPila: función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, si no está llena. si esta llena muestra un mensaje de error.
SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía muestra un mensaje de error.
EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.
Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, con las siguientes opciones:

Añadir elemento a la pila
Sacar elemento de la pila
Longitud de la pila
Mostrar pila
Salir


lista = []

def Longitud_Pila(lista):
    return len(lista)

def EstaVaciaPila(lista):
    if len(lista) == 0:
        return True
    else: return False

def EstaLlenaPila(lista):
    if len(lista) == 15:
        return True
    else: False

def AddPila(cadena, lista):
    if EstaLlenaPila(lista):
        return "La pila esta llena"
    else: 
        return lista.append(cadena)

def SacarDePila(cadena, lista):
    if EstaVaciaPila(lista):
        return "La pila esta vacia"
    else:
        lista.remove(cadena)

cadena = "CARLOS"



def MostrarPila(lista):
    if EstaVaciaPila(lista):
        return "La pila esta vacia"
    else:
        for i in lista:
            print(i)




AddPila(cadena, lista)

print(lista)

SacarDePila(cadena,lista)

print(len(lista))

*******************************
Ejercicio 15
Vamos a realizar un programa similar al anterior para trabajar con una cola. Una cola es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el primer elemento que se añade al conjunto es el primero que se puede sacar.

En realizada nos sirven todas las funciones del ejercicio 
anterior menos la función SacarDeLaCola que es la que tienes que modificar.


def LongitudCola(cola):
    return len(cola)

def EstaVaciaCola(cola):
    return len(cola) == 0

def AddCola(cad,cola):
    cola.append(cad)

def SacarDeLaCola(cola):
    if not EstaVaciaCola(cola):
        return cola.pop(0)
    else:
        print("No se puede sacar elemento. La cola esta vacia.")
        return ""
    
def EscribirCola(cola):
    for elem in cola:
        print(elem, end =" ")
    print()
    
micola = []
while True:
	print("1.- Añadir elemento a la cola")
	print("2.- Sacar elemento de la cola")
	print("3.- Longitud de la cola")
	print("4.- Mostrar cola")
	print("5.- Salir")
	opcion = int(input())
	if opcion == 1:
		elem = input("Dame la cadena para añadir a la cola:")
		AddCola(elem,micola)
	elif opcion == 2:
		print(SacarDeLaCola(micola))
	elif opcion == 3:
		print("Longitud: ",LongitudCola(micola))
	elif opcion == 4:
		EscribirCola(micola)
	elif opcion == 5:
		break
	else:
		print("Opción incorrecta")
	

"""