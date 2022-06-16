import random

print("choices:\nrock = (1)\npaper = (2)\nscissors = (3)")
print("")
print("Rules games:\nrock vs paper --> paper win!\npaper vs scissors --> scissors win!\nrock vs scissors --> rock win!")
while True:
    choices = ("rock", "paper", "scissors")
    choices = (1, 2, 3)
    player = int(input("Chose your number:"))
    computer = int(random.choice(choices))

    while player not in choices or player == computer:
        if player == computer:
            print("--your choice same as the computer--")
            player = int(input("Chose your number:"))

        else:
             print("Please select a number from the options 1 ,2 ,3")
             player = int(input("Chose your number:"))

    if player == 1 and computer == 2:
        player = "rock"
        computer = "paper"
        print("paper win, computer win!")
    elif player == 2 and computer == 1:
        print("paper win, player win!")

    elif player == 1 and computer == 3:
        player = "rock"
        computer = "scissors"
        print("rock win, player win!")
    elif player == 3 and computer == 1:
        print("rock win, computer win!")

    elif player == 2 and computer == 3:
        player = "paper"
        computer = "scissors"
        print("scissors win, computer win!")
    elif player == 3 and computer == 2:
        print("scissors win, player win!")

    rematch = input("Do you want play rematch y/n?")
    yes = "y"
    no = "n"
    while rematch != yes and rematch != no:
       print("you need to chose yes or no")
       rematch = input("Do you want play rematch y/n?")

    if rematch == yes:
        print("lets go to play")

    elif rematch == no:
        print("good bye")
        break












