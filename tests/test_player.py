"""
test_player.py

Test the player class and its methods.
"""
# Standard imports
from unittest import mock
from unittest.mock import MagicMock


# Third party imports
import pytest

# Local imports
from src import player
from src import game

@pytest.fixture
def player_fixture() -> player.Player:
    """
    Player setup
    """
    human_player = player.Player("Madalin Popa")
    human_player.choice = "Rock"
    return human_player

def test_player_instance(player_fixture: player.Player) -> None:
    """
    Test instance
    """
    assert player_fixture is not None

def test_player_score(player_fixture: player.Player) -> None:
    """
    Test score attribute.
    """
    assert player_fixture.score == 0

    with pytest.raises(ValueError) as exception:
        player_fixture.score = "A"
    assert str(exception.value) == "You must enter a valid score"

def test_player_name(player_fixture: player.Player) -> None:
    """
    Test name attribute.
    """
    assert player_fixture.name == "Madalin Popa"

    with pytest.raises(ValueError) as exception:
        player_fixture.name = 0
    assert str(exception.value) == "You must enter a valid name"

    with pytest.raises(ValueError) as exception:
        player_fixture.name = "1"
    assert str(exception.value) == "Please enter a valid name!"

def test_player_choice(player_fixture: player.Player) -> None:
    """
    Test choice attribute
    """
    assert player_fixture.choice == "Rock"

    with pytest.raises(ValueError) as exception:
        player_fixture.choice = 0
    assert str(exception.value) == "You must enter a valid choice"

@mock.patch("src.player.input")
def test_pick_element(fake_input: MagicMock) -> None:
    """
    Test pick elements
    """
    # Test invalid item
    with pytest.raises(ValueError) as exception:
        fake_input.return_value = "Test"
        result = player.Player.pick_element(">> ", game.Game.items)
        assert result == "Gun"

    fake_input.return_value = "gun"
    result = player.Player.pick_element(">> ", game.Game.items)
    assert result == "Gun"


