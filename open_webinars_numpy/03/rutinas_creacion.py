#Sección 3 - Operaciones con Numpy
import numpy as np

#Durante esta sección vamos a conocer las diferentes operaciones que
# tenemos disponibles en Numpy. Una vez conocido en profundidad el tipo array,
# ahora vamos a conocer el amplio abanico de operaciones que tenemos disponibles
# en la librería. Hablaremos de la manipulación y procesamiento de datos, así como
# de funciones lógicas, matemáticas o estadísticas.

#Leccion 1 - Rutinas de creación de arrays
#Hasta ahora hemos visto como crear arrays haciendo uso del 
# contructor ndarray, pero numpy nos proporciona una serie de rutinas 
# para facilitarnos dicha creación. Veamos algunas de ellas.

np.eye(4)

#Posee un parámetro k para poder desplazar la diagonal principal.

np.eye(4, k=1)

# identity - Devuelve un array identidad
np.identity(4, dtype = 'int8')

#ones - Devuelve un array de unos. Podemos definir su dimension
np.ones(shape=(2,3))

# zeros - Devuelve un array de zeros. Podemos definir su dimension
np.zeros(shape=(2,3))

# full - Devuelve una nueva matriz de forma y tipo dados, rellena con fill_value.
np.full(shape=(4,4), fill_value=99)

np.full(shape=(4,4), fill_value=[10,20,30,40])

#Creación desde datos existentes
# fromstring - Una nueva matriz 1-D inicializada a partir de datos de texto
# en una cadena.
np.fromstring('1 2 3 4' , sep = ' ')

datos = np.loadtxt('./Leccion 1 - Rutinas de creación de arrays/datos.txt', delimiter=' ', )
datos


#Rangos numéricos
# arange - Devuelve un array de los valores existentes en un invervalo definido.
# Podemos 
# configurar el tamaño del paso
np.arange(1, 10, 2)
np.arange(10, 1, -2)

# linspace - Devuelve un número de valores entre un intervalo
np.linspace(start=1, stop=10, num = 5, endpoint=False, retstep=True)
np.linspace(start=2, stop= 3.5, num = 10)
# logspace - Igual, pero aplicando una escala logaritmica
np.logspace(start=2, stop= 3.5, num = 10)

#Creación de matrices
# diag - Extrae la diagonal de una matriz o array de dos dimensiones

a = np.eye(N = 4)
a
np.diag(a)
np.diag(a, k = 1)

# diagflat - Crea una matriz bidimensional con la entrada usada como diagonal.
np.diagflat(v = [1,2,3,4], k = 0)
np.diagflat(v = [1,2,3,4], k = -1)
# tri - Una matriz con unos en la diagonal y debajo de ella, 
# y ceros en cualquier otro lugar.
np.tri(N = 5, M = 5)

# asmatrix - Crea un tipo matrix a partir de un array

a = np.array([[1,2,3,4], [4,3,2,1]])
np.asmatrix(a)