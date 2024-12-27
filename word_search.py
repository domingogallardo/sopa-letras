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

    @staticmethod
    def meets_criteria(word):
        """
        Función auxiliar para determinar si una palabra cumple con el criterio.
        En este caso: solo contiene '1's
        """
        return word == 'SOL'

    def get_all_horizontal_sequences_with_positions(self, min_length=2):
        results = []
        for row_idx, row in enumerate(self.puzzle):
            row_str = "".join(row)
            row_len = len(row_str)
            for start_col in range(row_len):
                for end_col in range(start_col + min_length, row_len + 1):
                    substring = row_str[start_col:end_col]
                    if self.meets_criteria(substring):
                        results.append((substring, (row_idx, start_col), (row_idx, end_col - 1)))
        return results

    def get_all_vertical_sequences_with_positions(self, min_length=2):
        results = []
        if not self.is_valid_puzzle():
            return results

        rows = len(self.puzzle)
        cols = len(self.puzzle[0])

        for col in range(cols):
            col_chars = []
            positions = []
            for row in range(rows):
                col_chars.append(self.puzzle[row][col])
                positions.append((row, col))

            col_str = "".join(col_chars)
            col_len = len(col_str)

            for start in range(col_len):
                for end in range(start + min_length, col_len + 1):
                    substring = col_str[start:end]
                    if self.meets_criteria(substring):
                        start_pos = positions[start]
                        end_pos = positions[end - 1]
                        results.append((substring, start_pos, end_pos))

        return results

    def get_all_diagonal_sequences_tl_br_with_positions(self, min_length=2):
        results = []
        if not self.is_valid_puzzle():
            return results

        rows = len(self.puzzle)
        cols = len(self.puzzle[0])

        def diagonal_from(r, c):
            diagonal_chars = []
            diagonal_positions = []
            row, col = r, c
            while row < rows and col < cols:
                diagonal_chars.append(self.puzzle[row][col])
                diagonal_positions.append((row, col))
                row += 1
                col += 1
            return "".join(diagonal_chars), diagonal_positions

        for start_col in range(cols):
            diag_str, diag_positions = diagonal_from(0, start_col)
            length = len(diag_str)
            for start in range(length):
                for end in range(start + min_length, length + 1):
                    substring = diag_str[start:end]
                    if self.meets_criteria(substring):
                        start_pos = diag_positions[start]
                        end_pos = diag_positions[end - 1]
                        results.append((substring, start_pos, end_pos))

        for start_row in range(1, rows):
            diag_str, diag_positions = diagonal_from(start_row, 0)
            length = len(diag_str)
            for start in range(length):
                for end in range(start + min_length, length + 1):
                    substring = diag_str[start:end]
                    if self.meets_criteria(substring):
                        start_pos = diag_positions[start]
                        end_pos = diag_positions[end - 1]
                        results.append((substring, start_pos, end_pos))

        return results

    def get_all_diagonal_sequences_tr_bl_with_positions(self, min_length=2):
        results = []
        if not self.is_valid_puzzle():
            return results

        rows = len(self.puzzle)
        cols = len(self.puzzle[0])

        def diagonal_from(r, c):
            diagonal_chars = []
            diagonal_positions = []
            row, col = r, c
            while row < rows and col >= 0:
                diagonal_chars.append(self.puzzle[row][col])
                diagonal_positions.append((row, col))
                row += 1
                col -= 1
            return "".join(diagonal_chars), diagonal_positions

        for start_col in range(cols):
            diag_str, diag_positions = diagonal_from(0, start_col)
            length = len(diag_str)
            for start in range(length):
                for end in range(start + min_length, length + 1):
                    substring = diag_str[start:end]
                    if self.meets_criteria(substring):
                        start_pos = diag_positions[start]
                        end_pos = diag_positions[end - 1]
                        results.append((substring, start_pos, end_pos))

        for start_row in range(1, rows):
            diag_str, diag_positions = diagonal_from(start_row, cols - 1)
            length = len(diag_str)
            for start in range(length):
                for end in range(start + min_length, length + 1):
                    substring = diag_str[start:end]
                    if self.meets_criteria(substring):
                        start_pos = diag_positions[start]
                        end_pos = diag_positions[end - 1]
                        results.append((substring, start_pos, end_pos))

        return results
