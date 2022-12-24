"""
 * Reto #22
 * CONJUNTOS
 * Fecha publicación enunciado: 01/06/22
 * Fecha publicación resolución: 07/06/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def conjuntos(arr_1,arr_2, condition):
    
    result = []
    
    if condition:
        for i in arr_1:
            if i in arr_2:
                result.append(i)
    else:
        for i in arr_1:
            if i not in arr_2:
                result.append(i)
        for j in arr_2:
            if j not in arr_1:
                result.append(j)
    return result

lista_1 = [1,2,3,4,5,6]
lista_2 = [1,2,11,8,9,7,10]
condition = True

print(conjuntos(lista_1, lista_2, condition))