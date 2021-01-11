class Board:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.make_board()
        self._possible_moves = width * height

    def width(self):
        return self._width

    def height(self):
        return self._height

    def possible_moves(self):
        return self._possible_moves

    def make_board(self):
        height = self.height()
        width = self.width()
        table = [['0 '] * (width + 1) for _ in range(height + 1)]
        for i in range(1, width+1):
            if i < 10:
                table[0][i] = f'{i} '
            else:
                table[0][i] = str(i)
        for i in range(1, height+1):
            if i < 10:
                table[i][0] = f'{i} '
            else:
                table[i][0] = str(i)
        self.table_board = table
        self._possible_moves = height * width - 4
        table[0][0] = "X "

    def draw_board(self):
        for i in range(self.height()+1):
            print(self.table_board[i])

    def start_board(self):
        height = self.height()//2
        width = self.width()//2
        self.table_board[height][width] = 'B '
        self.table_board[height][width + 1] = 'C '
        self.table_board[height + 1][width] = 'C '
        self.table_board[height + 1][width + 1] = 'B '
        self.draw_board()
