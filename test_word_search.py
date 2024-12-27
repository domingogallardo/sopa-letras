import pytest
from word_search import WordSearch

@pytest.fixture
def puzzle():
    return [
        ['S', 'O', 'L', '*'],
        ['S', 'S', '*', 'S'],
        ['*', 'O', 'O', '*'],
        ['*', 'L', 'L', '*']
    ]


@pytest.fixture
def big_puzzle():
    """
    Matriz 6x6 con varias secuencias 'SOL' en:
      - 5 horizontales
      - 6 verticales
      - 1 diagonal TL-BR
      - 1 diagonal TR-BL
    """
    return [
        ['S', 'O', 'L', 'S', 'O', 'S'],  # Fila 0
        ['O', 'O', 'S', 'O', 'O', 'S'],  # Fila 1
        ['L', 'S', 'L', 'L', 'S', 'O'],  # Fila 2
        ['S', 'O', 'L', 'S', 'O', 'L'],  # Fila 3
        ['O', 'L', 'S', 'O', 'L', 'S'],  # Fila 4
        ['L', 'S', 'O', 'L', 'S', 'O'],  # Fila 5
    ]

@pytest.fixture
def word_search(puzzle):
    return WordSearch(puzzle)

@pytest.fixture
def big_word_search(big_puzzle):
    return WordSearch(big_puzzle)

def test_is_valid_puzzle(word_search):
    assert word_search.is_valid_puzzle() is True

def test_horizontal_sequences(word_search):
    expected = [
        ('SOL', (0, 0), (0, 2)),
    ]
    result = word_search.get_all_horizontal_sequences_with_positions(min_length=3)
    for item in expected:
        assert item in result
    assert len(result) == len(expected)

def test_vertical_sequences(word_search):
    expected = [
        ('SOL', (1, 1), (3, 1)),
    ]
    result = word_search.get_all_vertical_sequences_with_positions(min_length=3)
    for item in expected:
        assert item in result
    assert len(result) == len(expected)

def test_diagonal_tl_br_sequences(word_search):
    expected = [
        ('SOL', (1, 0), (3, 2))
    ]
    result = word_search.get_all_diagonal_sequences_tl_br_with_positions(min_length=3)
    for item in expected:
        assert item in result
    assert len(result) == len(expected)

def test_diagonal_tr_bl_sequences(word_search):
    expected = [
        ('SOL', (1, 3), (3, 1))
    ]
    result = word_search.get_all_diagonal_sequences_tr_bl_with_positions(min_length=3)
    for item in expected:
        assert item in result
    assert len(result) == len(expected)

def test_big_horizontal_sequences(big_word_search):
    """
    Cinco apariciones horizontales de 'SOL':
      1) (0,0)->(0,2)  => S O L
      2) (3,0)->(3,2)  => S O L
      3) (3,3)->(3,5)  => S O L
      4) (4,2)->(4,4)  => S O L
      5) (5,1)->(5,3)  => S O L
    """
    result = big_word_search.get_all_horizontal_sequences_with_positions(min_length=3)
    expected = [
        ('SOL', (0, 0), (0, 2)),
        ('SOL', (3, 0), (3, 2)),
        ('SOL', (3, 3), (3, 5)),
        ('SOL', (4, 2), (4, 4)),
        ('SOL', (5, 1), (5, 3)),
    ]
    for item in expected:
        assert item in result
    assert len(result) == len(expected)

def test_big_vertical_sequences(big_word_search):
    """
    Seis apariciones verticales de 'SOL':
      1) (0,0)->(2,0) => S O L
      2) (3,0)->(5,0) => S O L
      3) (2,1)->(4,1) => S O L
      4) (0,3)->(2,3) => S O L
      5) (3,3)->(5,3) => S O L
      6) (2,4)->(4,4) => S O L
    """
    result = big_word_search.get_all_vertical_sequences_with_positions(min_length=3)
    expected = [
        ('SOL', (0, 0), (2, 0)),
        ('SOL', (3, 0), (5, 0)),
        ('SOL', (2, 1), (4, 1)),
        ('SOL', (0, 3), (2, 3)),
        ('SOL', (3, 3), (5, 3)),
        ('SOL', (2, 4), (4, 4)),
        ('SOL', (1, 5), (3, 5)),  # la séptima aparición
    ]
    for item in expected:
        assert item in result
    assert len(result) == len(expected)

def test_big_diagonal_tl_br_sequences(big_word_search):
    """
    Una aparición diagonal (arriba-izquierda a abajo-derecha).
      1) (0,0)->(2,2) => S O L
    """
    result = big_word_search.get_all_diagonal_sequences_tl_br_with_positions(min_length=3)
    expected = [
        ('SOL', (0, 0), (2, 2)),
    ]
    for item in expected:
        assert item in result
    # Puede que encuentres más si amplías la lógica a diagonales más largas,
    # pero para este ejemplo solo esperamos esta aparición.
    assert len(result) == len(expected)

def test_big_diagonal_tr_bl_sequences(big_word_search):
    """
    Una aparición diagonal (arriba-derecha a abajo-izquierda).
      1) (0,5)->(2,3) => S O L
    """
    result = big_word_search.get_all_diagonal_sequences_tr_bl_with_positions(min_length=3)
    expected = [
        ('SOL', (0, 5), (2, 3)),
    ]
    for item in expected:
        assert item in result
    assert len(result) == len(expected)