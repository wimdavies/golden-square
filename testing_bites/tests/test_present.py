import pytest
from lib.present import Present

@pytest.fixture
def present():
    return Present()

def test_init_with_contents_None(present):
    assert present.contents == None

def test_wrap_sets_variable_as_contents(present):
    present.wrap("A puppy!")
    assert present.contents == "A puppy!"

def test_wrap_raises_if_present_already_contains_contents(present):
    present.wrap("A puppy!")
    with pytest.raises(Exception, match=r"A contents has already been wrapped."):
        present.wrap("A kitten!")

def test_unwrap_returns_contents(present):
    present.wrap("A puppy!")
    assert present.unwrap() == "A puppy!"

def test_unwrap_raises_if_nothing_wrapped_yet(present):
    with pytest.raises(Exception, match=r"No contents have been wrapped."):
        present.unwrap()