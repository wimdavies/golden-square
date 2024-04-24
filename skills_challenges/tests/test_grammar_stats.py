import pytest
from lib.grammar_stats import GrammarStats

@pytest.fixture
def grammar_stats():
    return GrammarStats()

def test_check_init_raises_for_anything_other_than_string_arg(grammar_stats):
    with pytest.raises(TypeError, match=r"Argument must be a string"):
        grammar_stats.check(None)
    with pytest.raises(TypeError, match=r"Argument must be a string"):
        grammar_stats.check(1)
    with pytest.raises(TypeError, match=r"Argument must be a string"):
        grammar_stats.check([])

def test_check_raises_for_empty_string(grammar_stats):
    with pytest.raises(ValueError, match=r"String may not be empty"):
        assert grammar_stats.check("")

def test_check_returns_false_for_lower_case_string_no_punc(grammar_stats):
    assert grammar_stats.check("bum") == False

def test_check_returns_false_for_upper_case_string_no_punc(grammar_stats):
    assert grammar_stats.check("BUM") == False

def test_check_returns_false_for_valid_string_with_no_punc(grammar_stats):
    assert grammar_stats.check("Bum") == False

def test_check_returns_false_for_valid_string_with_invalid_punc(grammar_stats):
    assert grammar_stats.check("Bum,") == False
    assert grammar_stats.check("Bum/") == False
    assert grammar_stats.check("Bum:") == False

def test_check_returns_false_for_invalid_string_with_valid_punc(grammar_stats):
    assert grammar_stats.check("bum!") == False
    assert grammar_stats.check("bUM.") == False
    assert grammar_stats.check("bUm?") == False

def test_check_true_for_valid_string_with_valid_punc(grammar_stats):
    assert grammar_stats.check("Bum!") == True
    assert grammar_stats.check("BUM.") == True
    assert grammar_stats.check("BUm?") == True

def test_percentage_good_returns_0_when_no_checks_made(grammar_stats):
    assert grammar_stats.percentage_good() == 0

def test_percentage_good_returns_0_when_no_passes(grammar_stats):
    grammar_stats.check("bum")
    grammar_stats.check("bum")
    grammar_stats.check("bum")
    assert grammar_stats.percentage_good() == 0

def test_percentage_good_returns_100_when_all_passes(grammar_stats):
    grammar_stats.check("Bum!")
    grammar_stats.check("Bum!")
    assert grammar_stats.percentage_good() == 100

def test_percentage_good_returns_50_when_half_passes(grammar_stats):
    grammar_stats.check("Bum!")
    grammar_stats.check("Bum")
    assert grammar_stats.percentage_good() == 50

def test_percentage_good_returns_25_when_quarter_passes(grammar_stats):
    grammar_stats.check("Bum!")
    grammar_stats.check("Bum")
    grammar_stats.check("Bum")
    grammar_stats.check("Bum")
    assert grammar_stats.percentage_good() == 25

def test_percentage_good_rounds_and_returns_33_when_third_passes(grammar_stats):
    grammar_stats.check("Bum!")
    grammar_stats.check("Bum")
    grammar_stats.check("Bum")
    assert grammar_stats.percentage_good() == 33

def test_percentage_good_rounds_and_returns_67_when_two_thirds_passes(grammar_stats):
    grammar_stats.check("Bum!")
    grammar_stats.check("Bum!")
    grammar_stats.check("Bum")
    assert grammar_stats.percentage_good() == 67
