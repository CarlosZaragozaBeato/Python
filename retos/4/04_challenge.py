"""
  Reto #4
  ÁREA DE UN POLÍGONO
  Fecha publicación enunciado: 24/01/22
  Fecha publicación resolución: 31/01/22
  Dificultad: FÁCIL
 
  Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
  - La función recibirá por parámetro sólo UN polígono a la vez.
  - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
  - Imprime el cálculo del área de un polígono de cada tipo.
"""


#Interface
class Poligono():
  def CalcularArea():
    pass
  
  
######################Clases###################################  
class Triangulo(Poligono):
  base = 0
  altura = 0
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
    super().__init__()
    
  def CalcularArea(self):
    return self.base * self.altura  

class Cuadrado(Poligono):
  lado = 0
  def __init__ (self, lado):
    self.lado = lado
    super().__init__()
  
  def CalcularArea(self):
    return self.lado**2
    
  

class Rectangulo(Poligono):
  lado = 0
  def __init__(self, lado):
    self.lado = lado
    super().__init__()
  
  def CalcularArea(self):
    return self.lado**2

###########################################333







def ClcArea(poligono:Poligono):
  return poligono.CalcularArea()
  
triangulo = Triangulo(10,5)
cuadrado = Cuadrado(5)
rectangulo = Rectangulo(4)

print(ClcArea(cuadrado))
print(ClcArea(rectangulo))
print(ClcArea(triangulo))






 