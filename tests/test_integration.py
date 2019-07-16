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
    player1 = Player("Madalin Popa")
    player2 = Player("Computer")

    game = Game(player1, player2)
    game.start()
    game.winner()


