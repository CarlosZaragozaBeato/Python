#Sección 2 - Arrays
import numpy as np
""" 
Durante esta sección vamos a trabajar con el tipo de datos "array",
aprendiendo como podemos generarlos, recorrerlos, consultarlos, etc

Comenzamos creando distintos tipos de arrays simples

Un *ndarray* es un conjunto multidimensional (generalmente de tamaño fijo) 
de elementos del mismo tipo y tamaño. El número de dimensiones y elementos 
en una matriz se define por su forma, que es una tupla de N números enteros 
no negativos que especifican los tamaños de cada dimensión. El tipo de elementos
de la matriz se especifica mediante un objeto de tipo de datos independiente 
(dtype), uno de los cuales está asociado con cada ndarray.

El constructor a bajo nivel de ndarray es np.ndarray, pero no se recomienda su
uso. Para la creación de arrays, se recomienda usar los métodos:

array: Construye un nuevo array
zeros: Construye un array de zeros
ones: Construye un array vacío
También es intesante el método dtype
"""

array1 = np.array([1,2,3,4,5,6], dtype = 'int')
#print(type(array1))
#print(array1)
array2 = np.array([[1,2,3],[4,5,6]], dtype = 'int', ndmin=2 )
#print(array2)
array3 = np.array([1,2,3], dtype = 'complex')
#print(array3)
np.zeros(10)
np.zeros((5,2))
np.ones(10)
np.ones((5,2))
a = np.arange(10)
a.reshape((2,5))

