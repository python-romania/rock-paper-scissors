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

def user_input(prompt: str) -> int:
    """
    Menu choices
    """
    menu_input = int(input(prompt))
    if menu_input >= 2 or menu_input < 0:
        raise ValueError
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
            menu_choice = user_input(">>")
        except ValueError as e:
            print("You must enter a number between 0 and 1!")
        if menu_choice == 1:
            return True
        elif menu_choice == 0:
            exit = True
            return False


if __name__ == "__main__":
    start()
