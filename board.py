class Board:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.make_board()
        self._total_points = width * height

    def width(self):
        return self._width

    def height(self):
        return self._height

    def total_points(self):
        return self._total_points

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
        table[0][0] = "X "

    def draw_board(self):
        for i in range(self.height()+1):
            space = "  "
            formated_table = space.join(self.table_board[i])
            print(formated_table)

    def start_board(self):
        height = self.height()//2
        width = self.width()//2
        self.table_board[height][width] = 'Z '
        self.table_board[height][width + 1] = 'M '
        self.table_board[height + 1][width] = 'M '
        self.table_board[height + 1][width + 1] = 'Z '
        self.draw_board()
