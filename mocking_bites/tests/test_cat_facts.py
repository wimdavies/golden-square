from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_provide_returns_formatted_cat_fact_string():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"The leopard is the most widespread of all big cats.","length":51}
    cat_facts = CatFacts(requester_mock)
    assert cat_facts.provide() == "Cat fact: The leopard is the most widespread of all big cats."
