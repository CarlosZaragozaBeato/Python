"""
 Reto #3
  ¿ES UN NÚMERO PRIMO?
  Dificultad: MEDIA
 
  Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
  Hecho esto, imprime los números primos entre 1 y 100.
"""

def NumeroPrimo(value):
  for i in range(2,value):
    if value%i == 0:return False
    else: return True

for i in range(1,101):
  if  NumeroPrimo(i):
    print(f"Numero Primo es {i}")
  else: print(f"El numero {i} no es primo")