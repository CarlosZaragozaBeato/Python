#Lección 8 - Funciones estadísticas
import numpy as np
#Las funciones estadísticas también son realmente interesantes.
# Son bastante usadas cualquier analísis de datos
#Funciones relacionadas con el orden
# min y max devuelven los valores minimos y maximos de un array
a = np.array([2,5,6,10])
print("Min", np.min(a))
print("Max", np.max(a))

b = np.arange(12).reshape(3,4)
b

np.min(b, axis = 1) # Axis 1 por filas

np.min(b, axis = 0) # Axis 0 por columnas


# percentile - Calcule el percentil q-ésimo de los datos a lo largo del eje especificado.
b = np.arange(0, 101)
b

np.percentile(b, q = 11)
# Idem para el quantil. 

np.quantile(b, q = 0.25)

#Medias y varianzas
# median - Calcula la mediana (valor central)
np.median(b)
np.median(np.array([1,2,0,100,200,300,50]))

# average o media (con pesos)
a = np.array([1,2,3,4])
np.average(a)

np.average(a, weights=[2,2,1,1])
# mean - Practicamente idéntico
b = np.arange(12).reshape(4,3)
b

np.mean(b, axis = 0) # Media por columnas
np.mean(b, axis = 1) # Media por filas

# std - Desviacion estándar
np.std(b, axis = 0)
np.std(b)

#La desviación estándar es la raíz cuadrada del promedio de las desviaciones 
# al cuadrado de la media, es decir:

#std = sqrt(mean(abs(x - x.mean())**2))

# var - Varianza
np.var(b, axis = 1)

#La varianza es el promedio de las desviaciones cuadradas de la media, es decir:

#var = mean (abs (x - x.mean ()) ** 2).

#La desviación estándar es la raiz cuadrada de la varianza.

std = np.std(b, axis = 0)
print(std)
var = np.var(b, axis = 0)
print(var)

np.sqrt(var)


