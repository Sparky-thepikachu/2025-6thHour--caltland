#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW17

import random

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def rock_paper_scissors():
    player_call = int(input("1 for rock,2 for paper, 3 for scissors"))
    rock_paper_scissors_result = random.randint(1,3)

    if player_call == 1:
        if rock_paper_scissors_result == 1:
            print("tie!")
        elif rock_paper_scissors_result == 2:
            print("You lose!")
        elif rock_paper_scissors_result == 3:
            print("You win!")
    elif player_call == 2:
        if rock_paper_scissors_result == 1:
            print("you win!")
        elif rock_paper_scissors_result == 2:
            print("tie!")
        elif rock_paper_scissors_result == 3:
            print("You lose!")
    elif player_call == 3:
        if rock_paper_scissors_result == 1:
            print("you lose!")
        elif rock_paper_scissors_result == 2:
            print("you win!")
        elif rock_paper_scissors_result == 3:
            print("tie!")

    repeat_game()

def repeat_game():
    player_input = input("Do you want to play again? Y/N")

    if player_input == "Y" or player_input == "y":
       rock_paper_scissors()
    else:
        print("Thank you for playing!")

rock_paper_scissors()