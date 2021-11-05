from solution import shuffle_list


def test_shuffle_list() -> None:
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    actual = shuffle_list(arr)
    expected = [1, 8, 2, 7, 3, 6, 4, 5]
    assert actual == expected, 'Список перетасован неверно'


def test_shuffle_list_with_odd_elements() -> None:
    arr = [2, 8, 20, 28, 50, 82, 12]
    actual = shuffle_list(arr)
    expected = {'err_msg': 'Передан список с нечетным кол-вом элементов'}
    assert actual == expected, 'Не учтен список с нечетным кол-вом элементов во входных данных'
