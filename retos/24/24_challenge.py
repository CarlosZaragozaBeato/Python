"""
/*
 * Reto #24
 * ITERATION MASTER
 * Fecha publicación enunciado: 13/06/22
 * Fecha publicación resolución: 20/06/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Quiero contar del 1 al 100 de uno en
 * uno (imprimiendo cada uno). ¿De cuántas maneras
 * eres capaz de hacerlo? Crea el código para cada una de ellas.
 *
""" 

def one():
    for i in range(1,101):
        print(i)

def two():
    i= 1
    while i < 101:
        print(i)
        i+=1

def three(i = 1):
    if i > 100:
        return 
    print(i)
    
    return three(i+1)

