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

    def oneVSComputer(self):
        self._player1 = Player("Black")
        self._computer1 = Computer("White")
        pass

    def ComputerVsComputer(self):
        self._computer1 = Computer("Black")
        self._computer2 = Computer("White")
        pass


if __name__ == "__main__":
    Game()
