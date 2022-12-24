"""
  Reto #6
  INVIRTIENDO CADENAS
  Dificultad: FÁCIL
 
  Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
  - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 
"""
 
 
 
#Hacer de forma iterativa 
def dar_la_vuelta_iterativa(palabra):
  nueva_palabra = ''
  for  i in reversed(palabra):
    nueva_palabra += i 
  return nueva_palabra

def dar_la_vuelta_iterativa_v2(palabra):
  return palabra[::-1]

#print(dar_la_vuelta_iterativa("AMOR"))
#print(dar_la_vuelta_iterativa_v2("AMOR"))
#Hacer de forma recursiva


def dar_la_vuelta_recursivamente(palabra, index = -1):
  if (len(palabra)) == abs(index):
    return palabra[index]
  return palabra[index] + dar_la_vuelta_recursivamente(palabra, index-1)
  
print(dar_la_vuelta_recursivamente("CARLOS"))
