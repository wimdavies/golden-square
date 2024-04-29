import pytest
from lib.multiclass.todo import Todo

def test_todo_raises_type_error_if_not_string():
    with pytest.raises(TypeError, match=r"Task must be a string"):
        Todo(None)

def test_todo_sets_task_with_complete_set_to_false():
    assert Todo("Walk the dog").complete == False

def test_todo_marks_complete_to_true():
    todo = Todo("Walk the dog")
    todo.mark_complete()
    assert todo.complete == True
