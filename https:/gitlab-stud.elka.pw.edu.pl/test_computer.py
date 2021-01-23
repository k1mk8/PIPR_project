from computer import Computer


def test_computer_init(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    assert computer


def test_computer_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    assert computer.name() == 'Karol'


def test_computer_points(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    assert computer.points() == 2


def test_computer_set_points(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    computer.set_points(5)
    assert computer.points() == 5


def test_computer_color(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    assert computer.color() == "Black"


def test_computer_letter(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    letter = computer.letter(computer.color())
    assert letter == "M "


def test_computer_inrow(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
    ['1 ', '0 ', '0 ', '0 ', '0 '],
    ['2 ', '0 ', 'Z ', 'M ', '0 '],
    ['3 ', '0 ', 'M ', 'Z ', '0 '],
    ['4 ', '0 ', '0 ', '0 ', '0 ']]
    computer.inrow(table, 2, 1, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
    ['1 ', '0 ', '0 ', '0 ', '0 '],
    ['2 ', 'M ', 'M ', 'M ', '0 '],
    ['3 ', '0 ', 'M ', 'Z ', '0 '],
    ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_computer_incolumn(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    computer.incolumn(table, 1, 2, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', 'M ', '0 ', '0 '],
        ['2 ', '0 ', 'M ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_computer_diagonally_right_down(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', 'M ']]
    computer.diagonally_right_down(table, 1, 1, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'M ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'M ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', 'M ']]


def test_computer_diagonally_right_up(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'Z ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    computer.diagonally_right_up(table, 4, 1, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_computer_diagonally_left_up(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', 'M ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'Z ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    computer.diagonally_left_up(table, 4, 4, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', 'M ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'M ', 'M ', '0 '],
        ['3 ', '0 ', 'Z ', 'M ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_computer_diagonally_left_down(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'Z ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    computer.diagonally_left_down(table, 1, 4, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_computer_count_points(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    computer = Computer("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', 'M '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'M ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    computer.count_points(table, 1, 4)
    assert computer.points() == 4