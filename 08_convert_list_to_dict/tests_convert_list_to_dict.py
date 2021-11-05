from solution import convert_list_to_dict


def test_convert_list_to_dict() -> None:
    arr = ['Barbara', 'Gordon', 'Alfred', 'Pennyworth', 'Jason', 'Todd', 'Slade', 'Wilson']
    actual = convert_list_to_dict(arr)
    expected = {'Barbara': 'Gordon', 'Alfred': 'Pennyworth', 'Jason': 'Todd', 'Slade': 'Wilson'}
    assert actual == expected, 'Словарь из списка сформирован неверно'

    arr = ['1', '2', '3', '4']
    actual = convert_list_to_dict(arr)
    expected = {'1': '2', '3': '4'}
    assert actual == expected, 'Словарь из списка сформирован неверно'


def test_convert_list_to_dict_with_odd_elements() -> None:
    try:
        arr = ['bla', 'bla', 'bla']
        actual = convert_list_to_dict(arr)
        expected = {'err_msg': 'Передан список с нечетным кол-вом элементов'}
        assert actual == expected, 'Формат словаря с текстом ошибки неверный'
    except IndexError:
        assert False, 'Не учтен список с нечетным кол-вом элементов во входных данных'
