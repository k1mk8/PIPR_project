import random
import time


class Computer:
    def __init__(self, color):
        """
        tworzy obiekt klasy komputer i przyjmuje jego nazwe
        """
        self._name = input("Podaj nazwę gracza komputerowego:\n")
        self._points = 2
        self._color = color
        self.counter = 0

    def name(self):
        """
        zwraca nazwe komputera
        """
        return self._name

    def points(self):
        """
        zwraca punkty komputera
        """
        return self._points

    def color(self):
        """
        zwraca kolor jakim gra dany komputer
        """
        return self._color

    def set_points(self, points):
        """
        ustawia ilość punktów danemu komputerowi
        """
        self._points = points

    def letter(self, name=""):
        """
        zwraca litere jaką porusza się komputer
        """
        if name == "Black":
            letter = "M "
        elif name == "White":
            letter = "Z "
        return letter

    def move_on_board(self, table):
        """
        przeprowadza losowanie pozycji i ruch na planszy
        """
        if self.counter > 300:
            self.counter = 0
            print("Jeden z graczy komputerowych pominął ruch!\n\n\n")
            time.sleep(2)
        else:
            height, width = self.random_pos(len(table)-1, len(table[0])-1, table)
            self.place_on_board(table, height, width)

    def place_on_board(self, table, row, column):
        """
        sprawdza wszystkie możliwości ruchu na planszy
        """
        self.inrow(table, row, column, self.color())
        self.incolumn(table, row, column, self.color())
        self.diagonally_left_down(table, row, column, self.color())
        self.diagonally_left_up(table, row, column, self.color())
        self.diagonally_right_up(table, row, column, self.color())
        self.diagonally_right_down(table, row, column, self.color())
        self.count_points(table, row, column)

    def random_pos(self, height, width, table):
        """
        losuje pozycję z odpowiedniego zakresu
        """
        random_height = random.randint(1, height)
        random_width = random.randint(1, width)
        while table[random_height][random_width] != "0 ":
            random_height = random.randint(1, height)
            random_width = random.randint(1, width)
        return random_height, random_width

    def inrow(self, table, row, column, name=""):
        """
        sprawdza możliwość ruchu w linii
        """
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
        """
        sprawdza możliwość ruchu w kolumnie
        """
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
        """
        sprawdza możliwość ruchu po skosie do dołu i w prawo
        """
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
        """
        sprawdza możliwość ruchu po skosie do góry i w prawo
        """
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
        """
        sprawdza możliwość ruchu po skosie do góry i w lewo
        """
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
        """
        sprawdza możliwość ruchu po skosie do dołu i w lewo
        """
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
        """
        liczy ilość punktów na planszy i zatwierdza poprawność ruchu
        """
        letter = self.letter(self.color())
        number_of_appearances = 0
        for i in range(1, (len(table))):
            for j in range(1, (len(table[0]))):
                if table[i][j] == letter:
                    number_of_appearances += 1
        if number_of_appearances > self.points() + 1:
            self.set_points(number_of_appearances)
            print("Komputer wykonał ruch!\n\n\n")
            time.sleep(2)
        else:
            if row == 0 and column == 0:
                self.set_points(number_of_appearances)
            else:
                table[row][column] = "0 "
                self.counter += 1
                self.move_on_board(table)
