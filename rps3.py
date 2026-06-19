import sys
import random
from enum import Enum

def rps(name="Player"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal  player_wins, computer_wins, name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"\n{name}, Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)
    
        print(f"\n{name}, you chose {str(RPS(player)).replace('RPS.', '').title()} .")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()} .\n")
        

        def determine_winner(player, computer):
            nonlocal player_wins, computer_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name} You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name} You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name} You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                computer_wins += 1
                return f"🐍 Python wins!, Sorry {name}👵"
            
        game_result = determine_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame {game_count} complete!")
        print(f"\n{name} has won {player_wins} game(s).")
        print(f"Python has won {computer_wins} game(s).")

        print(f"\nPlay again? {name} (Y/N)")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")
    return play_rps
# Return value is the play_rps function, which is a closure that retains access to the player_wins and computer_wins variables from the rps function, allowing it to modify and access these variables each time it is called.





if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience for Rock, Paper, Scissors"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", dest="firstname", required="True", help="The name of the perrson to play the game"
    )
  

    args = parser.parse_args()

    rock_paper_scissors = rps(args.firstname)
    rock_paper_scissors()