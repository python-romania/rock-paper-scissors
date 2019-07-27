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
    for lin1, lin2, lin3 in zip(line1, line2, line3):
        print(f"{lin1:<10}{lin2:<10}{lin3:<}")
    print(" ")

def menu_input(prompt: str) -> int:
    """
    Get menu option.
    """
    while True:
        try:
            option = Game.menu_input(prompt)
            return option
        except ValueError as exception:
            print(str(exception))

def user_name_input(prompt: str) -> str:
    """
    Get user name.
    """
    while True:
        try:
            player = Player("Human Player")
            player.name = input(prompt)
            return player
        except ValueError as exception:
            print(str(exception))

def rounds_input(prompt: str, game: Game) -> int:
    """
    Get rounds input.
    """
    while True:
        try:
            rounds = input(prompt)
            if len(rounds) > 0:
                game.rounds = rounds
                return game.rounds
            else:
                return game.rounds
        except ValueError as exception:
            print(str(exception))

def items_input(prompt: str) -> str:
    """
    Get item input.
    """
    while True:
        try:
            option = Player.pick_element(prompt, Game.items)
            return option
        except ValueError as exception:
            print(str(exception))

def start() -> None:
    """
    Start game
    """
    # Display header
    header()

    # Display menu
    menu()

    exit_game = False

    # Menu choice
    menu_choice = menu_input(">> ")

    while not exit_game:

        if  menu_choice == 1:
            # Display options
            options()

            # Create player
            player = user_name_input(">> Enter your name: ")

            # Start a new game
            game = Game(player)

            # How many rounds
            rounds = rounds_input(">> How many rounds? default=3: ", game)

            # Start rounds
            for game_rounds in range(rounds):
                print(f">> Round {game_rounds + 1} starts!")
                game.player.choice = items_input(">> Enter your choice: ")
                computer_choice = game.computer_choice
                print(f">> Computer chose {computer_choice}")
                print(f">> {game.winner()}")

            # Final score
            print(">> Game Over!")
            if game.player.score > game.computer_score:
                print(f">> {game.player.name} won the game!")
                print(f">> Final score: {game.player.score}:{game.computer_score}")
            elif game.player.score < game.computer_score:
                print(">> Computer won the game!")
                print(f">> Final score: {game.computer_score}:{game.player.score}")
            elif game.player.score == game.computer_score:
                print(f">> Nobody won. We have a draw!")

            # Play again?
            play_again = menu_input(">> Do you want to play again? (1.Start, 0.Exit): ")

            if play_again == 1:
                menu_choice = 1
                continue
            elif play_again == 0:
                exit_game = True
        elif menu_choice == 0:
            exit_game = True

if __name__ == "__main__":
    start()
