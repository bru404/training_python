from solution import get_details


def test_get_details() -> None:
    actual = get_details([1, 2, 3, 4, 5, 6])
    expected = 'Index - 0 | Element - 1\n'\
               'Index - 1 | Element - 2\n'\
               'Index - 2 | Element - 3\n'\
               'Index - 3 | Element - 4\n'\
               'Index - 4 | Element - 5\n'\
               'Index - 5 | Element - 6\n'
    assert actual == expected, 'Неправильный формат выходных данных, либо неверное решение'
