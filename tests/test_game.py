"""
test_game.py

Test game module along with Game class.
"""
# Standard imports
from importlib import reload
from unittest import mock
from importlib import reload
from unittest.mock import MagicMock

# Third party imports
import pytest

# Local imports
from src import game
from src import player

@pytest.fixture
def game_instance() -> game.Game:
    """
    Game setup
    """
    # Define player
    human_player = player.Player("Madalin Popa")

    # Create a game instance
    game_instance = game.Game(human_player)

    return game_instance

def test_game_instance(game_instance: game.Game) -> None:
    """
    Test game instance
    """
    assert game_instance is not None

def test_game_items() -> None:
    """
    Test game items list
    """
    assert type(game.Game.items) == list
    assert len(game.Game.items) == 23

def test_game_rounds(game_instance: game.Game) -> None:
    """
    Test game rounds attribute
    """
    assert type(game_instance.rounds) == int
    assert game_instance.rounds == 3

    with pytest.raises(ValueError) as exception:
        game_instance.rounds = "A"
    assert str(exception.value) == "You must enter a number!"

    with pytest.raises(ValueError) as exception:
        game_instance.rounds = "101"
    expected = "You must enter a number between 1-100!"
    assert str(exception.value) == expected

    game_instance.rounds = 5
    assert game_instance.rounds == 5

def test_computer_choice(game_instance: game.Game) -> None:
    """
    Test computer choice.
    """
    with mock.patch("random.choice", lambda seq: seq[0]):
        reload(game)
        human = player.Player("Madalin")
        new_game = game.Game(human)
        assert new_game.computer_choice == "Gun"
    reload(game)

def test_calculate(game_instance: game.Game) -> None:
    """
    Test calculate
    """
    # Exception is throw is the value is not in the list
    with pytest.raises(ValueError) as exception:
        result = game_instance._calculate()
    assert str(exception.value) == "Please enter a valid item!"

    # Value is in the list, returns next 7
    game_instance.player.choice = "Gun"
    result = game_instance._calculate()
    assert type(result) == list
    assert len(result) == 7
    expected = ['Lighting', 'Devil', 'Dragon', 'Water', 'Air', 'Paper', 'Sponge']
    assert result == expected

def test_winner(game_instance: game.Game) -> None:
    """
    Test the final winner.
    """
    # Round 1
    with mock.patch("random.choice", lambda seq: "Paper"):
        # Reload game module
        reload(game)

        # Instantiate a new player and game
        human = player.Player("Madalin")
        new_game = game.Game(human)

        new_game.player.choice = "Rock"
        computer_choice = new_game.computer_choice
        result = new_game.winner()
        assert result == "Computer won!"
    reload(game)

    # Round 2
    with mock.patch("random.choice", lambda seq: "Human"):
        # Reload game module
        reload(game)

        # Instantiate a new player and game
        human = player.Player("Madalin")
        new_game = game.Game(human)

        new_game.player.choice = "Human"
        computer_choice = new_game.computer_choice
        result = new_game.winner()
        assert result == "Nobody won. It is a draw!"
    reload(game)

    # Round 3
    with mock.patch("random.choice", lambda seq: "Tree"):
        # Reload game module
        reload(game)

        # Instantiate a new player and game
        human = player.Player("Madalin")
        new_game = game.Game(human)

        new_game.player.choice = "Human"
        computer_choice = new_game.computer_choice
        result = new_game.winner()
        assert result == "Madalin won!"
        # Final Score
        assert new_game.player.score > new_game.computer_score
    reload(game)

@mock.patch("src.game.input")
def test_menu_input(fake_input) -> None:
    """
    Test menu input.
    """
    # Test not a number
    with pytest.raises(ValueError) as exception:
        fake_input.return_value = "A"
        result = game.Game.menu_input(">> ")
    assert str(exception.value) == "Please enter a number!"

    # Test invalid option
    with pytest.raises(ValueError) as exception:
        fake_input.return_value = "3"
        result = game.Game.menu_input(">> ")
    expected = "Please enter a number between 0 and 1!"
    assert str(exception.value) == expected
