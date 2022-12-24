#Leccion 4 - Algebra lineal
import numpy as np

#Numpy nos proporciona métodos para trabajar con álgebra lineal.

a = np.array([[3, 2], [1, 3]])
b = np.array([[2, 2], [1, 2]])

# Producto matricial de dos matrices
np.dot(a, b)

# vdot - Devuelve el producto escalar de dos vectores.
np.vdot(a,b)

#El calculo de arriba sería: 3*2 + 2*2 + 1*1 + 3*2 = 17

# inner - Producto interno de dos matrices.
a = np.arange(6).reshape((2,3))
b = np.arange(3)

np.inner(a, b)

#El calculo sería:
#0 x 0 + 1 x 1 + 2 x 2 = 5
#3 x 0 + 4 x 1 + 5 x 1 = 14


# matrix_power - Eleve una matriz cuadrada a la potencia (entera) n.
m = np.array([[2,3], [1,4]])
np.linalg.matrix_power(m, 2)

#La matriz m^2 es igual a el producto escalar de m x m.
# Podemos comprobar el resultado con np.dot

np.dot(m,m)


#Si no conocéis que son los valores y vectores propios de una matriz, podéis 
# investigar facilmente en la red. Lo que sí debéis saber es que numpy nos 
# proporciona un método para calcularlo de manera rápida y sencilla.

# eig - Calcula los valores propios y los vectores 
# propios rectos de una matriz cuadrada
m = np.diag([4,3,2,1])
m
np.linalg.eig(m)

# det - Calcula el determinante de una matriz.
np.linalg.det(m)
# solve - Resuelve una ecuación con matrices
a

b
a = np.array([[3,1], [1,2]])
b = np.array([9,8])
x = np.linalg.solve(a, b)
x
#El calculo de arriba sería:

#3 * x0 + 1 * x1 = 9
#1 * x0 + 2 * x1 = 8