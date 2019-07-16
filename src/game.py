"""
game.py

Contains Game class and its methods.
"""
# Local imports
from .player import Player

class Game:
    """
    Game class.
    """
    def __init__(self, player1: Player, player2: Player) -> None:
        self._player1 = player1
        self._player2 = player2

    @property
    def player1(self) -> Player:
        """
        Get player1
        """
        return self._player1

    @player1.setter
    def player1(self, value) -> None:
        """
        Set player1
        """
        if not isinstance(value, Player):
            raise ValueError("player must be an instance of Player")
        self._player1 = value

    @property
    def player2(self) -> Player:
        """
        Get player2
        """
        return self._player2

    @player2.setter
    def player2(self, value) -> None:
        """
        Set player2
        """
        if not isinstance(value, Player):
            raise ValueError("player must be an instance of Player")
        self._player2 = value

    def start(self) -> None:
        """
        Start the game
        """

    def winner(self) -> str:
        """
        Calculate the winner
        """
