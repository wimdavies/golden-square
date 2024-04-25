from lib.todo_list import TodoList

def test_todo_list_init_with_empty_list():
    assert TodoList()._storage == []

def test_todo_list_incomplete_returns_empty_list_when_none_added():
    assert TodoList().complete() == []

def test_todo_list_complete_returns_empty_list_when_none_added():
    assert TodoList().incomplete() == []

def test_todo_list_give_up_returns_does_nothing_when_none_added():
    todo_list = TodoList()
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == []
