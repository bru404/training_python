from solution import while_cycle


def test_while_cycle() -> None:
    actual = while_cycle([1, 2, 3, 4, 5, 6])
    expected = '1\n' \
               '2\n' \
               '3\n' \
               '4\n' \
               '5\n' \
               '6\n'
    assert actual == expected
