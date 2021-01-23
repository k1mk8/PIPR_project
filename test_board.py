from board import Board


def test_board():
    board = Board(4, 4)
    assert board


def test_board_width():
    board = Board(4, 4)
    assert board.width() == 4


def test_board_width():
    board = Board(4, 5)
    assert board.height() == 5


def test_board_total_points():
    board = Board(4, 5)
    assert board.total_points() == 20


def test_board_make_board():
    board = Board(4, 4)
    assert board.table_board == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
    ['2 ', '0 ', '0 ', '0 ', '0 '],
    ['3 ', '0 ', '0 ', '0 ', '0 '],
    ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_board_start_board():
    board = Board(4, 4)
    board.start_board()
    assert board.table_board == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
    ['2 ', '0 ', 'Z ', 'M ', '0 '],
    ['3 ', '0 ', 'M ', 'Z ', '0 '],
    ['4 ', '0 ', '0 ', '0 ', '0 ']]