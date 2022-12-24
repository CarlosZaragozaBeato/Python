"""
  Reto #17
  LA CARRERA DE OBSTÁCULOS
  Fecha publicación enunciado: 25/04/22
  Fecha publicación resolución: 02/05/22
  Dificultad: MEDIA
 
  Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamenteuna
  carrera de obstáculos.
  - La función recibirá dos parámetros:
       - Un array que sólo puede contener String con las palabras "run" o "jump"
       - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
  - La función imprimirá cómo ha finalizado la carrera:
       - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
         variará el símbolo de esa parte de la pista.
       - Si hace "jump" en "_" (suelo), se variará la pista por "x".
       - Si hace "run" en "|" (valla), se variará la pista por "/".
  - La función retornará un Boolean que indique si ha superado la carrera.
  Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

accion = "run"
pista = "suelo"

def carrera_obstaculos(accion, pista):
  if accion == "run" and pista == "suelo":
    return True
  elif accion == "run" and pista =="valla":
    return False
  elif accion =="jump" and pista == "valla":
    return True
  elif accion == "jump" and pista == "suelo":
    return False
  else:
    return "Introduce las variables correctas"

print(carrera_obstaculos(accion=accion, pista=pista))
