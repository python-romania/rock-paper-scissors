"""
test_main.py

Test main file.
"""
# Standard imports
import sys
from unittest import mock
from unittest.mock import MagicMock

# Third party imports
import pytest

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

def test_options(capfd) -> None:
    """
    Test display options.
    """
    # Display options
    main.options()

    # Capture output
    out, err = capfd.readouterr()
    line1 = "Rock      Gun       Lighting\n"
    line2 = "Devil     Dragon    Water\n"
    line3 = "Air       Paper     Sponge\n"
    line4 = "Wolf      Tree      Human\n"
    line5 = "Snake     Scissors  Fire\n"

    assert line1 in out
    assert line2 in out
    assert line3 in out
    assert line4 in out
    assert line5 in out

@mock.patch("main.input")
def test_input(fake_input: MagicMock, capfd) -> None:
    """
    Test user input
    """
    # Test ValueError exception when not a number
    with pytest.raises(ValueError) as exception:
        fake_input.return_value = "A"
        result = main.user_input(">")
    assert str(exception.value) == "You must enter a number!"

    # # Test invalid menu option

    with pytest.raises(ValueError) as exception:
        fake_input.return_value = 2
        result = main.user_input(">")
    assert str(exception.value) == "You must enter a number between 0 and 1!"

@pytest.mark.skip
@mock.patch("main.input")
def test_start(fake_input: MagicMock) -> None:
    """
    Test main function
    """
    # Test start game menu choice
    fake_input.return_value = 1
    result = main.start()
    assert result

    # Test exit game menu choice
    fake_input.return_value = 0
    result = main.start()
    assert not result
