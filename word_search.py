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
    
# --- NUEVO MÉTODO ---
    def get_all_vertical_sequences(self, min_length=2):
        """
        Devuelve un set con todas las secuencias contiguas de longitud >= min_length
        que se encuentren en cada columna de la sopa de letras.
        """
        sequences = set()
        if not self.is_valid_puzzle():
            return sequences

        # Cantidad de filas y columnas
        rows = len(self.puzzle)
        cols = len(self.puzzle[0])

        # Por cada columna, construimos un string vertical
        for col in range(cols):
            col_string = []
            for row in range(rows):
                col_string.append(self.puzzle[row][col])
            col_string = "".join(col_string)

            # Para cada columna (vista como string), calculamos substrings
            col_len = len(col_string)
            for start in range(col_len):
                for end in range(start + min_length, col_len + 1):
                    substring = col_string[start:end]
                    sequences.add(substring)
        return sequences
    
    def get_all_diagonal_sequences_tl_br(self, min_length=2):
        """
        Obtiene todas las secuencias diagonales (contiguas) en la dirección
        arriba-izquierda → abajo-derecha, con longitud >= min_length.
        """
        sequences = set()
        if not self.is_valid_puzzle():
            return sequences

        rows = len(self.puzzle)
        cols = len(self.puzzle[0])

        # Función para recoger la diagonal comenzando en (r, c)
        def diagonal_from(r, c):
            diagonal_chars = []
            row, col = r, c
            while row < rows and col < cols:
                diagonal_chars.append(self.puzzle[row][col])
                row += 1
                col += 1
            return "".join(diagonal_chars)

        # Recorremos la primera fila y la primera columna
        # para extraer todas las diagonales posibles en esta dirección.
        for start_col in range(cols):
            diag_str = diagonal_from(0, start_col)
            for start in range(len(diag_str)):
                for end in range(start + min_length, len(diag_str) + 1):
                    sequences.add(diag_str[start:end])

        for start_row in range(1, rows):  # Empezamos en 1 para no repetir la diagonal [0,0]
            diag_str = diagonal_from(start_row, 0)
            for start in range(len(diag_str)):
                for end in range(start + min_length, len(diag_str) + 1):
                    sequences.add(diag_str[start:end])

        return sequences
    
    # --- NUEVO MÉTODO ---
    def get_all_diagonal_sequences_tr_bl(self, min_length=2):
        """
        Obtiene todas las secuencias diagonales (contiguas) en la dirección 
        arriba-derecha → abajo-izquierda, con longitud >= min_length.
        """
        sequences = set()
        if not self.is_valid_puzzle():
            return sequences

        rows = len(self.puzzle)
        cols = len(self.puzzle[0])

        # Función para recoger la diagonal comenzando en (r, c)
        def diagonal_from(r, c):
            diagonal_chars = []
            row, col = r, c
            while row < rows and col >= 0:
                diagonal_chars.append(self.puzzle[row][col])
                row += 1
                col -= 1
            return "".join(diagonal_chars)

        # Recorremos la primera fila (r=0) para cada columna c
        for start_col in range(cols):
            diag_str = diagonal_from(0, start_col)
            for start in range(len(diag_str)):
                for end in range(start + min_length, len(diag_str) + 1):
                    sequences.add(diag_str[start:end])

        # Recorremos la última columna (c=cols-1) para cada fila r>0
        # (Arrancamos en r=1 para no repetir la diagonal de la esquina superior derecha)
        for start_row in range(1, rows):
            diag_str = diagonal_from(start_row, cols - 1)
            for start in range(len(diag_str)):
                for end in range(start + min_length, len(diag_str) + 1):
                    sequences.add(diag_str[start:end])

        return sequences