from solution import get_max_number


def test_get_max_number() -> None:
    actual = get_max_number([100, 200, 200, 1377])
    expected = 1377
    assert actual == expected, 'Неверно найден максимум в списке'

    actual = get_max_number([1, 1, 1, 1, 1])
    expected = 1
    assert actual == expected, 'Неверно найден максимум в списке'
