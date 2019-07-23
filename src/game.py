"""
game.py

Contains Game class and its methods.
"""
# Standard imports
from typing import List
import random

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

    def __init__(self, player: Player, rounds=3) -> None:
        self._player = player
        self._rounds = rounds
        self._computer_choice = ""
        self._computer_score = 0

    @property
    def player(self) -> Player:
        """
        Get player
        """
        return self._player

    @player.setter
    def player(self, value) -> None:
        """
        Set player
        """
        if not isinstance(value, Player):
            raise ValueError("player must be an instance of Player")
        self._player = value

    @property
    def computer_choice(self) -> str:
        """
        Returns computer choice.
        """
        self._computer_choice = random.choice(Game.items)
        return self._computer_choice

    @property
    def computer_score(self) -> int:
        """
        Returns compyter score.
        """
        return self._computer_score

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
        if not self.player.choice or self.player.choice not in Game.items:
            raise ValueError("Please enter a valid item!")

        player_index = Game.items.index(self.player.choice)

        return Game.items[player_index + 1: player_index + 8]

    def winner(self) -> str:
        """
        Calculate the winner
        """
        items = self._calculate()
        if self.computer_choice == self.player.choice:
            return "Nobody won. It is a draw!"
        elif self.computer_choice in self._calculate():
            self._computer_score += 1
            return f"Computer won!"
        else:
            self.player.score += 1
            return f"{self.player.name} won!"

    @staticmethod
    def menu_input(prompt: str) -> int:
        """
        Returns menu option input.
        """
        option = input(prompt)
        if type(option) == str and not option.isdigit():
            raise ValueError("Please enter a number!")

        option_int = int(option)

        if option_int < 0 or option_int > 2:
            raise ValueError("Please enter a number between 0 and 1!")
        return option_int


