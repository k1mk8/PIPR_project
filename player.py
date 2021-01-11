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
            self.inrow(table, row, column, self.color())
            self.incolumn(table, row, column, self.color())
            self.diagonally(table, row, column, self.color())
            self.count_points(table, row, column)

    def letter(self, name=""):
        if name == "Black":
            letter = "C "
        elif name == "White":
            letter = "B "
        return letter

    def inrow(self, table, row, column, name=""):
        letter = self.letter(name)
        table[int(row)][int(column)] = letter
        a = int(row)
        b = int(column) + 1
        while table[a][b] != f'{letter}' and b < len(table[0]):
            if table[a][b] == "0 ":
                b = int(column) + 1
                break
            b += 1
        for i in range(int(column), b):
            table[a][i] = f'{letter}'
        a = int(row)
        b = int(column) - 1
        while table[a][b] != f'{letter}' and b > 0:
            if table[a][b] == "0 ":
                b = int(column) - 1
                break
            b -= 1
        b += 1
        for i in range(b, int(column)):
            table[a][i] = f'{letter}'

    def incolumn(self, table, row, column, name=""):
        letter = self.letter(name)
        a = int(row) + 1
        b = int(column)
        while table[a][b] != f'{letter}' and a < len(table):
            if table[a][b] == "0 ":
                a = int(row) + 1
                break
            a += 1
        for i in range(int(row), a):
            table[i][b] = f'{letter}'
        a = int(row) - 1
        b = int(column)
        while table[a][b] != f'{letter}' and a > 0:
            if table[a][b] == "0 ":
                a = int(row) - 1
                break
            a -= 1
        a += 1
        for i in range(a, int(row)):
            table[i][b] = f'{letter}'

    def diagonally(self, table, row, column, name=""):
        letter = self.letter(name)
        a = int(row) - 1
        b = int(column) - 1
        while table[a][b] != f'{letter}' and a > 0 and b > 0:
            if table[a][b] == "0 ":
                a = int(row) - 1
                b = int(row) - 1
                break
            a -= 1
            b -= 1
        a += 1
        b += 1
        for i in range(a, int(row)):
            table[i][b] = f'{letter}'
            b += 1
        a = int(row) - 1
        b = int(column) + 1
        while table[a][b] != f'{letter}' and a > 0 and b < len(table[0]):
            if table[a][b] == "0 ":
                a = int(row) - 1
                b = int(column) + 1
                break
            a -= 1
            b += 1
        a += 1
        b -= 1
        for i in range(a, int(row)):
            table[i][b] = f'{letter}'
            b -= 1
        a = int(row) - 1
        b = int(column) - 1
        while table[a][b] != f'{letter}' and a < len(table) and b < len(table[0]):
            if table[a][b] == "0 ":
                a = int(row) - 1
                b = int(column) - 1
                break
            a += 1
            b += 1
        a -= 1
        b -= 1
        for i in range(int(row), a):
            table[i][b] = f'{letter}'
            b += 1
        a = int(row) + 1
        b = int(column) - 1
        while table[a][b] != f'{letter}' and a < len(table) and b > 0:
            if table[a][b] == "0 ":
                a = int(row) + 1
                b = int(column) - 1
                break
            a += 1
            b -= 1
        a -= 1
        b += 1
        for i in range((int(row) + 1), (a + 1)):
            table[i][b] = f'{letter}'
            b += 1

    def count_points(self, table, row=0, column=0):
        letter = self.letter(self.color())
        number_of_appearances = 0
        for i in range(1, (len(table))):
            for j in range(1, (len(table[0]))):
                if table[i][j] == letter:
                    number_of_appearances += 1
        if number_of_appearances > self.points() + 1:
            self.set_points(number_of_appearances)
        else:
            if int(row) == 0 and int(column) == 0:
                self.set_points(number_of_appearances)
                pass
            else:
                print("Nieprawidłowy ruch! Proszę podać inne pola.")
                table[int(row)][int(column)] = "0 "
                self.move_on_board(table)
