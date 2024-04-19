import pytest
from lib.counter import Counter

@pytest.fixture
def counter():
    return Counter()

def test_counter_init_with_count_0(counter):
    assert counter.count == 0

def test_counter_adds_to_count(counter):
    counter.add(1)
    counter.add(2)
    counter.add(3)
    assert counter.count == 6

def test_counter_report_returns_formatted_count_string(counter):
    counter.add(1)
    counter.add(2)
    counter.add(3)
    assert counter.report() == "Counted to 6 so far."