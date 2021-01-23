from interface import Interface
from player import Player
from computer import Computer


class Game():
    def __init__(self):
        """
        Wywyoływanie gry
        Tworzenie interfejsu
        Wybór opcji gry
        """
        self._interface = Interface()
        self._game_option = self.interface().game_option()
        self.game_option()

    def player1(self):
        """
        zwraca pierwszego gracza
        """
        return self._player1

    def player2(self):
        """
        zwraca drugiego gracza
        """
        return self._player2

    def computer1(self):
        """
        zwraca pierwszege gracza komputerowego
        """
        return self._computer1

    def computer2(self):
        """
        zwraca drugiego gracza komputerowego
        """
        return self._computer2

    def interface(self):
        """
        zwraca interface w celu wywołania określonej na nim funkcji
        """
        return self._interface

    def game_option(self):
        """
        pozwala wybrać opcję gry
        wywołuje odpowiednią funkcję do przeprowadzania rozgrywki
        """
        game_option = self._game_option
        if game_option == 1:
            self.oneVSone()
        elif game_option == 2:
            self.oneVSComputer()
        elif game_option == 3:
            self.ComputerVSComputer()

    def oneVSone(self):
        """
        obsługująca grę gracza z graczem
        """
        self._player1 = Player("Black")
        self._player2 = Player("White")
        possible_moves = self.interface().board.total_points()
        self.play_game(self.player1(), self.player2(), possible_moves)
        self.who_win(self.player1(), self.player2())
        mode = self.interface().after_game()
        if mode == 1:
            Game()
        elif mode == 2:
            pass

    def oneVSComputer(self):
        """
        obsługująca grę gracza z komputerem
        """
        self._player1 = Player("Black")
        self._computer1 = Computer("White")
        possible_moves = self.interface().board.total_points()
        self.play_game(self.player1(), self.computer1(), possible_moves)
        self.who_win(self.player1(), self.computer1())
        mode = self.interface().after_game()
        if mode == 1:
            Game()
        elif mode == 2:
            pass

    def ComputerVSComputer(self):
        """
        obsługująca grę komputera z komputerem
        """
        self._computer1 = Computer("Black")
        self._computer2 = Computer("White")
        possible_moves = self.interface().board.total_points()
        self.play_game(self.computer1(), self.computer2(), possible_moves)
        self.who_win(self.computer1(), self.computer2())
        mode = self.interface().after_game()
        if mode == 1:
            Game()
        elif mode == 2:
            pass

    def who_win(self, player1, player2):
        """
        sprawdzająca zwycięzce rozgrywki
        """
        if player1.points() > player2.points():
            print(f"Gratulacje! Wygrał gracz: {player1.name()}")
        elif player1.points() < player2.points():
            print(f"Gratulacje! Wygrał gracz: {player2.name()}")
        elif player1.points() == player2.points():
            print("Remis!")

    def play_game(self, player1, player2, possible_moves):
        """
        przeprowadzająca rozgrywkę
        """
        while ((player1.points() + player2.points()) < possible_moves) and (player1.points() != 0) and (player2.points() != 0):
            player1.move_on_board(self.interface().board.table_board)
            player2.count_points(self.interface().board.table_board)
            self.interface().board.draw_board()
            player2.move_on_board(self.interface().board.table_board)
            player1.count_points(self.interface().board.table_board)
            self.interface().board.draw_board()


if __name__ == "__main__":
    Game()
