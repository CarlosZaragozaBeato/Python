"""
  Reto #20
  PARANDO EL TIEMPO
  Fecha publicación enunciado: 16/05/22
  Fecha publicación resolución: 23/05/22
  Dificultad: MEDIA
 
  Enunciado: Crea una función que sume 2 números y retorne su resultado pasados 
  unos segundos.
  - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar
  en finalizar su ejecución.
  - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, 
  es decir, sin detener la ejecución del programa principal. Se podría 
  ejecutar varias veces al mismo tiempo.
"""

import time

def parando_tiempo(valor1, valor2):
  print("Comienza el programa")
  resultado = valor1  + valor2
  print("Esperando al programa")
  time.sleep(2)
  print("Termina el programa")
  return resultado

print(parando_tiempo(10,5))
print(parando_tiempo(10,5))
print(parando_tiempo(10,5))
