from board import Board


class Interface():
    def __init__(self):
        """
        Wycztuje wysokość i szerokość planszy
        Tworzy tablice do gry
        Inicjuje początkowy wygląd
        wybiera opcje gry
        """
        width = self.read_width_of_board()
        height = self.read_height_of_board()
        self.board = Board(width, height)
        print("Początkowy wygląd planszy:")
        self.board.start_board()
        self.choose_option()

    def possible_moves(self):
        """
        zwraca maksymalna ilość ruchów
        """
        return self._possible_moves

    def read_width_of_board(self):
        """
        czyta szerokość planszy od użytkownika
        """
        dictionary = {
            1: "Podaj szerokośc planszy z zakresu od 8 do 30:\n"
        }
        width = input(dictionary[1])
        while not(width.isdigit() and (int(width) in range(8, 31))):
            width = input(dictionary[1])
        return int(width)

    def read_height_of_board(self):
        """
        czyta wysokość planszy od użytkownika
        """
        dictionary = {
            2: "Podaj wysokość planszy z zakresu od 8 do 30:\n"
        }
        height = input(dictionary[2])
        while not(height.isdigit() and (int(height) in range(8, 31))):
            height = input(dictionary[2])
        return int(height)

    def after_game(self):
        """
        pozwala wybrać opcje gry po zakończeniu rozgrywki
        """
        print("Wybierz co chcesz zrobić:\n")
        print("1 - wybór opcji gry\n")
        print("2 - zakończenie programu\n")
        option = input()
        while option.isdigit() and int(option) not in [1, 2]:
            print("Wybierz co chcesz zrobić:\n")
            print("1 - Wybór opcji gry\n")
            print("2 - Zakończenie programu\n")
            option = input()
        return int(option)

    def choose_option(self):
        """
        pozwala wybrać opcje gry
        """
        dictionary = {
            1: "Wybierz opcję gry:\n1-1VS1\n2-1VSComputer\n3-ComputerVSComputer\n"
        }
        game_option = input(dictionary[1])
        while game_option.isdigit() and int(game_option) not in [1, 2, 3]:
            game_option = input(dictionary[1])
        self._game_option = int(game_option)

    def game_option(self):
        """
        zwraca opcje gry
        """
        return self._game_option
