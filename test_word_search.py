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

def test_get_all_horizontal_sequences_with_coords():
    puzzle = [
        ["A", "B", "C"],
        ["X", "Y", "Z"]
    ]
    ws = WordSearch(puzzle)

    # Resultado esperado
    expected_sequences = [
        ('AB', (0, 0), (0, 1)),
        ('ABC', (0, 0), (0, 2)),
        ('BC', (0, 1), (0, 2)),
        ('XY', (1, 0), (1, 1)),
        ('XYZ', (1, 0), (1, 2)),
        ('YZ', (1, 1), (1, 2)),
    ]
        # Obtenemos las secuencias generadas por la función
    sequences = ws.get_all_horizontal_sequences_with_positions(min_length=2)

    # Comprobamos que el tamaño de la lista es el esperado
    assert len(sequences) == len(expected_sequences), (
        f"Expected {len(expected_sequences)} sequences, got {len(sequences)}"
    )

    # Comprobamos que cada resultado esperado está en la lista devuelta
    for expected in expected_sequences:
        assert expected in sequences, f"Expected {expected} not found in results"

def test_get_all_vertical_sequences_with_coords():
    puzzle = [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"]
    ]
    ws = WordSearch(puzzle)

    # Resultado esperado
    expected_sequences = [
        ('AD', (0, 0), (1, 0)),
        ('DG', (1, 0), (2, 0)),
        ('ADG', (0, 0), (2, 0)),
        ('BE', (0, 1), (1, 1)),
        ('EH', (1, 1), (2, 1)),
        ('BEH', (0, 1), (2, 1)),
        ('CF', (0, 2), (1, 2)),
        ('FI', (1, 2), (2, 2)),
        ('CFI', (0, 2), (2, 2)),
    ]

    # Obtenemos las secuencias generadas por la función
    sequences = ws.get_all_vertical_sequences_with_positions(min_length=2)

    # Comprobamos que el tamaño de la lista es el esperado
    assert len(sequences) == len(expected_sequences), (
        f"Expected {len(expected_sequences)} sequences, got {len(sequences)}"
    )

    # Comprobamos que cada resultado esperado está en la lista devuelta
    for expected in expected_sequences:
        assert expected in sequences, f"Expected {expected} not found in results"

def test_get_all_diagonal_sequences_tl_br_with_coords():
    puzzle = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"],
        ["M", "N", "O", "P"]
    ]
    ws = WordSearch(puzzle)

    # Se esperan las diagonales y sus subcadenas (longitud ≥ 2),
    # junto con las coordenadas (fila,columna) de inicio y fin.
    expected_sequences = [
        # Diagonal principal: A-F-K-P
        ("AF",   (0, 0), (1, 1)),
        ("FK",   (1, 1), (2, 2)),
        ("KP",   (2, 2), (3, 3)),
        ("AFK",  (0, 0), (2, 2)),
        ("FKP",  (1, 1), (3, 3)),
        ("AFKP", (0, 0), (3, 3)),

        # Diagonal B-G-L
        ("BG",   (0, 1), (1, 2)),
        ("GL",   (1, 2), (2, 3)),
        ("BGL",  (0, 1), (2, 3)),

        # Diagonal C-H
        ("CH",   (0, 2), (1, 3)),

        # Diagonal E-J-O
        ("EJ",   (1, 0), (2, 1)),
        ("JO",   (2, 1), (3, 2)),
        ("EJO",  (1, 0), (3, 2)),

        # Diagonal I-N
        ("IN",   (2, 0), (3, 1)),
    ]

    # Obtenemos las secuencias que genera nuestra clase
    sequences = ws.get_all_diagonal_sequences_tl_br_with_positions(min_length=2)

    # Comprobamos que el número total de secuencias es el esperado
    assert len(sequences) == len(expected_sequences), (
        f"Se esperaban {len(expected_sequences)} secuencias, pero se obtuvieron {len(sequences)}"
    )

    # Verificamos que cada secuencia esperada esté realmente en los resultados
    for expected in expected_sequences:
        assert expected in sequences, f"La secuencia {expected} no está presente en los resultados."

def test_get_all_diagonal_sequences_tr_bl_with_coords():
    puzzle = [
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["I", "J", "K", "L"],
        ["M", "N", "O", "P"]
    ]
    ws = WordSearch(puzzle)

    # Esperamos estas diagonales con sus subcadenas (≥ 2) y coordenadas:
    expected_sequences = [
        # Desde (0,3) D → G → J → M => "DGJM"
        ("DG",   (0,3), (1,2)),
        ("GJ",   (1,2), (2,1)),
        ("JM",   (2,1), (3,0)),
        ("DGJ",  (0,3), (2,1)),
        ("GJM",  (1,2), (3,0)),
        ("DGJM", (0,3), (3,0)),

        # Desde (0,2) C → F → I => "CFI"
        ("CF",   (0,2), (1,1)),
        ("FI",   (1,1), (2,0)),
        ("CFI",  (0,2), (2,0)),

        # Desde (0,1) B → E => "BE"
        ("BE",   (0,1), (1,0)),

        # Desde (0,0) A => longitud 1 (no se incluyen)

        # Desde (1,3) H → K → N => "HKN"
        ("HK",   (1,3), (2,2)),
        ("KN",   (2,2), (3,1)),
        ("HKN",  (1,3), (3,1)),

        # Desde (2,3) L → O => "LO"
        ("LO",   (2,3), (3,2)),

        # Desde (3,3) P => longitud 1 (no se incluye)
    ]

    sequences = ws.get_all_diagonal_sequences_tr_bl_with_positions(min_length=2)

    # Comprobamos que el número de secuencias coincida con lo esperado
    assert len(sequences) == len(expected_sequences), (
        f"Se esperaban {len(expected_sequences)} secuencias, pero se obtuvieron {len(sequences)}"
    )

    # Comprobamos que cada secuencia esperada está efectivamente en la lista de resultados
    for expected in expected_sequences:
        assert expected in sequences, f"La secuencia {expected} no está presente en los resultados."
