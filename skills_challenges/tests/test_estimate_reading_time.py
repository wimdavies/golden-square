import pytest
from lib.estimate_reading_time import *

def test_estimate_reading_time_given_empty_string_returns_0_0():
    result = estimate_reading_time("")
    assert result == 0.0

def test_estimate_reading_time_given_200_words_returns_1_0():
    result = estimate_reading_time("yo " * 200)
    assert result == 1.0

def test_estimate_reading_time_given_100_words_returns_0_5():
    result = estimate_reading_time("yo " * 100)
    assert result == 0.5

def test_estimate_reading_time_given_300_words_returns_1_5():
    result = estimate_reading_time("yo " * 300)
    assert result == 1.5

def test_estimate_reading_time_given_400_words_returns_2_0():
    result = estimate_reading_time("yo " * 400)
    assert result == 2.0

def test_estimate_reading_time_given_None_it_raises():
    with pytest.raises(TypeError, match=r"Argument must be a string"):
        estimate_reading_time(None)
