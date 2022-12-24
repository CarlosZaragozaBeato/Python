"""
  Reto #13
  FACTORIAL RECURSIVO
  Fecha publicación enunciado: 28/03/22
  Fecha publicación resolución: 04/04/22
  Dificultad: FÁCIL
  
  Enunciado: Escribe una función que calcule y retorne 
  el factorial de un número dado de forma recursiva.
"""

valor = 10

def factorial_recursivo(valor):
  if valor == 0:
    return 1
  if valor == 1:
    return 1
  return valor*factorial_recursivo(valor-1)

print(factorial_recursivo(valor))