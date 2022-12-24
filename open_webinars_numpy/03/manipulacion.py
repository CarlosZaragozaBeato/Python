import numpy as np

#Leccion 2 - Manipulación de arrays
#Dimensiones del array

# shape - Recuperas la dimension
a = np.array([[1,2,3,4], [4,3,2,1]])
a.shape

# reshape - Modificar la dimension
a.reshape((4,2))
# ravel - Aplana un array de más de 1D
a.ravel()

a.T
#Tipos de arrays

# asarray - Convierte una lista python en numpy array
np.asarray([1,2,3,4], dtype = np.int8)


# asfarray - Igual, pero devuelve el array de tipo float
np.asfarray([1,2,3,4])
np.asfarray([1,2,3,4], dtype = np.int8)


# asarray_chkfinite - Convierte la entrada en un array, verificando NaN o Infs.

a = [1,2,3,4, np.nan]
np.asarray_chkfinite(a)

# repeat - Genera un array de números iguales
a = np.repeat(a = 99, repeats=10)
a
a.reshape((2,5))

#Union de arrays

# concatenate - Une un conjunto de arrays por filas o columnas
a = np.array([[1,2,3,4], [1,2,3,4]])
b = np.array([[4,3,2,1]])

print(a.shape)
print(b.shape)

np.concatenate((a,b), axis = 0)
np.concatenate((a.T, b.T), axis=1)

# stack - Parecido a join, pero genera un nuevo indice
a = np.array([1,2,3,4])
b = np.array([4,3,2,1])

np.stack(arrays=(a,b), axis = 1)
np.stack(arrays=(a,b), axis = 0)

#Division de arrays

# split - Divide un array en varios 
a = np.arange(0, 20)
a
np.split(a, indices_or_sections=4)
np.split(a, [3, 5, 10, 16])

#Añadir y eliminar elementos
# insert - Inserta elementos en una posicion del array


a = np.array([1,2,3,4])
a

np.insert(a, obj=4, values=[5,6])
np.insert(a, obj=1, values=[5,6])

# append - Inserta elementos al final del array
np.append(a, [5,6])

# delete - Elimina un elemento del array
np.delete(a, obj = 3)


# trim_zeros - Elimina los 0s al inicio y el final del array
a = np.array([0, 0, 0, 0, 1, 2, 3, 4, 0, 0])
np.trim_zeros(a)

# unique - Deja los elementos unicos del array
a = np.array([1,1,1,1,2,2,2,2,3,3,3,3])
np.unique(a)
