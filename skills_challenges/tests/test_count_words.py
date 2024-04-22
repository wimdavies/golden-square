from lib.count_words import count_words

def test_returns_0_for_empty_string():
    assert count_words("") == 0

def test_returns_1_for_single_word():
    assert count_words("one") == 1

def test_returns_2_for_two_words():
    assert count_words("one two") == 2

def test_returns_5_for_five_words():
    assert count_words("one two three four five") == 5

def test_returns_1_for_a_single_hyphenated_word():
    assert count_words("single-toed") == 1

def test_returns_5_for_five_words_including_punctuation():
    assert count_words("one, two! three. four five") == 5

def test_returns_5_for_five_words_including_newlines():
    assert count_words("one two!\nthree. \nfour five") == 5