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