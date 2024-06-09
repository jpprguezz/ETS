import pytest

from operations import sum, sub, mul, div, pow

@pytest.mark.parametrize("a,b,expected_result", [(2, 4, 6), (3, 1, 4), (9, 2, 11)])
def test_sum(a, b, expected_result):
    assert sum(a, b) == expected_result

@pytest.mark.parametrize("a,b,expected_result", [(3, 1, 2), (10, 10, 0), (150, 25, 125)])
def test_sub(a, b, expected_result):
    assert sub(a, b) == expected_result

@pytest.mark.parametrize("a,b,expected_result", [(2, 2, 4), (3, 3, 9), (9, 2, 18)])
def test_mul(a, b, expected_result):
    assert mul(a, b) == expected_result

@pytest.mark.parametrize("a,b,expected_result", [(6, 3, 2), (10, 2, 5)])
def test_div(a, b, expected_result):
    assert div(a, b) == expected_result

@pytest.mark.parametrize("a,b,expected_result", [(2, 3, 8), (10, 2, 100)])
def test_pow(a, b, expected_result):
    assert pow(a, b) == expected_result