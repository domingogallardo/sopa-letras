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

def test_get_all_vertical_sequences():
    puzzle = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ]
    ws = WordSearch(puzzle)
    
    sequences = ws.get_all_vertical_sequences(min_length=2)
    # Columnas: "ADG", "BEH", "CFI"
    # Substrings de longitud >= 2 de la primera columna:
    # "AD", "DG", "ADG"
    assert "AD" in sequences
    assert "DG" in sequences
    assert "ADG" in sequences
    # Substrings de la segunda columna:
    # "BE", "EH", "BEH"
    assert "BE" in sequences
    assert "EH" in sequences
    assert "BEH" in sequences
    # Substrings de la tercera columna:
    # "CF", "FI", "CFI"
    assert "CF" in sequences
    assert "FI" in sequences
    assert "CFI" in sequences

    # Comprobamos que no genera secuencias de longitud 1
    assert "A" not in sequences
    assert "F" not in sequences