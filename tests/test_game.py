"""
test_game.py

Test game module along with Game class.
"""
# Third party imports
import pytest

# Local imports
from src.game import Game
from src.player import Player

@pytest.fixture
def game_instance() -> Game:
    """
    Game setup
    """
    # Define players
    player1 = Player("Madalin Popa")
    player2 = Player("Computer")

    # Create a game instance
    game = Game(player1, player2)

    return game


def test_game_instance(game_instance: Game) -> None:
    """
    Test game instance
    """
    assert game_instance is not None

def test_game_items() -> None:
    """
    Test game items list
    """
    assert type(Game.items) == list
    assert len(Game.items) == 22

def test_game_rounds(game_instance: Game) -> None:
    """
    Test game rounds attribute
    """
    assert type(game_instance.rounds) == int
    assert game_instance.rounds == 3

    with pytest.raises(ValueError) as exception:
        game_instance.rounds = "A"
    assert str(exception.value) == "You must enter a number!"

def test_calculate(game_instance: Game) -> None:
    """
    Test calculate
    """
    # Exception is throw is the value is not in the list
    with pytest.raises(ValueError) as exception:
        result = game_instance.calculate()
    assert str(exception.value) == "Please enter a valid item!"

@pytest.mark.skip
def test_winner(game_instance: Game) -> None:
    """
    Test winner
    """
    # Get next 7 items
    result = game_instance.winner()
    assert result == "Computer won the game!"
