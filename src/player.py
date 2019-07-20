"""
player.py

Contains Player class and all the actions related.
"""

class Player:
    """
    Player class.
    It is used to identify a player.
    """
    def __init__(self, name: str) -> None:
        self._name = name
        self._choice: str = None
        self._score: int = 0

    @property
    def name(self) -> str:
        """
        Get player name
        """
        return self._name

    @name.setter
    def name(self, value) -> None:
        """
        Set player name
        """
        if type(value) != str:
            raise ValueError("You must enter a valid name")
        self._name = value

    @property
    def score(self) -> int:
        """
        Get player score
        """
        return self._score

    @score.setter
    def score(self, value) -> None:
        """
        Set player score
        """
        if type(value) != int:
            raise ValueError("You must enter a valid score")
        self._score = value

    @property
    def choice(self) -> str:
        """
        Get player choice
        """
        return self._choice

    @choice.setter
    def choice(self, value) -> str:
        """
        Set player choice
        """
        if type(value) != str:
            raise ValueError("You must enter a valid choice")
        self._choice = value
