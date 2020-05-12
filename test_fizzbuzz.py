from fizzbuzz import fizzbuzz


def test_number():
    assert fizzbuzz(1) == 1


def test_div_3():
    assert fizzbuzz(3) == 'Fizz'


def test_div_5():
    assert fizzbuzz(5) == 'Buzz'


def test_div_3and5():
    assert fizzbuzz(15) == 'Fizz Buzz'


def test_range():
    result = [fizzbuzz(x) for x in range(1, 16)]
    assert result == [
        1,
        2,
        'Fizz',
        4,
        'Buzz',
        'Fizz',
        7,
        8,
        'Fizz',
        'Buzz',
        11,
        'Fizz',
        13,
        14,
        'Fizz Buzz']


