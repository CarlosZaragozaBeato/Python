import numpy as np
"""
  Reto #18
  TRES EN RAYA
  Fecha publicación enunciado: 02/05/22
  Fecha publicación resolución: 09/05/22
  Dificultad: DIFÍCIL
 
  Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
  - "X" si han ganado las "X"
  - "O" si han ganado los "O"
  - "Empate" si ha habido un empate
  - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
  Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
 """
tablero = np.array([["O","0","O"],["O","0","O"],["O","O","O"]])



def comprobar_tablero(tablero):
  if tablero[0,0] == "X" and tablero[0,1] == "X" and tablero[0,2] == "X":
     return "GANAN LAS X"
  elif tablero[0,0] == "X" and tablero[1,0] == "X" and tablero[2,0] == "X":
     return "GANAN LAS X"
  elif tablero[0,0] == "X" and tablero[1,1] == "X" and tablero[2,2] == "X":
     return "GANAN LAS X"
  elif tablero[0,2] == "X" and tablero[1,2] == "X" and tablero[2,2] == "X":
     return "GANAN LAS X"
  elif tablero[0,2] == "X" and tablero[1,2] == "X" and tablero[2,0] == "X":
     return "GANAN LAS X"
  elif tablero[1,0] == "X" and tablero[1,1] == "X" and tablero[1,2] == "X":
     return "GANAN LAS X"
  elif tablero[2,0] == "X" and tablero[2,1] == "X" and tablero[2,2] == "X":
     return "GANAN LAS X"
  
  if tablero[0,0] == "O" and tablero[0,1] == "O" and tablero[0,2] == "O":
     return "GANAN LAS O"
  elif tablero[0,0] == "O" and tablero[1,0] == "O" and tablero[2,0] == "O":
     return "GANAN LAS O"
  elif tablero[0,0] == "O" and tablero[1,1] == "O" and tablero[2,2] == "O":
     return "GANAN LAS O"
  elif tablero[0,2] == "O" and tablero[1,2] == "O" and tablero[2,2] == "O":
     return "GANAN LAS O"
  elif tablero[0,2] == "O" and tablero[1,2] == "O" and tablero[2,0] == "O":
     return "GANAN LAS O"
  elif tablero[1,0] == "O" and tablero[1,1] == "O" and tablero[1,2] == "O":
     return "GANAN LAS O"
  elif tablero[2,0] == "O" and tablero[2,1] == "O" and tablero[2,2] == "O":
     return "GANAN LAS O"
  return "EMPATE"
  
  

print(comprobar_tablero(tablero)) 
 
 