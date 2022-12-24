#Leccion 3 - Indexado y recorrido de arrays
import numpy as np
""" 
Podemos consultar un campo del array con los carácteres []. 
Tenemos que recordar que en python, los indices comienzan por cero,
por lo que si queremos consultar el primer elemento de un array lo haríamos 
de la siguiente manera
"""

a = np.array([0,1,2,3,4,5,6,7,8,9])
#print(a[0])
#print(a[9])
#print(a.shape)
#print(a[10])
#Slicing
"""
Podemos consultar distintos elementos del array con el slicing.
En el slice tenemos que definir: inicio:fin:paso
"""
#print(a[0:9:2])
#print(a[0:8:3])
#Podemos recuperar los dos últimos elementos, usando valores negativos
a[-2:10]
#También podemos recorrer los valores de mayor a menor definiendo el tamaño
#del paso como un nº negativo
a[9::-1]
#También podemos definir solo el inicio, o el fin
a[:5]
a[5:]
""" 
Para los array multidimensionales funciona del mismo modo. Solo tenemos que verlos 
en forma de matriz, y consultar la fila y columna que deseemos
"""
a = np.array([[1,2,3], [3,4,5]], dtype = np.int8)
a[1][0]
a[1,0]
a[1, 0:2]
a[0:2, 0:2]
#Exactamente igual funciona cuando hablamos de un tipo matrix
#Indexado booleano
a = np.array([0,1,2,3,4,5,6,7,8,9])
a > 4
#La operación a > 4 nos devuelve un array de True y False. 
#Este mismo array, lo podemos enviar a nuestro array para realizar una consulta.
a[a>4]
bool_array = np.array([True, False,True, False,True, False,True, False,True, False])
a[bool_array]
a % 2 == 0
a[a % 2 == 0]

#También actuamos de la misma forma cuando el array es de tipo char

char_array = np.array(['Openwebinars', 'Machine Learning', 'Numpy'])
char_array

char_array[char_array == 'Numpy']


#Recorrido
#El objeto iterador nditer, introducido en NumPy 1.6, proporciona muchas 
# formas flexibles de visitar todos los elementos de una o más matrices de 
# forma sistemática. Además del iterador nditer, el cual es un poco más complejo,
# también podemos recorrer los elementos de un array con un simple bucle for.

a = np.array([0,1,2,3,4,5,6,7,8,9])

for valor in a:
    print(valor)

for valor in np.nditer(a):
    print(valor)