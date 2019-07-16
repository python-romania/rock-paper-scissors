"""
test_main.py

Test main file.
"""
# Standard imports
import sys
from unittest import mock

# Local imports
import main

def test_header(capfd) -> None:
    """
    Test header()
    """
    # Display header
    main.header()

    # Capture prints
    out, err = capfd.readouterr()

    # Test header
    first_line = "*" * 50
    second_line = " Rock Paper Scissors - Text Game\n"
    third_line = "*" * 50
    forth_line = " /n"
    assert first_line in out
    assert second_line in out
    assert third_line in out

def test_menu(capfd) -> None:
    """
    Test menu
    """
    # Display menu
    main.menu()

    # Capture prints
    out, err = capfd.readouterr()

    # Test menu
    first_line = "Chose an option:\n"
    second_line = " \n"
    third_line = "    1. Start\n"
    forth_line = "    0. Exit\n"

    assert first_line in out
    assert second_line in out
    assert third_line in out
    assert forth_line in out


@mock.patch("main.input")
def test_start(fake_input) -> None:
    """
    Test main function
    """
    # Set a fake return value
    fake_input.return_value = "1"

    # Get the return value
    result = main.start()

    # Test start game
    assert result == True

    # Set fake return value
    fake_input.return_value = "0"

    # Get the new result
    result = main.start()

    # Test exit game
    assert result == False
