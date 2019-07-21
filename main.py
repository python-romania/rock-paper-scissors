"""
main.py

Display the menus and starts the program.

**************************************************
 Rock Paper Scissors - Text Game
**************************************************

Chose an option:

    1. Start
    0. Exit

>> 1

Rock         Water     Tree
Gun          Air       Human
Lighting     Paper     Snake
Devil        Sponge    Scissors
Dragon       Wolf      Fire

>> Enter your name: Madalin Popa
>> How many rounds?: 3
>> Round 1 starts!
>> Enter your choice: Rock
>> Computer choice: Paper
>> Computer won round 1!
>> Round 2 starts!
>> Enter your choice: Paper
>> Computer choice: Scissors
>> Computer won round 2!
>> Round 3 starts!
>> Enter your choice: Rock
>> Computer choice: Scissors
>> Madalin Popa won round 3!
>> Game Over!
>> Computer won the game!
>> Do you want to play again? (1.Start, 0.Exit):

"""
# Standard imports
import random

# Local imports
from src.game import Game
from src.player import Player

def header() -> None:
    """
    Print the programm header
    """
    print("*" * 50)
    print(" Rock Paper Scissors - Text Game")
    print("*" * 50)
    print(" ")

def menu() -> None:
    """
    Print the program menu
    """
    print("Chose an option:")
    print(" ")
    print("     1. Start")
    print("     0. Exit")
    print(" ")

def options() -> None:
    """
    Print the options
    """
    items = ["Rock", "Gun", "Lighting", "Devil", "Dragon",
            "Water", "Air", "Paper", "Sponge", "Wolf",
            "Tree", "Human", "Snake", "Scissors", "Fire"]

    line1 = items[0::3]
    line2 = items[1::3]
    line3 = items[2::3]

    print(" ")
    for l1, l2, l3 in zip(line1, line2, line3):
        print(f"{l1:<10}{l2:<10}{l3:<}")
    print(" ")

def user_input(prompt: str) -> int:
    """
    Menu choices
    """
    menu_input = input(prompt)

    if type(menu_input) == str and not menu_input.isdigit():
        raise ValueError("You must enter a number!")

    menu_input = int(menu_input)

    if menu_input >= 2 or menu_input < 0:
        raise ValueError("You must enter a number between 0 and 1!")
    return menu_input


def start() -> None:
    """
    Start game
    """
    # Display header
    header()

    # Display menu
    menu()

    exit = False
    while not exit:
        try:

            # Menu choice
            menu_choice = user_input(">> ")

            if  menu_choice == 1:
                # Display options
                options()

                # Create players
                player1 = Player(input(">> Enter your name: "))
                player2 = Player("Computer")

                # How many rounds
                rounds = input(">> How many rounds? default=3: ")

                # Start a new game
                game = Game(player1, player2)

                if len(rounds) > 0:
                    game.rounds = rounds

                # Start rounds
                for gr in range(game.rounds):
                    print(f">> Round {gr + 1} starts!")
                    game.player1.choice = input(">> Enter your choice: ")
                    game.player2.choice = random.choice(Game.items)
                    print(f">> Computer chose {game.player2.choice}")
                    print(f">> {game.winner()}")

                # Final score
                print(">> Game Over!")
                if game.player1.score > game.player2.score:
                    print(f">> {game.player1.name} won the game!")
                elif game.player1.score < game.player2.score:
                    print(f">> {game.player2.name} won the game!")
                elif game.player1.score == game.player2.score:
                    print(f">> Nobody won. We have a draw!")

                # Play again?
                play_again = user_input(">> Do you want to play again? (1.Start, 0.Exit): ")

                if play_again == 1:
                    menu_choice = 1
                    continue
                elif play_again == 0:
                    exit = True
            elif menu_choice == 0:
                exit = True
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    start()
