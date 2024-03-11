from unittest.mock import patch
import pytest
from solutions import (
    minmax,
    minmax_keys,
    minmax_values,
    keys_of_minmax_values,
    minmax_items,
    minmax2
)


@pytest.mark.parametrize(
    "arguments, expected",
    [
        ((1, 3, 2, 5), (1, 5)),
        ((9, 7, 6), (6, 9)),
        (range(5), (0, 4))
    ],
)
def test_minmax(arguments, expected):
    result = minmax(arguments)
    assert result == expected, f"\nresult  : {result}\nexpected: {expected}"

def test_none():
    result = minmax([])
    expected = (None, None)
    assert result == expected, f'\nresult  : {result}\nexpected: {expected}'

@pytest.mark.parametrize(
'arguments, default, expected',
[
([], 0, (0, 0)),
([], -1, (-1, -1)),
]
)
def test_default(arguments, default, expected):
    result = minmax([], default=default)
    expected = (default, default)
    assert result == expected, f'\nresult  : {result}\nexpected: {expected}'

def test_strings():
    result = minmax(['world', 'is', 'strange', 'hello'])
    expected = ('hello', 'world')
    assert result == expected, f'\nresult  : {result}\nexpected: {expected}'

def test_key():
    result = minmax(['world', 'is', 'strange', 'hello'], key=len)
    expected = ('is', 'strange')
    assert result == expected, f'\nresult  : {result}\nexpected: {expected}'

    result = minmax(['World', 'is', 'strange', 'hello'], key=str.lower)
    expected = ('hello', 'World')
    assert result == expected, f'\nresult  : {result}\nexpected: {expected}'

def test_minmax_keys():
    assert minmax_keys(dict(a=1, b=2)) == ('a', 'b')
    assert minmax_keys({'a': 3, 'b': 4, 'c': 5}) == ('a', 'c')

    # this verifies that minmax was called by minmax_keys
    with patch('solutions.omtenta_20220819.minmax', return_value=(None, None)) as mock_mm:
        minmax_keys({'a': 1})

    mock_mm.assert_called_with({'a': 1})

def test_minmax_values():
    assert minmax_values(dict(a=1, b=2)) == (1, 2)
    assert minmax_values({'a': 3, 'b': 4, 'c': 5}) == (3, 5)

    # did you call minmax?

    with patch('solutions.omtenta_20220819.minmax', return_value=(None, None)) as mock_mm:
        minmax_values({})

    mock_mm.assert_called()

def test_keys_of_minmax_values():
    dct = {'a': 2, 'b': 1}
    assert minmax(dct) == ('a', 'b')
    assert minmax_values(dct) == (1, 2)
    assert keys_of_minmax_values(dct) == ('b', 'a')

    # did you call minmax?

    with patch('solutions.omtenta_20220819.minmax', return_value=(None, None)) as mock_mm:
        keys_of_minmax_values({})

    mock_mm.assert_called()

def test_keys_of_minmax_items():
    dct = {'b': 2, 'a': 1}
    assert minmax_items(dct) == (('a', 1), ('b', 2))

    # did you call minmax?
    with patch('solutions.omtenta_20220819.minmax', return_value=(None, None)) as mock_mm:
        minmax_items({})

    mock_mm.assert_called()

def test_3a():
    # repeat the previous test,
    result = minmax2(['world', 'is', 'strange', 'hello'], key=len)
    expected = ('is', 'strange')

    assert result == expected, f'\nresult  : {result}\nexpected: {expected}'

    # but note that the return value is not the ordinary tuple
    assert result.__class__.__name__ == 'MinMax'

def test_3b():
    # the return value of the `minmax2` function is an object with attributes min and max

    result = minmax2(['world', 'is', 'strange', 'hello'], key=len)

    assert result.min == 'is'
    assert result.max == 'strange'

def test_3c():
    # This test verifies that the original function minmax was called
    from solutions import minmax2
    from unittest.mock import patch
    with patch('solutions.omtenta_20220819.minmax', return_value=(None, None)) as mock_mm:
        minmax2([])
    mock_mm.assert_called_with([], default=None, key=None)

def test_3d():
    assert minmax2([1, 2, 3]) == (1, 3)
    assert minmax2(1, 2, 3) == (1, 3)

    assert minmax2(range(5)) == (0, 4)
    assert minmax2(*range(5)) == (0, 4)
