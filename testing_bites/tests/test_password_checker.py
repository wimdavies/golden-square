import pytest
from lib.password_checker import PasswordChecker

def test_check_returns_True_if_password_long_enough():
    pass_check = PasswordChecker()
    assert pass_check.check("goblintoast") == True

def test_check_raises_exception_if_password_too_short():
    pass_check = PasswordChecker()
    with pytest.raises(Exception, match=r"Invalid password, must be 8\+ characters."):
        pass_check.check("gob")