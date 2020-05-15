class Board:
    """
    Class, which represents board.
    """
    def __init__(self):
        self._field = []
        for i in range(3):
            self._field.append([])
            for j in range(3):
                self._field[i].append(" ")
        self.last_turn = tuple()
        self._filled = 0

    def draw(self):
        """
        Draws board.
        :return: None
        """
        s = []
        print(" 0 1 2")
        for i in range(3):
            s.append(str(i) + "|".join(self._field[i]))
        print("\n _ _ _\n".join(s))
        print()

    def __setitem__(self, index_tuple, value):
        """
        Sets to given value given cell on the field.
        :param index_tuple: tuple of int
        :param value: str
        :return: None
        """
        assert len(index_tuple) == 2, "Invalid number of board subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert 0 <= row < 3 and 0 <= col < 3, "Board subscript out of range."
        self._field[row][col] = value
        self.last_turn = (row, col)
        self._filled += 1

    def __getitem__(self, index_tuple):
        """
        Returns value of given cell.
        :param index_tuple: tuple of int
        :return: str
        """
        assert len(index_tuple) == 2, "Invalid number of board subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert 0 <= row < 3 and 0 <= col < 3, "Board subscript out of range."
        return self._field[row][col]

    def get_last_turn(self):
        """
        Returns row, col of the cell, which was filled last turn.
        :return: tuple
        """
        return self.last_turn[0], self.last_turn[1]

    def clear(self):
        """
        Clears the board.
        :return: None
        """
        for i in range(3):
            for j in range(3):
                self[i, j] = " "

    def finished(self):
        """
        Returns 1 if first player won, 2 - if second, 0 - if tie, -1 - game is not finished.
        :return: int
        """
        if self[0, 0] != " ":
            if self[0, 0] == self[0, 1] == self[0, 2] or self[0, 0] == self[1, 0] == self[2, 0] or\
               self[1, 1] == self[2, 2] == self[0, 0]:
                return 1 if self[0, 0] == "X" else 2
        if self[0, 1] != " ":
            if self[0, 1] == self[1, 1] == self[2, 1]:
                return 1 if self[0, 1] == "X" else 2
        if self[0, 2] != " ":
            if self[0, 2] == self[1, 2] == self[2, 2] or self[0, 2] == self[1, 1] == self[2, 0]:
                return 1 if self[0, 2] == "X" else 2
        if self[1, 0] != " ":
            if self[1, 0] == self[1, 1] == self[1, 2]:
                return 1 if self[1, 0] == "X" else 2
        if self[2, 0] != " ":
            if self[2, 0] == self[2, 1] == self[2, 2]:
                return 1 if self[2, 0] == "X" else 2
        if self._filled == 9:
            return 0
        return -1

    def get_free_cells(self):
        """
        Returns list of coordinates of  free cells.
        :return: list of tuple
        """
        free_cells = []
        for i in range(3):
            for j in range(3):
                if self[i, j] == " ":
                    free_cells.append((i, j))
        return free_cells
