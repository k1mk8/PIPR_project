from board import Board


class Interface():
    def __init__(self):
        width = self.read_width_of_board()
        height = self.read_height_of_board()
        self.board = Board(width, height)
        print("Początkowy wygląd planszy:")
        self.board.start_board()
        self.choose_option()

    def possible_moves(self):
        return self._possible_moves

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
