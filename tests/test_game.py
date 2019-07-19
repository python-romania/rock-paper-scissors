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


def test_game_instance(game_instance) -> None:
    """
    Test game instance
    """
    # Test players
    assert isinstance(game_instance.player1, Player)
    assert isinstance(game_instance.player2, Player)
    assert game_instance.player1.name == "Madalin Popa"
    assert game_instance.player2.name == "Computer"

    with pytest.raises(ValueError):
        game_instance.player1 = "A"
        game_instance.player2 = "B"
        assert "player must be an instance of Player"

    # Test game items
    assert type(Game.items) == list
    assert len(Game.items) == 22

    # Test game rounds
    assert type(game_instance.rounds) == int
    assert game_instance.rounds == 3

    with pytest.raises(ValueError) as exception:
        game_instance.rounds = "A"
        assert exception.value == "You must enter a number!"

def test_calculate(game_instance) -> None:
    """
    Test calculate
    """
    # Exception is throw is the value is not in the list
    with pytest.raises(ValueError) as exception:
        result = game_instance.calculate()
        assert exception.value == "Please entes a valid item"
    # TODO: implement test by checking the returned list

@pytest.mark.skip
def test_winner(game_instance) -> None:
    """
    Test winner
    """
    # Get next 7 items
    result = game_instance.winner()
    assert result == "Computer won the game!"
