"""
 *Reto #19
  CONVERSOR TIEMPO
  Fecha publicación enunciado: 09/05/22
  Fecha publicación resolución: 16/05/22
  Dificultad: FACIL
 
  Enunciado: Crea una función que reciba días, 
  horas, minutos y segundos (como enteros) y
  retorne su resultado en milisegundos.
"""

fecha = "10/5/40/1500"

def calcular_milisegundos(date):
  date = date.split("/")
  milisegundos = int(date[3]) *1000
  milisegundos += int(date[2]) *60000
  milisegundos += int(date[1]) *3600000
  milisegundos += int(date[0]) *86400000
  
  return milisegundos

print(calcular_milisegundos(fecha))
  
  
  