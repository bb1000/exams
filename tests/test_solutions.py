import pytest
from solutions import (
    GBP,
    NegativePounds,
    to_pence,
)




@pytest.mark.parametrize(
    "arguments, expected",
    [
        ((1, 0, 0), 240),
        ((0, 1, 0), 12),
        ((0, 0, 5), 5),
        ((1, 1, 1), 253),
    ],
)
def test_to_pence(arguments, expected):
    assert to_pence(*arguments) == expected


@pytest.mark.parametrize(
    "arguments, expected",
    [
        ((0, 0, 13), (0, 1, 1)),
        ((0, 0, 245), (0, 0, 5)),
        ((0, 0, 245), (1, 1, 0)),
    ],
)
def test_reduce(arguments, expected):
    assert GBP(1, 1, 1) == GBP(0, 21, 1)  # This is fine


def test_negative_pounds():
    with pytest.raises(NegativePounds):
        GBP(1, -21, 0)  # Not fine


def test_gbp():
    assert GBP(1, -19, 0) == GBP(0, 1, 0)  # This is fine

def test_raises():
    with pytest.raises(NegativePounds):
        GBP(1, -21, 0) # Not fine
