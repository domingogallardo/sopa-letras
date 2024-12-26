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

def test_get_all_horizontal_sequences():
    puzzle = [
        ["A", "B", "C"],
        ["X", "Y", "Z"]
    ]
    ws = WordSearch(puzzle)

    # De la primera fila ("ABC"), se esperan substrings de longitud >= 2:
    # "AB", "BC", "ABC"
    # De la segunda fila ("XYZ"), se esperan: 
    # "XY", "YZ", "XYZ"
    sequences = ws.get_all_horizontal_sequences(min_length=2)
    
    assert "AB" in sequences
    assert "BC" in sequences
    assert "ABC" in sequences
    assert "XY" in sequences
    assert "YZ" in sequences
    assert "XYZ" in sequences

    # Comprobamos que no genera secuencias de longitud 1
    assert "A" not in sequences
    assert "X" not in sequences