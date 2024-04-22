import pytest
from lib.string_builder import StringBuilder

@pytest.fixture
def string_builder():
    return StringBuilder()

def test_string_builder_init_with_empty_string(string_builder):
    assert string_builder.str == ""

def test_string_builder_add_concatenates_arg_with_str(string_builder):
    string_builder.add("Hello")
    assert string_builder.str == "Hello"

def test_string_builder_size_returns_length_of_str(string_builder):
    assert string_builder.size() == 0

def test_string_builder_output_returns_str(string_builder):
    assert string_builder.output() == ""
