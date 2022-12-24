""" 
  Reto #12
  ¿ES UN PALÍNDROMO?
  Fecha publicación enunciado: 21/03/22
  Fecha publicación resolución: 28/03/22
  Dificultad: MEDIA
 
  Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
  Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
  NO se tienen en cuenta los espacios, signos de puntuación y tildes.
  Ejemplo: Ana lleva al oso la avellana.
"""

palindromo_1 = "Sometamos o matemos"


def is_palindrome(str):
  str = str.lower().replace(" ","").replace(",","")
  i = 0
  j = len(str)-1
  
  while i<j:
    if str[i] != str[j]:
      return False 
    i += 1
    j -= 1
  return True

print(is_palindrome(palindromo_1))
  
