# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you ant to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""

# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like randome and time packages wev'e discussed about) 
# ----------------------------------------------------------------------------------------------------------------------
import random

# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Here you write code :)
# ----------------------------------------------------------------------------------------------------------------------
"""
I'll give you the text inputs for this program, to make your lives a little easier.
In addition, and to make it simple to you, the input from the user will be an integer:
1 for ROCK
2 for PAPER
3 for SCISSORS
A text input describing the operation is unacceptable and will cost you with points.

A quick reminder of the rules:

ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
PAPER(2) vs ROCK(1)      --> PAPER(2) wins

DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
"""

# print the instructions for the user to see:
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")

# The game will run in a WHILE loop.
# The loop is infinite, and only the user has the power to stop it (when they say they don't want to play anymore)
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












