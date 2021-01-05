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

    def move_on_board(self, table):
        print(f'Teraz ruch gracza: {self.name()}, jeśli nie ma prawdiłowego ruchu wpisz dwa zera')
        row = input("Podaj numer wiersza:\n")
        column = input("Podaj numer kolumny:\n")
        if int(row) == 0 and int(column) == 0:
            pass
        else:
            if self.color() == "Black":
                self.inrow(table, row, column, "Black")
                self.incolumn(table, row, column, "Black")
                self.diagonally(table, row, column, "Black")
            elif self.color() == "White":
                self.inrow(table, row, column, "White")
                self.incolumn(table, row, column, "White")
                self.diagonally(table, row, column, "White")

    def inrow(self, table, row, column, name=""):
        if name == "Black":
            letter = "C "
        elif name == "White":
            letter = "B "
        a = int(row)
        b = int(column) + 1
        while table[a][b] != "0 " and b < len(table):
            if table[a][b] == f'{letter}':
                break
            b += 1
        for i in range(int(column), b):
            table[a][i] = f'{letter}'
        a = int(row)
        b = int(column) - 1
        while table[a][b] != "0 " and b > 0:
            if table[a][b] == f'{letter}':
                break
            b -= 1
        for i in range(b + 1, int(column) + 1):
            table[a][i] = f'{letter}'

    def incolumn(self, table, row, column, name=""):
        if name == "Black":
            letter = "C "
        elif name == "White":
            letter = "B "
        a = int(row) + 1
        b = int(column)
        while table[a][b] != "0 " and a < len(table):
            if table[a][b] == f'{letter}':
                break
            a += 1
        for i in range(int(row), a):
            table[i][b] = f'{letter}'
        a = int(row) - 1
        b = int(column)
        while table[a][b] != "0 " and a > 0:
            if table[a][b] == f'{letter}':
                break
            a -= 1
        for i in range(a + 1, int(row) + 1):
            table[i][b] = f'{letter}'

    def diagonally(self, table, row, column, name=""):
        if name == "Black":
            letter = "C "
        elif name == "White":
            letter = "B "
        a = int(row) - 1
        b = int(column) - 1
        while table[a][b] != "0 " and a > 0 and b > 0:
            if table[a][b] == f'{letter}':
                break
            a -= 1
            b -= 1
        a += 1
        b += 1
        for i in range(a, int(column)):
            table[i][b] = f'{letter}'
            b += 1
