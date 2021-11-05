from solution import is_subsequence


def test_is_subsequence() -> None:
    actual = is_subsequence('pi', 'ghidmpmgfpczasdfi')
    expected = True
    assert actual == expected, 'Подпоследовательность найдена неверно'

    actual = is_subsequence('abcde', 'qweabcdrtye')
    expected = True
    assert actual == expected, 'Подпоследовательность найдена неверно'

    actual = is_subsequence('op', 'poghd')
    expected = False
    assert actual == expected, 'Подпоследовательность найдена неверно'
