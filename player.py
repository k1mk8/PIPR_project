class Player:
    def __init__(self, nickname, color):
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
