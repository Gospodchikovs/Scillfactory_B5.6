from main import win_combination


def test_win_combination_horizontal():
    test_field = [['X', 'X', 'X'], ['-', '-', '-'], ['-', '-', '-']]
    res = win_combination(test_field)
    assert res
    test_field = [['0', '0', '0'], ['-', '-', '-'], ['-', '-', '-']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', '-', '-'], ['X', 'X', 'X'], ['-', '-', '-']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', '-', '-'], ['0', '0', '0'], ['-', '-', '-']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', '-', '-'], ['-', '-', '-'], ['X', 'X', 'X']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', '-', '-'], ['-', '-', '-'], ['0', '0', '0']]
    res = win_combination(test_field)
    assert res


def test_win_combination_vertical():
    test_field = [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
    res = win_combination(test_field)
    assert res
    test_field = [['0', '-', '-'], ['0', '-', '-'], ['0', '-', '-']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', 'X', '-'], ['-', 'X', '-'], ['-', 'X', '-']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', '0', '-'], ['-', '0', '-'], ['-', '0', '-']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', '-', 'X'], ['-', '-', 'X'], ['-', '-', 'X']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', '-', '0'], ['-', '-', '0'], ['-', '-', '0']]
    res = win_combination(test_field)
    assert res


def test_win_combination_diagonal():
    test_field = [['X', '-', '-'], ['-', 'X', '-'], ['-', '-', 'X']]
    res = win_combination(test_field)
    assert res
    test_field = [['0', '-', '-'], ['-', '0', '-'], ['-', '-', '0']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', '-', 'X'], ['-', 'X', '-'], ['X', '-', '0']]
    res = win_combination(test_field)
    assert res
    test_field = [['-', '-', '0'], ['-', '0', '-'], ['0', '-', '-']]
    res = win_combination(test_field)
    assert res
