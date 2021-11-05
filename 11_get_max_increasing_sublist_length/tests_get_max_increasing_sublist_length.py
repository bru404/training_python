from solution import get_max_increasing_sublist_length


def test_get_max_increasing_sublist_length() -> None:
    actual = get_max_increasing_sublist_length([1, 2, 3, 0])
    expected = 3
    assert actual == expected, 'Наибольшая длина возрастающего подсписка определена неверно'

    actual = get_max_increasing_sublist_length([99, 34, 2])
    expected = 1
    assert actual == expected, 'Наибольшая длина возрастающего подсписка определена неверно'

    actual = get_max_increasing_sublist_length([1, 2, 72, -600, 9, 17, 87, 0])
    expected = 4
    assert actual == expected, 'Наибольшая длина возрастающего подсписка определена неверно'
