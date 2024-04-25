import pytest
from lib.todo_list import TodoList
from lib.todo import Todo

@pytest.fixture
def empty_todo_list():
    return TodoList()

@pytest.fixture
def busy_todo_list():
    todo_list = TodoList()
    todo_1 = Todo("Walk the dog")
    todo_2 = Todo("Pet the cat")
    todo_3 = Todo("Wash the car")
    todo_list.add(todo_1)
    todo_list.add(todo_2)
    todo_list.add(todo_3)
    return todo_list

def test_todo_list_incomplete_returns_one_task_when_one_added(empty_todo_list):
    todo_1 = Todo("Walk the dog")
    empty_todo_list.add(todo_1)
    assert empty_todo_list.incomplete() == [todo_1]

def test_todo_list_incomplete_returns_multiple_tasks_when_multiple_added(busy_todo_list):
    assert len(busy_todo_list.incomplete()) == 3

def test_todo_list_incomplete_returns_list_less_first_when_first_completed(busy_todo_list):
    busy_todo_list.incomplete()[0].mark_complete()
    assert len(busy_todo_list.incomplete()) == 2
    assert busy_todo_list.incomplete()[0].task == "Pet the cat"

def test_todo_list_complete_returns_list_of_first_when_first_completed(busy_todo_list):
    busy_todo_list.incomplete()[0].mark_complete()
    assert len(busy_todo_list.complete()) == 1
    assert busy_todo_list.complete()[0].task == "Walk the dog"

def test_todo_list_complete_returns_empty_list_when_none_completed(busy_todo_list):
    assert busy_todo_list.complete() == []

def test_give_up_marks_all_as_complete(busy_todo_list):
    busy_todo_list.give_up()
    assert len(busy_todo_list.complete()) == 3
    assert busy_todo_list.incomplete() == []