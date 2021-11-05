from solution import is_palindrome


def test_is_palindrome() -> None:
    actual = is_palindrome('radar')
    expected = True
    assert actual == expected, 'Неверное определение палиндрома'

    actual = is_palindrome('civic')
    expected = True
    assert actual == expected, 'Неверное определение палиндрома'

    actual = is_palindrome('Because I am Batman')
    expected = False
    assert actual == expected, 'Неверное определение палиндрома'

    actual = is_palindrome('')
    expected = True
    assert actual == expected, 'Неверное определение палиндрома'
