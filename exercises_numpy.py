import numpy as np
#1 Obtener version y configuracion
#print(np.__version__)
#print(np.show_config())
######################################################
#2 Obtener Información de la Función add de Numpy
#print(np.info(np.add))
######################################################
#3 Comprobar si un Arreglo tiene Elementos Igual a Cero
#a = [1,3,5,7,0]
#print(np.all(a))
######################################################
#4 Comprobar si en un Arreglo Existe al menos un Elemento Distinto de Cero
#a = [np.array([0,0,1,0])]
#print(np.any(a))
#######################################################
#5 Comprobar si los Elementos de un Arreglo son Finitos
#a = [0,1,2,np.nan,np.inf, -np.inf]
#print(np.isfinite(a))
######################################################
#6 Comprobar si los Elementos de un Arreglo son Finitos
#a = [0,1,2,np.nan,np.inf, -np.inf]
#print(np.isinf(a))
######################################################
#7 Comprobar si los Elementos de un Arreglo NumPy son Nulos
#a = [1,1,2,5,4,6,np.nan]
#print(np.isnan(a))
#######################################################
#8 Comprobar si cada Elemento de un Arreglo es un Número Real, Complejo, o Escalar
#a = np.array([1,2,5,8,-1+3j,3,2j])
#b = 5.5
#print(np.iscomplex(a))
#print(np.isreal(a))
#print(np.isscalar(b))
#######################################################
# 9 Comprobar si Dos Arreglos son Iguales Bajo un Grado de Tolerancia
#print(np.allclose([1e10,1e-7],[1.000001e10, 1e-8]))
#print(np.allclose([1e10,1e-8],[1.000001e10, 1e-9]))
#print(np.allclose([1.0, np.nan],[1.0,np.nan],equal_nan=True))
#######################################################
#10 Aplicar Operadores Relacionales a Cada Elemento de Dos Arreglos
#a = np.array([5,7])
#b = np.array([3,7])
#print(np.less(a,b))
#print(np.less_equal(a,b))
#print(np.greater(a,b))
#print(np.greater_equal(a,b))
#######################################################
#11 Comprobar Igualdad con Tolerancia Elemento a Elemento de Dos Arreglos
#a = np.array([1,2,3,3])
#b = np.array([1,2,3,3.0000001])
#print(np.isclose(a,b, rtol=1e-9))
#######################################################
#12 Obtener el Tamaño en Bytes que Ocupa un Arreglo NumPy
#a = np.array([2,3,5,7,11])
#print(a.size * a.itemsize)
#######################################################
#13 Crear Tres Arreglos con 10 Ceros, 10 Unos, y 10 Sietes
#a1 = np.zeros(10)
#a2 = np.ones(10)
#a3 = np.ones(10) * 7
#print(a1)
#print(a2)
#print(a3)
#######################################################
#14 Crear un Arreglo con Enteros entre 20 y 50
#a = np.arange(20,51)
#print(a)
#######################################################
#15 Crear un Arreglo con Enteros Pares entre 20 y 50
#a= np.arange(20,51,2) 
#print(a) 
#######################################################
#16 Crear una Matriz Identidad
#matriz = np.identity(3)
#print(matriz)
#######################################################
#17 Generar un Número Aleatorio entre 0 y 1 (Exclusivo)
#numero = np.random.random()
#print(numero)
#######################################################
#18 Generar 10 Números Aleatorios Siguiendo una Distribución Normal Estándar
#aleatorios = np.random.normal(0,1,10)
#print(aleatorios)
#######################################################
#19Crear un Rango de Números y Excluir el Primer y Último Elemento
#rango = np.arange(15,55)
#print(rango[1:-1])
#######################################################
#20 Crear un Matriz de 4x3 e Imprimir su Contenido
#arreglo = np.arange(1,13).reshape(4,3)
#for i in np.nditer(arreglo):
#    print(i, end =" ")
#######################################################
#21 Crear un Arreglo con 5 Valores Distribuidos Uniformemente entre 10 y 50
#arreglo = np.linspace(10, 50, 5)
#print(arreglo)
#######################################################
#22Crear un Arreglo con Valores 0 a 9, e Invertir el Signo de los Valores 5 a 7
#arreglo = np.arange(10)
#arreglo[(arreglo>=5) & (arreglo<=7)]*=-1
#print(arreglo)
#######################################################
#23 Crear Arreglo con 5 Elementos con Valores Aleatorios
#arreglo = np.random.randint(0,11,5)
#print(arreglo)
#######################################################
#24 Multiplicar Elemento a Elemento dos Arreglos
#a1 = np.array([1,2,3,4])
#a2 = np.array([5,6,7,8])
#resultado = a1*a2
#print(resultado)
#######################################################
#25 Crear una Matriz de 3x4 con Valores de 1 a 12
#matriz = np.arange(1,13).reshape((3,4))
#print(matriz)
#######################################################
#26: Obtener la Cantidad de Filas y Columnas de una Matriz
#matriz = np.arange(1,13).reshape((3,4))
#print(matriz.shape)
#######################################################
#27: Crear una Matriz Identidad de 5x5
#m_identidad = np.eye(5)
#print(m_identidad)
#######################################################
#28: Crear una Matriz Marco
#matriz = np.ones((10,10))
#matriz[1:-1,1:-1] = 0
#print(matriz)
#######################################################
#29: Crear una Matriz de 5x5 con los Valores 1 a 5 en la Diagonal Principal
#matriz = np.diag([1,2,3,4,5])
#print(matriz)
#######################################################
#30: Crear una Matriz 4x4 con 0 y 1 Escalonados
#matriz = np.zeros((4,4))
#matriz[::2,1::2] = 1
#matriz[1::2,::2]=1
#print(matriz)
#######################################################
#31: Crear un Arreglo Tridimensional con Valores Aleatorios
#a = np.random.random((3,3,3))
#print(a)
#######################################################
#32: Sumar Todos los Elementos de una Matriz
#matriz = np.array([[1,2,3], [4,5,6]])
#print(np.sum(matriz,axis=0))
#######################################################
#33: Calcular el Producto Punto entre Dos Vectores (Arreglos)
#a = np.array([3,5])
#b = np.array([2,3])
#print(np.dot(a,b))
#######################################################
#34: Sumar un Arreglo a Cada Fila de una Matriz
#m = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#a = np.array([1,1,0])
#resultado = np.empty_like(m)
#for i in range(4):
#    resultado[i, :] =  m[i,:]+a 
#print(resultado)
#######################################################
#35: Guardar un Arreglo en Formato Binario
#arreglo = np.arange(20)
#np.save('ejercicio35.npy', arreglo)
#import os
#if os.path.exists('ejercicio35.npy'):
#    arreglo2 = np.load('ejercicio35.npy')
#    print(arreglo2)
#    print(np.array_equal(arreglo2, arreglo))
#######################################################
#36: Guardar dos Arreglos en Formato Comprimido (.npz) y Cargarlos
#a = np.arange(1,5)
#b = np.arange(6,10)
#np.savez('ejercicio36.npz',x=a, y=b)
#with np.load('ejercicio36.npz') as archivo:
#    a1 = archivo['x']
#    b1 = archivo['y'] 
#    print(a1, b1)
#######################################################
#37: Guardar un Arreglo en un Archivo de Texto, y luego Cargar el Archivo
#import os
#matriz = np.arange(12).reshape(3,4)
#encabezado = 'col1 col2 col3 col4'
#np.savetxt('ejercicio37.txt', matriz, fmt="%d", header=encabezado)
#matriz2 = np.loadtxt('ejercicio37.txt')
#print(matriz2)
#######################################################
#38: Convertir un Arreglo en Bytes y Luego Revertir su Conversión
#a = np.array([2,3,5,7,11])
#a_bytes = a.tostring()
#a2 = np.fromstring(a_bytes, dtype=a.dtype)
#print(a2)
#######################################################
#39: Crear un Arreglo a Partir de una Lista, y Obtener la Lista Original
#lista = [2,3,5,7,11]
#arreglo = np.array(lista)
#lista_2 = arreglo.tolist()
#print(lista_2)
#######################################################
#40: Crear una Gráfica
#import matplotlib.pyplot as plt
#x = np.arange(0,3*np.pi,0.2)
#y = np.sin(x)
#plt.plot(x,y)
#plt.show()
#######################################################