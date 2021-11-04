from solution import get_common_elements


def test_get_common_elements() -> None:
    arr1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    actual = get_common_elements(arr1, arr2)
    expected = [1, 1, 2, 3, 5, 8, 13]
    assert actual == expected, 'Общие элементы найдены неверно'

    arr1 = [1, 2, 3]
    arr2 = [1, 2]
    actual = get_common_elements(arr1, arr2)
    expected = [1, 2]
    assert actual == expected, 'Общие элементы найдены неверно'


def test_get_common_elements_without_common() -> None:
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    actual = get_common_elements(arr1, arr2)
    expected = []
    assert actual == expected, 'Убедись, что при отсутствии общего, возвращается пустой список'
