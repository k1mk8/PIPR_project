class Player:
    def __init__(self, color=''):
        nickname = input("Podaj nazwę gracza: ")
        self._name = nickname
        self._points = 2
        self._color = color

    def name(self):
        return self._name

    def points(self):
        return self._points

    def set_points(self, points):
        self._points = points

    def color(self):
        return self._color

    def move_on_board(self):
        print(f'Teraz ruch gracza: {self.name()}')
        row = input("Podaj numer wiersza:\n")
        column = input("Podaj numer kolumny:\n")
