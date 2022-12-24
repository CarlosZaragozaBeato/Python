#Ejercicios lecciones 1-4
import numpy as np

#Ejercicio 1
#Genera un array que contenga 25 elementos entre 0 y 99 siguiendo una
# distribución lineal. Luego, transforma ese array en una matriz de 5 x 5.
# ¿Cuál es la diagonal de la matriz? ¿Y la diagonal justo superior?

a = np.linspace(start=0, stop=100, num = 25, endpoint=False)
a

m = a.reshape(5,5)
m

np.diag(m)

np.diag(m, k=1)

#Ejercicio 2
#Crea un de 5 x 4 con el valor repetido 10. Une esa matriz a la matriz del 
# ejercicio anterior para conseguir dos nuevas matrices, una de 5 x 9, y 
# otra de 9 x 5.


m2 = np.repeat(5, 20).reshape(4,5)
m2

np.concatenate((m, m2), axis = 0)

np.concatenate((m, m2.T), axis = 1)

#Ejercicio 3
#Teniendo el array inicial que podéis ver justo abajo, debéis realizar las 
# operaciones necesarias para obtener el array:

#array(['Este', 'Es', 'Un', 'Curso', 'De', 'Openwebinars'], dtype='

#¿Qué elementos del array comienzan por 'E'?


a = np.array(['     este es un curso de openwebinars    '])
a

a1 = np.char.strip(a)
a1


a2 = np.char.split(a1, ' ')
a2 = np.array(a2[0])
a2

a3 = np.char.capitalize(a2)
a3

e = np.char.startswith(a3, 'E')
e

a3[e]

#Ejercicio 4
#Considerando las matrices A y B.

#Realiza la multiplicación matricial de AxB y BxA. ¿Son iguales?
#Realiza la multiplicación de la matriz A x 2
#¿Cúanto es la multiplicación escalar de AxB? ¿y de BxA?

a = np.array([[3,1,2], [4,1,3], [2,0,1]])
b = np.array([[2,0,3], [1,1,1], [0,2,4]])

print(a)
print(b)

#Realiza la multiplicación matricial de AxB y BxA. ¿Son iguales?

axb = np.dot(a,b)
axb


bxa = np.dot(b,a)
bxa
# Realiza la multiplicación de la matriz A x 2
a * 2

# ¿Cúanto es la multiplicación escalar de AxB?
np.vdot(a,b)
np.vdot(b,a)

#Ejercicio 5
#Usando la matriz A del ejercicio anterior, calcula:

#A^3
#El determinante de A
#Resuelve la ecuación Ax = y, siendo *y* el array [3,2,5]
a
b

# A^3
a3 = np.linalg.matrix_power(a, 3)
a3
#Comprobamos realizando la multiplicación matricial
_ = np.dot(a, a)
np.dot(_, a)

# El determinante de A
np.linalg.det(a)

# Resuelve la ecuación Ax = y, siendo y el array [3,2,5]
y = np.array([3,2,5])



np.linalg.solve(a, y)