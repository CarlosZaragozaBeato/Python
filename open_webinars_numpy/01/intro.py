#Seccion 1 - Introducción
#Lección 2 - Conociendo Numpy
import numpy as np
""" 
Numpy es una de las librerías más usadas en el mundo de la ciencia del dato.
Una de las principales ventajas de Numpy es que nos permite trabajar con vectores
y matrices. Por ejemplo, un fichero CSV se puede representar fácilmente en forma 
de matriz, de manera que cada fila de la matriz hace referencia a cada fila del 
fichero, y cada columna de la matriz hace referencia a un atributo del fichero

Las principales características de Numpy son:

-Está escrito en C
-Incluye funciones para operaciones matemáticas, lógicas, ordenación, 
I/O, estadísticas, etc.
-El objeto *ndarray* es el tipo de dato más importante.
-Realmente rápido
-Muy usado en el mundo del Data Science
Veamos un ejemplo en el que Numpy nos hace la vida más fácil
"""
lista_python = [1,2,3,4]
valor = 2
#print(type(lista_python))
lista_python * 2
""" 
Como véis, si multiplico una lista Python * 2, lo que obtengo es la misma lista
dos veces, cosa que habitualmente no buscamos. ¿Cómo implementaría en python 
la multiplicación de los elementos de una lista por un valor?
"""
res = []
valor = 2
for v in lista_python:
    res.append(v * valor)
#print(res)
#Con Numpy, esto es tan simple como realizar la multiplicación
valores_numpy = np.array([1,2,3,4])
#print(valores_numpy * 2)
#¿Y qué ocurre si queremos multiplicar dos listas? 
# Con Python, sería algo tal que así:
lista_python2 = [4,3,2,1]
res = []
for i in range(len(lista_python)):
    res.append(lista_python[i] * lista_python2[i])
#print(res)
#En cambio, en Numpy...
valores_numpy2 = np.array([4,3,2,1])
res = valores_numpy * valores_numpy2
print(res)

""" 
Como podéis ver, Numpy nos hace la vida más facil a la hora de trabajar con listas
(o arrays). ¡¡Imaginaos con matrices!!

Además, hemos dicho Numpy es realmente rápido. Vamos a realizar un par de pruebas 
comparándolo con Python
"""

