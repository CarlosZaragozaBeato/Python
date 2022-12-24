"""
  Reto #7
  CONTANDO PALABRAS
  Dificultad: MEDIA
 
  Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
  - Los signos de puntuación no forman parte de la palabra.
  - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
  - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""
#FORMA ITERATIVA

def contar_palabra(palabra):
  mapa = {}
  for i in palabra:
    if comprobar_palabra(i, mapa):
      value = 0
      for j in palabra:
        if i == j:
          value +=1
      mapa[i] = value
  return mapa

def comprobar_palabra(letra, mapa):
  for i in mapa.keys():
    if i == letra: return False
  return True

print(contar_palabra("AAAAAseeeeel"))

 