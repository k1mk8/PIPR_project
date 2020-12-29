class Interface():
    def __init__(self):
        self._width_of_board = self.read_width_of_board()
        self._height_of_board = self.read_height_of_board()
        height = self.height_of_board()
        width = self.width_of_board()
        table = [['0'] * width for _ in range(height)]
        self.table_board = table
        self.initial_layout()
        print("Początkowy wygląd planszy:")
        self.draw_board()
        self.choose_option()

    def read_width_of_board(self):
        dictionary = {
            1: "Podaj szerokośc planszy z zakresu od 8 do 30:\n"
        }
        width_of_board = input(dictionary[1])
        while int(width_of_board) not in range(8, 31):
            width_of_board = input(dictionary[1])
        return int(width_of_board)

    def read_height_of_board(self):
        dictionary = {
            2: "Podaj wysokość planszy z zakresu od 8 do 30:\n"
        }
        height_of_board = input(dictionary[2])
        while int(height_of_board) not in range(8, 31):
            height_of_board = input(dictionary[2])
        return int(height_of_board)

    def width_of_board(self):
        return self._width_of_board

    def height_of_board(self):
        return self._height_of_board

    def initial_layout(self):
        height = self.height_of_board()//2 - 1
        width = self.width_of_board()//2 - 1
        self.table_board[height][width] = 'B'
        self.table_board[height][width + 1] = 'C'
        self.table_board[height + 1][width] = 'C'
        self.table_board[height + 1][width + 1] = 'B'

    def draw_board(self):
        for i in range(self.height_of_board()):
            print(self.table_board[i])

    def choose_option(self):
        dictionary = {
            1: "Wybierz opcję gry:\n1VS1\n1VSComputer\nComputerVSComputer\n"
        }
        game_option = input(dictionary[1])
        while game_option not in ["1VS1", "1VSComputer", "ComputerVSComputer"]:
            game_option = input(dictionary[1])
        self._game_option = game_option

    def game_option(self):
        return self._game_option
