from lib.check_codeword import *

def test_check_codeword_returns_correct_for_horse():
    assert check_codeword("horse") == "Correct! Come in."

def test_check_codeword_returns_close_for_valid_start_and_end():
    assert check_codeword("hoe") == "Close, but nope."
    
def test_check_codeword_returns_close_for_valid_start_and_end():
    assert check_codeword("hoe") == "Close, but nope."

def test_check_codeword_returns_wrong_for_invalid_codeword():
    assert check_codeword("gorilla") == "WRONG!"
