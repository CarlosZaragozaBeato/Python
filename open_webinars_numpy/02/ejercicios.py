import numpy as np
#Ejercicio 1
#Crea 3 nuevos arrays.

#Array de tipo entero, que contenga solo los números impares del 1 al 100.
#Array de tipo cadena con tu nombre y apellidos
#Array de tipo fechas, que contenga todos los días desde el 
# 01Enero2020 al 04Febrero2020

array_impares = np.arange(1, 100, 2)
array_impares

_ = np.arange(1,100)
array_impares = _[_ % 2 != 0]
array_impares

datos = np.array(['Carlos', 'Zaragoza', 'Beato'])
datos

array_fechas = np.arange('2020-01-01', '2020-02-04', dtype='datetime64[D]')
array_fechas

#Ejercicio 2
#Recupera los últimos 10 elementos del array de impares
array_impares[:len(array_impares)-11:-1]

#Ejercicio 3
#Recorre el array de fechas, y genera un nuevo numpy array que contenga
# unicamente los días laborales

laborables = []
for fecha in array_fechas:
    if np.is_busday(fecha):
        laborables.append(fecha)
laborables_array = np.array(laborables, dtype = 'datetime64')

laborables_array

array_fechas[np.is_busday(array_fechas)]

#Ejercicio 4
#Genera la siguiente matriz.

A = np.matrix('10 1 8 4 ; 3 7 2 1 ; 0 2 20 12')
A

import numpy.ma as ma

A_masked = ma.masked_greater_equal(A, 10)
A_masked

#Ejercicio 5
#Crea dos fechas, la primera de ellas será tu fecha de nacimiento, y la segunda,
# la de un familiar o amigo tuyo.

#¿Qué diferencia en horas hay entre las dos fechas?
#¿Cual sería tu fecha de nacimiento si hubieras nacido 236 horas antes?

fech_naci = np.datetime64('1995-07-03')
fech_naci_hermano = np.datetime64('1999-01-11')

diff = fech_naci - fech_naci_hermano
np.timedelta64(diff, 'h')

print(f"Mi hermano es {str(np.timedelta64(diff, 'h'))} horas mayor que yo")

h = np.timedelta64(236, 'h')
nueva_fechnaci = fech_naci - h
print(f"Mi fecha de nacimiento sería {str(nueva_fechnaci)}")