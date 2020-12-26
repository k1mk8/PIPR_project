import sys


class Interface():
    def __init__(self):
        board = input("Podaj wielkość planszy z zakresu od 8 do 30: \n")
        while int(board) not in range(8, 31):
            board = input("Podaj wielkość planszy z zakresu od 8 do 30: \n")
            if board == '^[':
                sys.exit()
        self._size_of_board = int(board)
        self.draw_board()

    def size_of_board(self):
        return self._size_of_board

    def player_1_move(self):
        self.place = input("Podaj miejsce ruchu: \n")

    def draw_board(self):
        board = self.size_of_board()
        for i in range(1, board+1):
            row = ''
            for j in range(1, board+1):
                row += "O "
            print(row)

