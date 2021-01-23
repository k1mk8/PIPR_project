import pytest
from player import Player


def test_player_init(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    assert player


def test_player_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    assert player.name() == 'Karol'


def test_player_points(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    assert player.points() == 2


def test_player_set_points(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    player.set_points(5)
    assert player.points() == 5


def test_player_color(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    assert player.color() == "Black"


def test_player_letter(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    letter = player.letter(player.color())
    assert letter == "M "


def test_player_get_size(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert player.get_size(10, 10) == (1, 1)


def test_player_inrow(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
    ['1 ', '0 ', '0 ', '0 ', '0 '],
    ['2 ', '0 ', 'Z ', 'M ', '0 '],
    ['3 ', '0 ', 'M ', 'Z ', '0 '],
    ['4 ', '0 ', '0 ', '0 ', '0 ']]
    player.inrow(table, 2, 1, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
    ['1 ', '0 ', '0 ', '0 ', '0 '],
    ['2 ', 'M ', 'M ', 'M ', '0 '],
    ['3 ', '0 ', 'M ', 'Z ', '0 '],
    ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_player_incolumn(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    player.incolumn(table, 1, 2, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', 'M ', '0 ', '0 '],
        ['2 ', '0 ', 'M ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_player_diagonally_right_down(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', 'M ']]
    player.diagonally_right_down(table, 1, 1, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'M ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'M ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', 'M ']]


def test_player_diagonally_right_up(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'Z ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    player.diagonally_right_up(table, 4, 1, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_player_diagonally_left_up(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', 'M ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'Z ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    player.diagonally_left_up(table, 4, 4, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', 'M ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'M ', 'M ', '0 '],
        ['3 ', '0 ', 'Z ', 'M ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_player_diagonally_left_down(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'Z ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    player.diagonally_left_down(table, 1, 4, "Black")
    assert table == [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', '0 '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'Z ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]


def test_player_count_points(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Karol')
    player = Player("Black")
    table = [['X ', '1 ', '2 ', '3 ', '4 '],
        ['1 ', '0 ', '0 ', '0 ', 'M '],
        ['2 ', '0 ', 'Z ', 'M ', '0 '],
        ['3 ', '0 ', 'M ', 'M ', '0 '],
        ['4 ', '0 ', '0 ', '0 ', '0 ']]
    player.count_points(table, 1, 4)
    assert player.points() == 4
