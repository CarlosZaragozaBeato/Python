#Sección 2 - Arrays
import numpy as np
#Lección 2 - Tipos de datos

""" 
Python define solo un tipo por cadaclase de datos en particular
(solo hay un tipo de entero, un tipo de float, etc.). Esto puede tener sentido 
en aplicaciones que no necesitan preocuparse por las distintas formas en en que se 
pueden representar los datos en un ordenador. Sin embargo, cuando trabajamos con
el análisis de datos, a menudo necesitamos más control.

En NumPy, hay 24 nuevos tipos fundamentales de Python para describir diferentes 
tipos de escalares. Estos descriptores de tipo se basan principalmente en los tipos
disponibles en el lenguaje C en el que está escrito CPython, con varios tipos
adicionales compatibles con los tipos de Python.
"""

a = np.array([1,2,3,4], dtype=np.int_)
bool_array = np.array([[1,0,0,1], [0,1,1,0]], dtype = np.bool)
char_array = np.array(['a','b','c'], dtype = np.chararray)

""" 
Además, cada uno de los tipos de la jerarquía que vemos arriba, 
poseen tipos de datos con distinto tamaño. Esto significa, capaces 
de almacenar un número distinto de bits. Por ejemplo:

Para los *int* tenemos:

int8 → Máximo 8 bits
int16 → Máximo 16 bits
int32 → Máximo 32 bits
int64 → Máximo 64 bits
Para los *float* tenemos:

float16 → Máximo 16 bits
float32 → Máximo 32 bits
float64 → Máximo 64 bits
"""
from sys import getsizeof

a = np.array([1,2,3,4], dtype = np.int8)
b = np.array([1,2,3,4], dtype = np.int64)
#print("A", getsizeof(a))
#print("B", getsizeof(b))
#print(a.dtype)
#print(b.dtype)
#print(bool_array.dtype)

dt = np.dtype('int32')
#print(dt.type)
dt.type is np.int32

"""
Además, podemos crear tipos de datos con una combinación de 'carácter' + 'nº 
de bytes'. Los carácter que podemos usar son:

'?' : boolean
'b' : (signed) byte
'B' : unsigned byte
'i' : (signed) integer
'u' : unsigned integer
'f' : floating-point
'c' : complex-floating point
'm' : timedelta
'M' : datetime
'O' : (Python) objects
'S', 'a' : zero-terminated bytes (not recommended)
'U' : Unicode string
'V' : raw data (void)
"""
dt = np.dtype('f8')
a = np.array([1,2,3,4], dtype = dt)
#print(a)
#print(a.dtype)
dt = np.dtype('int32')
dt.kind
#Un tipo de dato muy importante en Numpy es el NaN, o valor nulo.
nan = np.nan
np.isnan(nan)
x = np.array([[1., 2.], [np.nan, 3.], [np.nan, np.nan]])
""" 
El tipo matrix
Los objetos de matriz heredan del ndarray y, por lo tanto, tienen los 
mismos atributos y métodos que ndarrays. Sin embargo, las matrices solo 
pueden tener dimensión 2.
"""
m = np.matrix('1 2 3 ; 4 5 6')
m = np.mat([[1,2,3], [3,4,5]], dtype = np.float16)
a = np.array([[1,2,3], [3,4,5]], dtype = np.float16)
#print(type(a))
m = np.asmatrix(a)
#print(type(m))
