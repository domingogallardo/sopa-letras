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

def test_get_all_diagonal_sequences_tl_br():
    """
    Test para comprobar las diagonales en dirección
    arriba-izquierda → abajo-derecha.
    """
    puzzle = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ]
    ws = WordSearch(puzzle)
    sequences = ws.get_all_diagonal_sequences_tl_br(min_length=2)

    # Diagonales con longitud >= 2 en top-left → bottom-right:
    #   * Desde (0,0): "A", "E", "I" => "AEI" (longitud 3), y también "AE", "EI"
    #   * Desde (0,1): "B", "F" => "BF" (longitud 2)
    #   * Desde (0,2): "C" => no llega a min_length=2
    #   * Desde (1,0): "D", "H" => "DH"
    #   * Desde (2,0): "G" => tampoco llega
    # Por tanto, con longitud >= 2 tenemos: "AE", "EI", "AEI", "BF", "DH"

    assert "AE" in sequences
    assert "EI" in sequences
    assert "AEI" in sequences
    assert "BF" in sequences
    assert "DH" in sequences

    # Comprobamos que secuencias de 1 no aparezcan
    assert "A" not in sequences
    assert "C" not in sequences
    assert "G" not in sequences

def test_get_all_diagonal_sequences_tr_bl():
    """
    Test para comprobar las diagonales en dirección
    arriba-derecha → abajo-izquierda.
    """
    puzzle = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ]
    ws = WordSearch(puzzle)
    sequences = ws.get_all_diagonal_sequences_tr_bl(min_length=2)

    # Diagonales con longitud >= 2 en top-right → bottom-left:
    #
    #  * Desde (0,2): "C", "E", "G" => "CEG" y sus substrings "CE", "EG"
    #  * Desde (0,1): "B", "D" => "BD"
    #  * Desde (0,0): "A" => no llega a min_length
    #  * Desde (1,2): "F", "H" => "FH"
    #  * Desde (2,2): "I" => no llega
    #
    # Por tanto, con longitud >= 2 aparecen: "CE", "EG", "CEG", "BD", "FH"

    assert "CE" in sequences
    assert "EG" in sequences
    assert "CEG" in sequences
    assert "BD" in sequences
    assert "FH" in sequences

    # Comprobamos que secuencias de 1 no aparezcan
    assert "C" not in sequences
    assert "I" not in sequences
    assert "A" not in sequences