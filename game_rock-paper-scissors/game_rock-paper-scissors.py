# Python game: Rock-Paper-Scissors
# Dec 31, 2020

from random import randint
print("Pls input Rock, Paper, or Scissors: ")
player = input()
inputValidation = 0
computer = randint(0,2)

if computer == 0:
    computer = "Rock"
if computer == 1:
    computer = "Paper"
if computer == 2:
    computer = "Scissors"

print("---")
print("You choose: " + player)
print("Computer chooses: " + computer)
print("---")

while inputValidation == 0:
    if player == computer:
        inputValidation = 1
        print("Draw")
    else:
        if player == "Rock":
            inputValidation = 1
            if computer == "Paper":
                print("Lose")
            else:
                print("Win")

        elif player == "Paper":
            inputValidation = 1
            if computer == "Rock":
                print("Win")
            else:
                print("Lose")

        elif player == "Scissors":
            inputValidation = 1
            if computer == "Rock":
                print("Lose")
            else:
                print("Win")
        
        # input validation handling
        else:
            inputValidation = 0
            print ("Opps! Invalid option! Pls input again: ")
            player = input()