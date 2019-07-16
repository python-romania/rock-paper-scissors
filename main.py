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

def header() -> None:
    """
    Prints the programm header
    """
    print("*" * 50)
    print(" Rock Paper Scissors - Text Game")
    print("*" * 50)
    print(" ")

def menu() -> None:
    """
    Prints the program menu
    """
    print("Chose an option:")
    print(" ")
    print("     1. Start")
    print("     0. Exit")
    print(" ")

def start() -> None:
    """
    Start game
    """
    # Display header
    header()

    # Display menu
    menu()

    user_input = input("> ")
    if user_input == "1":
        return True
    elif user_input == "0":
        return False
