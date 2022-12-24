"""
  Reto #8
  DECIMAL A BINARIO
  Fecha publicación enunciado: 18/02/22
  Fecha publicación resolución: 02/03/22
  Dificultad: FÁCIL
 
  Enunciado: Crea un programa se encargue de transformar un número decimal 
  a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""
def calcular_binario(numero):
    binario = ""
    while numero != 0:
        resto = numero %2
        resultado = numero //2
        binario = f"{resto}{binario}"
        numero = resultado
    return binario
print(calcular_binario(10))
