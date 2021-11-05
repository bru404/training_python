from solution import get_sum_digits


def test_get_sum_digits() -> None:
    actual = get_sum_digits(1111)
    expected = 4
    assert actual == expected, 'Неверная сумма цифр числа'

    actual = get_sum_digits(1984)
    expected = 22
    assert actual == expected, 'Неверная сумма цифр числа'

    actual = get_sum_digits(000000)
    expected = 0
    assert actual == expected, 'Неверная сумма цифр числа'
