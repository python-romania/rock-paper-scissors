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

def test_player_instance(player_fixture: Player) -> None:
    """
    Test instance
    """
    assert player_fixture is not None

def test_player_score(player_fixture: Player) -> None:
    """
    Test score attribute.
    """
    assert player_fixture.score == 0

    with pytest.raises(ValueError) as exception:
        player_fixture.score = "A"
    assert str(exception.value) == "You must enter a valid score"

def test_player_name(player_fixture: Player) -> None:
    """
    Test name attribute.
    """
    assert player_fixture.name == "Madalin Popa"

    with pytest.raises(ValueError) as exception:
        player_fixture.name = 0
    assert str(exception.value) == "You must enter a valid name"

def test_player_choice(player_fixture: Player) -> None:
    """
    Test choice attribute
    """
    assert player_fixture.choice == "Rock"

    with pytest.raises(ValueError) as exception:
        player_fixture.choice = 0
    assert str(exception.value) == "You must enter a valid choice"

