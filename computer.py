class Computer:
    def __init__(self, name, color):
        self._name = name
        self._points = 2
        self._color = color

    def name(self):
        return self._name

    def points(self):
        return self._points

    def color(self):
        return self._color

    def set_points(self, points):
        self._points = points

    def letter(self, name=""):
        if name == "Black":
            letter = "C "
        elif name == "White":
            letter = "B "
        return letter

    def move_on_board(self, table):
        pass
