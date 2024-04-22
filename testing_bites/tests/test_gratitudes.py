import pytest
from lib.gratitudes import Gratitudes

@pytest.fixture
def gratitudes():
    return Gratitudes()

def test_init_with_empty_list(gratitudes):
    assert gratitudes.gratitudes == []

def test_add_adds_gratitude_to_list(gratitudes):
    gratitudes.add("kittens")
    assert gratitudes.gratitudes == ["kittens"]

def test_format_returns_string_of_formatted_gratitudes(gratitudes):
    gratitudes.add("kittens")
    gratitudes.add("puppies")
    assert gratitudes.format() == "Be grateful for: kittens, puppies"
