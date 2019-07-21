"""
game.py

Contains Game class and its methods.
"""
# Standard imports
from typing import List

# Local imports
from .player import Player

class Game:
    """
    Game class.
    """
    # Items list
    items: List[str] = ['Gun', 'Lighting', 'Devil', 'Dragon',
                        'Water', 'Air', 'Paper', 'Sponge',
                        'Wolf', 'Tree', 'Human', 'Snake',
                        'Scissors', 'Fire', 'Rock', 'Gun',
                        'Lighting', 'Devil', 'Dragon', 'Water',
                        'Air', 'Paper', 'Sponge']

    def __init__(self, player1: Player, player2: Player, rounds=3) -> None:
        self._player1 = player1
        self._player2 = player2
        self._rounds = rounds

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

    @property
    def rounds(self) -> int:
        """
        Get game rounds
        """
        return self._rounds

    @rounds.setter
    def rounds(self, value) -> None:
        """
        Set rounds
        """
        if type(value) == str and not value.isdigit():
            raise ValueError("You must enter a number!")
        value = int(value)

        if value < 0 or value > 100:
            raise ValueError("You must enter a number between 1-100!")

        self._rounds = value

    def _calculate(self) -> List[str]:
        """
        Get te list with items which can beat the user.
        """
        if not self.player1.choice or self.player1.choice not in Game.items:
            raise ValueError("Please enter a valid item!")

        player1_index = Game.items.index(self.player1.choice)

        return Game.items[player1_index + 1: player1_index + 8]

    def winner(self) -> str:
        """
        Calculate the winner
        """
        items = self._calculate()
        if self.player2.choice == self.player1.choice:
            return "Nobody won. It is a draw!"
        elif self.player2.choice in items:
            self.player2.score += 1
            return f"{self.player2.name} won!"
        else:
            self.player1.score += 1
            return f"{self.player1.name} won!"
