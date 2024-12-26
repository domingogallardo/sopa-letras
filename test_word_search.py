import pytest
from word_search import WordSearch

def test_puzzle_construction():
    puzzle = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U", "V", "W", "X", "Y"]
    ]
    ws = WordSearch(puzzle)
    assert ws.is_valid_puzzle() is True

def test_puzzle_construction_fails():
    # Aquí, la tercera fila es más corta
    puzzle = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N"],
    ]
    ws = WordSearch(puzzle)
    assert ws.is_valid_puzzle() is False