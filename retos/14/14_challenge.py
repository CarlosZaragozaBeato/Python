""" 
  Reto #14
  ¿ES UN NÚMERO DE ARMSTRONG?
  Fecha publicación enunciado: 04/04/22
  Fecha publicación resolución: 11/04/22
  Dificultad: FÁCIL
 
   Enunciado: Escribe una función que calcule si un número dado es un número 
   de Amstrong (o también llamado narcisista).
   Si no conoces qué es un número de Armstrong, 
   debes buscar información al respecto.
"""

numero = 407

def calcular_numero(numero):
  sum = 0
  temp = sum
  while temp>0:
    digit = temp%10
    sum+= digit **3
    temp//=10
  
  if numero == sum:
    return True
  else:
    return False
print(calcular_numero(numero))  
