import pytest
from solutions import GBP, NegativePounds

def test_gbp():
    assert GBP(1, -19, 0) == GBP(0, 1, 0) # This is fine

def test_negative_pounds():
    with pytest.raises(NegativePounds):
        GBP(1, -21, 0) # Not fine
