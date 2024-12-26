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

def test_get_all_diagonal_sequences_tl_br_small():
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

def test_get_all_diagonal_sequences_tr_bl_small():
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

def test_get_all_diagonal_sequences_tl_br_large():
    puzzle = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"],
        ["M", "N", "O", "P"]
    ]
    ws = WordSearch(puzzle)
    sequences = ws.get_all_diagonal_sequences_tl_br(min_length=2)

    # Comprobamos las diagonales y subcadenas principales:
    # A-F-K-P => "AFKP", "AFK", "FKP", "AF", "FK", "KP"
    # B-G-L   => "BGL", "BG", "GL"
    # C-H     => "CH"
    # E-J-O   => "EJO", "EJ", "JO"
    # I-N     => "IN"

    # Aserciones
    assert "AF"   in sequences
    assert "FK"   in sequences
    assert "KP"   in sequences
    assert "AFK"  in sequences
    assert "FKP"  in sequences
    assert "AFKP" in sequences

    assert "BG"   in sequences
    assert "GL"   in sequences
    assert "BGL"  in sequences

    assert "CH"   in sequences

    assert "EJ"   in sequences
    assert "JO"   in sequences
    assert "EJO"  in sequences

    assert "IN"   in sequences

    # Comprobamos que no aparecen secuencias de longitud 1
    assert "A"    not in sequences
    assert "H"    not in sequences
    assert "M"    not in sequences

def test_get_all_diagonal_sequences_tr_bl_large():
    puzzle = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"],
        ["M", "N", "O", "P"]
    ]
    ws = WordSearch(puzzle)
    sequences = ws.get_all_diagonal_sequences_tr_bl(min_length=2)

    # Diagonales principales y sus subcadenas (≥ 2) en dirección top-right → bottom-left:
    #
    # 1) Desde (0,3) "D" → (1,2) "G" → (2,1) "J" → (3,0) "M"
    #    Diagonal completa: "DGJM"
    #    Subcadenas: "DG", "GJ", "JM", "DGJ", "GJM", "DGJM"
    #
    # 2) Desde (0,2) "C" → (1,1) "F" → (2,0) "I"
    #    Diagonal completa: "CFI"
    #    Subcadenas: "CF", "FI", "CFI"
    #
    # 3) Desde (0,1) "B" → (1,0) "E"
    #    Diagonal completa: "BE"
    #
    # 4) Desde (0,0) "A" => longitud 1, no se incluye
    #
    # 5) Desde (1,3) "H" → (2,2) "K" → (3,1) "N"
    #    Diagonal completa: "HKN"
    #    Subcadenas: "HK", "KN", "HKN"
    #
    # 6) Desde (2,3) "L" → (3,2) "O"
    #    Diagonal completa: "LO"
    #
    # 7) Desde (3,3) "P" => longitud 1, no se incluye
    #
    # Comprobamos en las aserciones todas las de longitud >= 2:

    # Diagonal D-G-J-M
    assert "DG"   in sequences
    assert "GJ"   in sequences
    assert "JM"   in sequences
    assert "DGJ"  in sequences
    assert "GJM"  in sequences
    assert "DGJM" in sequences

    # Diagonal C-F-I
    assert "CF"  in sequences
    assert "FI"  in sequences
    assert "CFI" in sequences

    # Diagonal B-E
    assert "BE" in sequences

    # Diagonal H-K-N
    assert "HK"  in sequences
    assert "KN"  in sequences
    assert "HKN" in sequences

    # Diagonal L-O
    assert "LO" in sequences

    # Comprobamos que no aparezcan secuencias de longitud 1
    assert "A" not in sequences
    assert "D" not in sequences
    assert "H" not in sequences
    assert "P" not in sequences
