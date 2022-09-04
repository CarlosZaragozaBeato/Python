import random

def number_guessing_game():
    number = random.randint(0,100)
    option = -1
    while(number != option):
        option = int(input("Enter a number"))
        if number > option:
            print("Enter a higher number")
        elif number < option:
            print("Enter a lower number")
        else: 
            print("The number is correct") 

number_guessing_game() 
    