"""
test_integration.py

Test all the game.
"""
# Local imports
from src.game import Game
from src.player import Player

def test_game():
    """
    Test the entire game
    """
    # Create player instances
    player1 = Player("Madalin Popa")
    player2 = Player("Computer")

    # Add player choices
    player1.choice = "Rock"
    player2.choice = "Gun"

    game = Game(player1, player2)
    game.start()
    assert game.winner() == "Computer won!"


