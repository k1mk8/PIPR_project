from interface import Interface
from player import Player
from computer import Computer


class Game():
    def __init__(self):
        self._interface = Interface()
        self._game_option = self._interface.game_option()
        self.game_option()

    def player1(self):
        return self._player1

    def player2(self):
        return self._player2

    def computer1(self):
        return self._computer1

    def computer2(self):
        return self._computer2

    def interface(self):
        return self._interface

    def game_option(self):
        game_option = self._game_option
        if game_option == "1VS1":
            self.oneVSone()
        elif game_option == "1VSComputer":
            self.oneVSComputer()
        elif game_option == "ComputerVSComputer":
            self.ComputerVSComputer()

    def oneVSone(self):
        self._player1 = Player("Black")
        self._player2 = Player("White")
        possible_moves = self.interface().board.possible_moves()
        total_points = self.player1().points() + self.player2().points()
        while total_points < possible_moves or self.player1.points() == 0 or self.player2.points() == 0:
            self.player1().move_on_board(self.interface().board.table_board)
            self.player2().count_points(self.interface().board.table_board)
            self.interface().board.draw_board()
            self.player2().move_on_board(self.interface().board.table_board)
            self.player1().count_points(self.interface().board.table_board)
            self.interface().board.draw_board()
        if self.player1.points() > self.player2.points():
            print(f"Gratulacje! Wygrał gracz: {self.player1.name()}")
        elif self.player1.points() < self.player2.points():
            print(f"Gratulacje! Wygrał gracz: {self.player2.name()}")
        elif self.player1.points() == self.player2.points():
            print("Remis!")
        self.interface().after_game()

    def oneVSComputer(self):
        self._player1 = Player("Black")
        self._computer1 = Computer("White")
        if self.player1.points() > self.computer1.points():
            print(f"Gratulacje! Wygrał gracz: {self.player1.name()}")
        elif self.player1.points() < self.computer1.points():
            print(f"Gratulacje! Wygrał gracz: {self.computer1.name()}")
        elif self.player1.points() == self.computer1.points():
            print("Remis!")
        self.interface().after_game()

    def ComputerVsComputer(self):
        self._computer1 = Computer("Black")
        self._computer2 = Computer("White")
        pass


if __name__ == "__main__":
    Game()
