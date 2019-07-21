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
    assert len(Game.items) == 23

def test_game_rounds(game_instance: Game) -> None:
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

def test_calculate(game_instance: Game) -> None:
    """
    Test calculate
    """
    # Exception is throw is the value is not in the list
    with pytest.raises(ValueError) as exception:
        result = game_instance._calculate()
    assert str(exception.value) == "Please enter a valid item!"

    # Value is in the list, returns next 7
    game_instance.player1.choice = "Gun"
    result = game_instance._calculate()
    assert type(result) == list
    assert len(result) == 7
    expected = ['Lighting', 'Devil', 'Dragon', 'Water', 'Air', 'Paper', 'Sponge']
    assert result == expected

def test_winner(game_instance: Game) -> None:
    """
    Test the final winner.
    """
    # Round 1
    game_instance.player1.choice = "Rock"
    game_instance.player2.choice = "Paper"
    result = game_instance.winner()
    assert result == "Computer won!"

    # Round 2
    game_instance.player1.choice = "Human"
    game_instance.player2.choice = "Tree"
    result = game_instance.winner()
    assert result == "Madalin Popa won!"

    # Round 3
    game_instance.player1.choice = "Devil"
    game_instance.player2.choice = "Air"
    result = game_instance.winner()
    assert result == "Computer won!"

    # Final score
    assert game_instance.player1.score < game_instance.player2.score
