"""
test_player.py

Test the player class and its methods.
"""
# Third party imports
import pytest

# Local imports
from src.player import Player

@pytest.fixture
def player_fixture() -> Player:
    """
    Player setup
    """
    player = Player("Madalin Popa")
    player.choice = "Rock"
    return player

def test_player_instance(player_fixture) -> None:
    """
    Test instance
    """
    # Test score
    assert player_fixture.score == 0

    # Test score exception
    with pytest.raises(ValueError) as exception:
        player_fixture.score = "A"
        assert exception.value == "You must enter a valid score"

    # Test player name
    assert player_fixture.name == "Madalin Popa"

    # Test name exception
    with pytest.raises(ValueError) as exception:
        player_fixture.name = 0
        assert exception.value == "You must enter a valid name"

    # Test player choice
    assert player_fixture.choice == "Rock"

    # Test choice exception
    with pytest.raises(ValueError) as exception:
        player_fixture.choice = 0
        assert exception.value == "You must enter a valid choice"

