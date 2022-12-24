#Leccion 7 - Funciones matemáticas
import numpy as np

#Dentro de todas las funciones matemáticas que tenemos disponibles 
# en Numpy, destacamos las siguientes categorías.

#Redondeo
a = 2.49264

# round - Redonde un número a las cifras que definamos
np.round(a, 1)

array = np.array([1.435, 13.1435, 4.916])
np.round(array, 2)

# floor - Devuelve el suelo - el número entero pequeño más cercano
np.floor(array)

# Devuelve el techo - el siguiente número entero
np.ceil(array)

#Sumas y productos

# prod - Devuelve el producto de los elementos de la matriz sobre un eje dado
b = np.array([2,3,4])
np.prod(b)

b = np.array([[2,3,4],[2,2,2]])
np.prod(b, axis = 0)

np.prod(b, axis = 1)

# sum - Mismo funcionamiento que prod, pero en este caso realizando la suma

np.sum(b)

np.sum(b, axis = 0)

np.sum(b, axis = 1)

#Exponentes y logaritmos

#exp - Calcula el exponencial de todos los elementos en la matriz de entrada.
b
np.exp(b)

#El exponencial se calcula como el número e elevado al escalar.
# Es decir, es equivalente a:

np.power(np.e, b)

#Para el cálculo de logaritmos tenemos las opciones:

#log: base e
#log10: base 10
#log2: base 2

p = np.power(np.e, b)
np.log(p)

np.log10(b)

np.power(10, np.log10(b))

np.log2(b)

np.power(2, np.log2(b))

#Operaciones aritméticas
#Hacen referencia a operaciones básicas de suma, resta, multiplicación o 
# división de cada elemento del array.

a = np.array([[1,2,3,4], [4,3,2,1]])
b = np.array([4,3,2,1])

# Suma
np.add(a,b)

# Resta
np.subtract(a,b)

# Multiplicacion
np.multiply(a,b)


# Division
np.divide(a,b)