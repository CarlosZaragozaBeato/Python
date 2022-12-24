"""
/*
 * Reto #25
 * PIEDRA, PAPEL, TIJERA
 * Fecha publicación enunciado: 20/06/22
 * Fecha publicación resolución: 27/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

lista = [("R","S"),("S","R"),("P","S")]
player_one = ""
player_two = ""
score_one = 0
score_two = 0
draw = 0



def check_win(player_one, player_two):
    if player_one == "R":
        if player_two == "P":
            return 2
        elif player_two == "S":
            return 1
        else:return 0
    elif player_one == "S":
        if player_two == "P":
            return 1
        elif player_two == "S":
            return 0
        else:return 2
    elif player_one =="P":
        if player_two == "P":
            return 0
        elif player_two == "S":
            return 2
        else:return 1


for i in lista:
    if check_win(i[0],i[1]) == 1: score_one +=1
    elif check_win(i[0], i[1]) == 2: score_two +=1 
    
if score_one>score_two: print("PLAYER ONE WINS")
elif score_two>score_one:print("PLAYER TWO WINS")
else:print("DRAW")


