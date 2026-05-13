import sys
import random
from enum import Enum
# value = input("Please enter a value")
# print(value)

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(RPS(2))

print(RPS.ROCK)
print(RPS["PAPER"])
print(RPS.SCISSORS.value)
    

playerchoice = input("Enter ... \n1 for rock \n2 for paper \n3 for scissors")

player = int(playerchoice)


if player < 1 | player > 3:
    print("Invalid input")
    sys.exit()


computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose" + " " + str(RPS(player)).replace("RPS.2", ""))
print("The computer chose" + " " + str(RPS(computer)).replace("RPS.", ""))
print("")


if player == 1 and computer == 3:
    print("You win")
elif player == 2 and computer == 1:
    print("You win")
elif player == 3 and computer == 2: 
    print("You win")
elif player == computer:
    print("Tie game")
else:
    print("Computer won")