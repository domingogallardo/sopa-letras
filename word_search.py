class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def is_valid_puzzle(self):
        if not self.puzzle:
            return False
        # Comprobar que todas las filas tengan la misma longitud
        row_length = len(self.puzzle[0])
        for row in self.puzzle:
            if len(row) != row_length:
                return False
        return True
    

    def get_all_horizontal_sequences(self, min_length=2):
        """
        Devuelve un set con todas las secuencias contiguas de longitud >= min_length
        que se encuentren en cada fila de la sopa de letras.
        """
        sequences = set()
        for row in self.puzzle:
            row_str = "".join(row)
            row_len = len(row_str)
            for start in range(row_len):
                for end in range(start + min_length, row_len + 1):
                    substring = row_str[start:end]
                    sequences.add(substring)
        return sequences