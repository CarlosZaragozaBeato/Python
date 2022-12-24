#Lección 5 - Trabajando con fechas
import numpy as np
#A partir de NumPy 1.7, existen tipos de datos de matriz central que
# admiten de forma nativa la funcionalidad de fecha y hora. El tipo de 
# datos se llama "datetime64", así llamado porque "datetime" ya está usado 
# por una librería nativa de Python.

#La forma más básica de crear fechas y horas es a partir de cadenas en 
# formato de fecha o fecha y hora ISO 8601. Las unidades de fecha son años 
# ('Y'), meses ('M'), semanas ('W') y días ('D'), mientras que las unidades 
# de tiempo son horas ('h'), minutos ('m' ), segundos ('s'), milisegundos ('ms').
d = np.datetime64('2020-09-01')
d = np.datetime64('2020-13-01')
dh = np.datetime64('2020-09-01T14:30')

#Podemos crear arrays de fechas, pero debemos indicar el tipo de dato.
# En otro caso, aparecerá como tipo cadena.
np.array(['2020-07-01', '2020-08-01', '2020-09-01'])
np.array(['2020-07-01', '2020-08-01', '2020-09-01'], dtype='datetime64')

#También podemos crear arrays de fechas con el iterador de numpy *arange*

np.arange('2020-08', '2020-09', dtype='datetime64[D]')
np.arange('2020-08', '2020-09', dtype='datetime64[W]')

#También podemos realizar comparaciones entre los tipos fechas. Si dos fechas 
# y horas tienen unidades diferentes, es posible que sigan representando el mismo 
# momento de tiempo, y la conversión de una unidad más grande como meses a una
# unidad más pequeña como días se considera un elenco "seguro" porque el momento 
# del tiempo todavía se representa exactamente.

np.datetime64('2020') == np.datetime64('2020-01-01')
np.datetime64('2020-03-14T11') == np.datetime64('2020-03-14T11:00:00.00')

#Operaciones con fechas
#NumPy permite la resta de dos valores de fecha y hora, una 
# operación que produce un número con una unidad de tiempo. 
# Para ello, se crea el tipo *timedelta64*, el cual usa los 
# mismos carácteres de 'Y', 'M', 'D', 'h', 'm', 's' para su creación

np.timedelta64(4, 'D')
np.timedelta64(10, 'h')

#También podemos generar un timedelta, y luego cambiar su unidad.
a = np.timedelta64(8, 'D')
np.timedelta64(a, 'W')

#Cuando restamos dos fechas, también obtenemos un timedelta64 como resultado

np.datetime64('2020-08-01') - np.datetime64('2020-07-01')

## Suma de dias / meses / semanas / etc. a una fecha
np.datetime64('2020-08-01') + np.timedelta64(10, 'D')
np.datetime64('2020-08-01') - np.timedelta64(1, 'W')
np.datetime64('2020-08-01') + np.timedelta64(48, 'h')

#También podemos realizar operaciones directamente entre dos timedeltas distintos
np.timedelta64(1, 'W') + np.timedelta64(4, 'D')

#Hay dos unidades timedeltas ('Y', años y 'M', meses) que se tratan de manera 
# especial, porque el tiempo que representan cambia dependiendo de cuándo se 
# utilizan. Si bien una unidad de día timedelta equivale a 24 horas, no hay forma 
# de convertir una unidad de mes en días, porque los diferentes meses
# tienen diferentes números de días.


a = np.timedelta64(1, 'M')
np.timedelta64(a, 'D')

#Días laborables

#Para permitir que la fecha y hora se use en contextos donde solo ciertos días
# de la semana son válidos, NumPy incluye un conjunto de funciones de 
# “día laborable” (día laboral). El valor predeterminado para las funciones de 
# día laborable es que los únicos días válidos son de lunes a viernes 
# (los días hábiles habituales). La implementación se basa en una "máscara de
# semana" que contiene 7 banderas booleanas para indicar días válidos


np.busday_offset('2020-09-03', 1)
np.busday_offset('2020-09-03', 2)

#Si el día es no laborable, debemos indicar si queremos el siguiente 
# día laborable, o el anterior. Podemos hacerlo con el parámetro roll

np.busday_offset('2020-09-05', 0)
np.busday_offset('2020-09-05', 0, roll = 'forward')
np.busday_offset('2020-09-05', 0, roll = 'backward')

#Para comprobar si un día es laborable, usamos la funcion *np.is_busday*
# Jueves
#print(np.is_busday(np.datetime64('2020-09-03')))
# Sabado
#print(np.is_busday(np.datetime64('2020-09-05')))
#También podemos contar el número de días laborables en un rango de fechas
np.busday_count(np.datetime64('2020-09-01'), np.datetime64('2020-09-30'))


