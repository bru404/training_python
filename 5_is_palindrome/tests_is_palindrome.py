from solution import is_palindrome


def test_is_palindrome() -> None:
    actual = is_palindrome('radar')
    expected = True
    assert actual == expected

    actual = is_palindrome('civic')
    expected = True
    assert actual == expected

    actual = is_palindrome('not a palindrome')
    expected = False
    assert actual == expected

    actual = is_palindrome('')
    expected = True
    assert actual == expected
