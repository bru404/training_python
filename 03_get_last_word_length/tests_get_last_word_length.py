from solution import get_last_word_length


def test_get_last_word_length() -> None:
    actual = get_last_word_length('I hate programming')
    expected = 11
    assert actual == expected, 'Неверная длина последнего слова'

    actual = get_last_word_length('Hello world')
    expected = 5
    assert actual == expected, 'Неверная длина последнего слова'


def test_get_last_word_length_with_empty_string() -> None:
    try:
        actual = get_last_word_length('')
        expected = 0
        assert actual == expected, 'Неверная длина последнего слова'
    except IndexError:
        assert False, 'В решении не учтено, что строка может быть пустой'
