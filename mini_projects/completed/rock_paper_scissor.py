import random

def game():
    print("1. Rock")
    print("2. Papper")
    print("3. Scissors")
    print("")
    player = int(input("Enter one number: "))
    print("")
    computer = random.randint(1,3)
    print(game_logic(computer, player))

def game_logic(computer:int,player:int):
    if(player == 0 or player > 3):
        return "Enter a valid number please."
    else:
        if player == 1 and computer ==1:
            return "DRAW"
        elif player == 1 and computer ==2:
            return "Computer Wins"
        elif player == 1 and computer ==3:
            return "Player Wins"
        elif player == 2 and computer ==1:
            return "Player Wins"
        elif player == 2 and computer ==2:
            return "DRAW"
        elif player == 2 and computer ==3:
            return "Computer Wins"
        elif player == 3 and computer ==1:
            return "Computer Wins"
        elif player == 3 and computer ==2:
            return "Player Wins"
        elif player == 3 and computer ==3:
            return "Draw"
    
game()