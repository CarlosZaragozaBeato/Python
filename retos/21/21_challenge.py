"""
 * Reto #21
 * CALCULADORA .TXT
 * Fecha publicación enunciado: 23/05/22
 * Fecha publicación resolución: 01/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
"""


texto = open("C:/Users/carlo/Desktop/retos/Python-Exercises/retos/21/21.txt","r")

lineas = texto.read().split("\n")


i =0

rango = len(lineas)-1
while i<rango:
    if '*' in lineas or '/' in lineas:
        if lineas[i]=="*" :
            lineas[i] = int(lineas[i-1]) * int(lineas[i+1])
            del(lineas[i+1])
            del(lineas[i-1])
            i=0
            rango = len(lineas)
       
        if lineas[i] == "/":
            lineas[i] = int(lineas[i-1]) / int(lineas[i+1])
            del(lineas[i+1])
            del(lineas[i-1])
            i=0
            rango = len(lineas)
    i+=1
            
i = 0

while i<rango:
    if '+' in lineas or '-' in lineas:
        if lineas[i]=="+" :
            lineas[i] = int(lineas[i-1]) + int(lineas[i+1])
            del(lineas[i+1])
            del(lineas[i-1])
            i=0
            rango = len(lineas)-1
       
        if lineas[i] == "-":
            lineas[i] = int(lineas[i-1]) - int(lineas[i+1])
            del(lineas[i+1])
            del(lineas[i-1])
            i=0
            rango = len(lineas)-1
    i+=1
            
print(lineas)