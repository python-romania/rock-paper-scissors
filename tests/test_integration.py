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
    player = Player("Madalin Popa")

    # Add player choices
    player.choice = "Rock"

    game = Game(player)
    game.winner() == "Computer won!"
    print(f"Computer choice is: {game.computer_choice}")
