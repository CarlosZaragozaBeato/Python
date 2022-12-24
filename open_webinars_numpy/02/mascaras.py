#Leccion 4 - Mascaras
import numpy.ma as ma
import numpy as np
#En muchas circunstancias, los conjuntos de datos pueden estar incompletos o
# contaminados por la presencia de datos no válidos. Por ejemplo, es posible 
# que un sensor no haya podido registrar datos o haya registrado 
# un valor no válido. El módulo numpy.ma proporciona una forma conveniente de 
# abordar este problema mediante la introducción de matrices enmascaradas.

#Una matriz enmascarada es la combinación de un numpy.ndarray estándar y 
# una máscara. Cuando un elemento de la máscara es False, el elemento 
# correspondiente de la matriz asociada es válido y se dice que está desenmascarado. 
# Cuando un elemento de la máscara es True, se dice que el elemento correspondiente
# de la matriz asociada está enmascarado (no válido).




x = np.array([1,2,3,-1,4])

# Definimos el valor negativo como invalido
mask_array = ma.masked_array(x, mask = [0,0,0,1,0])
#print(mask_array)
mask_array.min()
#También podemos definir la máscara directamente en el
# constructor de array del modulo ma.
x = ma.array([1,2,3,-1,4], mask = [0,0,0,1,0])

#Si queremos recuperar únicamente los valores válidos, usamos el método compressed
x.compressed()

#Puedo enmascarar o desenmascarar todos los elementos asignando 
# True o False a toda la máscara.

x.mask = True
x.mask = False
x.mask = [0,0,0,1,0]

#Podemos consultar si un valor es válido con el método ma.masked
#print(x[0] is ma.masked)
#print(x[3] is ma.masked)
#Podemos 'rellenar' los valores enmascarados con un valor concreto.
x.filled(0)

#Algunos métodos interesantes para la gestión de máscaras son:
x = np.array([1,2,3,-1,4])
masked = ma.masked_equal(x, 4)
masked = ma.masked_equal(x, 4)
masked = ma.masked_where(x<2, x)
masked = ma.masked_greater_equal(x, 2)
masked = ma.masked_inside(x, 1, 3)


