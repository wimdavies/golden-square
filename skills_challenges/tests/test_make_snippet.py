from lib.make_snippet import make_snippet

# empty string => empty string
def test_given_empty_string_returns_empty_string():
    assert make_snippet("") == ""

# four words => four words
def test_given_four_words_returns_four_words():
    assert make_snippet("once upon a stormy") == "once upon a stormy"

# five words => five words
def test_given_five_words_returns_five_words():
    assert make_snippet("once upon a stormy night") == "once upon a stormy night"

# six words => five words plus "..."
def test_given_six_words_returns_five_words_plus_ellipsis():
    assert make_snippet("once upon a stormy night I") == "once upon a stormy night..."

# ten words => five words plus "..."
def test_given_ten_words_returns_five_words_plus_ellipsis():
    assert make_snippet("once upon a stormy night I went to bed anyway") == "once upon a stormy night..."
