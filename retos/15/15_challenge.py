""" 
  Reto #15
  ¿CUÁNTOS DÍAS?
  Fecha publicación enunciado: 11/04/22
  Fecha publicación resolución: 18/04/22
  Dificultad: DIFÍCIL
 
  Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
  - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
  - La función recibirá dos String y retornará un Int.
  - La diferencia en días será absoluta (no importa el orden de las fechas).
  - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""
fecha_1 = "11/05/22"
fecha_2 = "11/10/21"



def calcular_meses(current_month):
  dias = 0
  if int(current_month) == 1:
    dias = 31
  elif int(current_month) == 2:
    dias = 28
  elif int(current_month) == 3:
    dias = 31  
  elif int(current_month) == 4:
    dias = 30 
  elif int(current_month) == 5:
    dias = 31  
  elif int(current_month) == 6:
    dias = 30  
  elif int(current_month) == 7:
    dias = 31  
  elif int(current_month) == 8:
    dias = 31  
  elif int(current_month) == 9:
    dias = 30  
  elif int(current_month) == 10:
    dias = 31  
  elif int(current_month) == 11:
    dias = 30  
  elif int(current_month) == 12:
    dias = 31
  else:
    dias=-1 
  return dias 
  

def calcular_fechas(fecha_1, fecha_2):
  fecha_1_trozeada = fecha_1.split("/")
  fecha_2_trozeada = fecha_2.split("/")
  fecha_menor = 0
  
  
  if fecha_1_trozeada[2] > fecha_2_trozeada[2] and fecha_1_trozeada[1] > fecha_2_trozeada[1] and fecha_1_trozeada[0] > fecha_2_trozeada[0]:
    fecha_menor = fecha_1_trozeada
  else: 
    fecha_menor = fecha_2_trozeada

  diferencia_anios = abs(int(fecha_1_trozeada[2]) - int(fecha_2_trozeada[2]))
  diferencia_dias = abs(int(fecha_1_trozeada[0]) - int(fecha_2_trozeada[0]))
  diferencias_meses =  abs(int(fecha_1_trozeada[1]) - int(fecha_2_trozeada[1]))
  diferencia_meses_dias = 0
  
  if diferencias_meses > 0:
    current_month = int(fecha_menor[1])
    while diferencias_meses >= 0:
      diferencia_meses_dias += calcular_meses(current_month)
      current_month -=1
      diferencias_meses-=1
      
  diferencia_anios_dias = diferencia_anios*365
  total_dias = diferencia_anios_dias + diferencia_meses_dias + diferencia_dias
  
  return total_dias
  
  
print(calcular_fechas(fecha_1, fecha_2))






