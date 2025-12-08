import pytest
from main import winner

def test_draw_cases():
    assert winner("rock", "rock") == "draw"
    assert winner("paper", "paper") == "draw"
    assert winner("scissors", "scissors") == "draw"

def test_player_wins():
    assert winner("rock", "scissors") == "player"
    assert winner("paper", "rock") == "player"
    assert winner("scissors", "paper") == "player"

def test_computer_wins():
    assert winner("rock", "paper") == "computer"
    assert winner("paper", "scissors") == "computer"
    assert winner("scissors", "rock") == "computer"

def test_invalid_input():
    with pytest.raises(KeyError):
        winner("stone", "rock")
