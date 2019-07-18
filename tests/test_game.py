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

def test_start(game_instance) -> None:
    """
    Test start game
    """
    result = game_instance.start()
    assert result

