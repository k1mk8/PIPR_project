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
        letter = self.letter(self.color())
        print(f'Teraz ruch gracza: {self.name()}, twój znak to: {letter}, jeśli nie ma prawdiłowego ruchu wpisz X')
        row, column = self.get_size((len(table) - 1), (len(table[0]) - 1))
        if row == "X":
            pass
        elif row == 0 and column == 0:
            pass
        elif table[row][column] != "0 ":
            print("Dane pole jest zajęte!")
            row, column = self.get_size((len(table)-1), (len(table[0])-1))
            while table[row][column] != "0 ":
                row, column = self.get_size((len(table)-1), (len(table[0])-1))
            self.place_on_board(table, row, column)
        else:
            self.place_on_board(table, row, column)

    def place_on_board(self, table, row, column):
        self.inrow(table, row, column, self.color())
        self.incolumn(table, row, column, self.color())
        self.diagonally_left_down(table, row, column, self.color())
        self.diagonally_left_up(table, row, column, self.color())
        self.diagonally_right_up(table, row, column, self.color())
        self.diagonally_right_down(table, row, column, self.color())
        self.count_points(table, row, column)

    def get_size(self, height, width):
        row = input("Podaj numer wiersza:\n")
        while not(row.isdigit() and int(row) in range(1, width+1)):
            if row == "X":
                return row, 0
            row = input("Podaj prawidłowy numer wiersza:\n")
        column = input("Podaj numer kolumny:\n")
        while not(column.isdigit() and int(column) in range(1, height+1)):
            column = input("Podaj prawidłowy numer kolumny:\n")
        return int(row), int(column)

    def letter(self, name=""):
        if name == "Black":
            letter = "M "
        elif name == "White":
            letter = "Z "
        return letter

    def inrow(self, table, row, column, name=""):
        letter = self.letter(name)
        table[row][column] = letter
        a = row
        b = column + 1
        while b < len(table[0]) and table[a][b] != f'{letter}':
            if table[a][b] == "0 ":
                b = column + 1
                break
            b += 1
        if b != len(table[0]):
            for i in range(column, b):
                table[a][i] = f'{letter}'
        a = row
        b = column - 1
        while table[a][b] != f'{letter}' and b > 0:
            if table[a][b] == "0 ":
                b = column - 1
                break
            b -= 1
        if b != 0:
            b += 1
            for i in range(b, column):
                table[a][i] = f'{letter}'

    def incolumn(self, table, row, column, name=""):
        letter = self.letter(name)
        a = row + 1
        b = column
        while a < len(table) and table[a][b] != f'{letter}':
            if table[a][b] == "0 ":
                a = row + 1
                break
            a += 1
        if a != len(table):
            for i in range(row, a):
                table[i][b] = f'{letter}'
        a = row - 1
        b = column
        while a > 0 and table[a][b] != f'{letter}':
            if table[a][b] == "0 ":
                a = row - 1
                break
            a -= 1
        if a != 0:
            a += 1
            for i in range(a, row):
                table[i][b] = f'{letter}'

    def diagonally_right_down(self, table, row, column, name=""):
        letter = self.letter(name)
        a = row + 1
        b = column + 1
        while a < len(table) and b < len(table[0]) and table[a][b] != f'{letter}':
            if table[a][b] == "0 ":
                a = row + 1
                b = column + 1
                break
            a += 1
            b += 1
        if a != len(table) and b != len(table[0]):
            a -= 1
            b = column + 1
            for i in range(row + 1, a + 1):
                table[i][b] = f'{letter}'
                b += 1

    def diagonally_right_up(self, table, row, column, name=""):
        letter = self.letter(name)
        a = row - 1
        b = column + 1
        while a > 0 and b < len(table[0]) and table[a][b] != f'{letter}':
            if table[a][b] == "0 ":
                a = row - 1
                b = column + 1
                break
            a -= 1
            b += 1
        if a != 0 and b != len(table[0]):
            a += 1
            b -= 1
            for i in range(a, row):
                table[i][b] = f'{letter}'
                b -= 1

    def diagonally_left_up(self, table, row, column, name=""):
        letter = self.letter(name)
        a = row - 1
        b = column - 1
        while a > 0 and b > 0 and table[a][b] != f'{letter}':
            if table[a][b] == "0 ":
                a = row - 1
                b = column - 1
                break
            a -= 1
            b -= 1
        if a == 0 or b == 0:
            pass
        else:
            if a != len(table) and b != len(table[0]):
                a += 1
                b += 1
                for i in range(a, row):
                    table[i][b] = f'{letter}'
                    b += 1

    def diagonally_left_down(self, table, row, column, name=""):
        letter = self.letter(name)
        a = row + 1
        b = column - 1
        while a < len(table) and b > 0 and table[a][b] != f'{letter}':
            if table[a][b] == "0 ":
                a = row + 1
                b = column - 1
                break
            a += 1
            b -= 1
        if a != len(table) and b != 0:
            a -= 1
            b += 1
            for i in range(b, column):
                table[a][i] = f'{letter}'
                a -= 1

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
            if row == 0 and column == 0:
                self.set_points(number_of_appearances)
                pass
            else:
                print("Nieprawidłowy ruch! Proszę podać inne pola.")
                table[row][column] = "0 "
                self.move_on_board(table)
