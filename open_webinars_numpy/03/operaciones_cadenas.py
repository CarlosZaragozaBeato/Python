#Leccion 3 - Operaciones con cadenas
import numpy as np
#The numpy.char module provides a set of vectorized string operations for 
# arrays of type numpy.string_ or numpy.unicode_.


# add - Devuelve la concatenación de cadenas de elementos para 
# dos matrices de str o unicode.
a = np.array(['A', 'B', 'C'], dtype = np.str)
b = np.array(['D', 'E', 'F'], dtype = np.str)

np.char.add(a,b)

# multiply - Devuelve (a * i), es decir, concatenación múltiple 
# de cadenas, por elementos.
np.char.multiply(a, [2,3,4])


# capitalize - Devuelve una copia de a con solo el primer 
# carácter de cada elemento en mayúscula.
nombres = np.array(['maria', 'antonio', 'francisco'], dtype = np.str)
np.char.capitalize(nombres)


# replace - Devuelve un array después de reemplazar los caracteres
np.char.replace(nombres, 'mar', 'sof')

# split - Para cada elemento de a, devuelve una lista de 
# las palabras de la cadena, utilizando sep como cadena delimitadora.
nombre = np.array(['Mi nombre es Abraham Requena'])
np.char.split(nombre, sep=' ')


c = np.array(['  Hola  ', '  Adios '])
np.char.strip(c)

#Comparación

# equal - Valores iguales
a = np.array(['A', 'B', 'C'], dtype = np.str)
b = np.array(['D', 'B', 'F'], dtype = np.str)

np.char.equal(a,b)
np.char.not_equal(a,b)
# greater_equal . Compara el mayor o igual a nivel cadena. A < B, o F > C
np.char.greater_equal(a,b)

# less_equal
np.char.less_equal(a,b)

#Información sobre la cadena


# endswith - Devuelve True si la palabra acaba en el char que definimos
c = np.array(['Hola', 'Adios'])
np.char.endswith(c, suffix='ios')


# startswith - Devuelve True si la palabra comienza en el char que definimos
np.char.startswith(c, prefix='Ad')


# islower - Devuelve True si todos los caracteres están en minusculas
c = np.array(['HOLA', 'adios'])
np.char.islower(c)


# islower - Devuelve True si todos los caracteres están en mayusculas
c = np.array(['HOLA', 'adios'])
np.char.isupper(c)


# isdigit - Devuelve True si todos los elementos son numericos
c = np.array(['HOLA', 'adios', '123'])
np.char.isdigit(c)