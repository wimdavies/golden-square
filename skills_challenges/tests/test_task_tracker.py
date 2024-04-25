import pytest
from lib.task_tracker import TaskTracker

def test_init_with_empty_list():
    task_tracker = TaskTracker()
    assert task_tracker.list_incomplete() == []

def test_add_task_that_is_not_string_raises_TypeError():
    task_tracker = TaskTracker()
    with pytest.raises(TypeError, match=r"A valid task can only be a string"):
        task_tracker.add(42)
    with pytest.raises(TypeError, match=r"A valid task can only be a string"):
        task_tracker.add([])
    with pytest.raises(TypeError, match=r"A valid task can only be a string"):
        task_tracker.add(None)

def test_add_single_task_is_in_list():
    task_tracker = TaskTracker()
    task_tracker.add("Walk the dog")
    assert task_tracker.list_incomplete() == ["Walk the dog"]

def test_add_multiple_tasks_all_in_list():
    task_tracker = TaskTracker()
    task_tracker.add("Walk the dog")
    task_tracker.add("Stroke the cat")
    assert task_tracker.list_incomplete() == ["Walk the dog", "Stroke the cat"]

def test_mark_single_task_complete():
    task_tracker = TaskTracker()
    task_tracker.add("Walk the dog")
    task_tracker.add("Stroke the cat")
    task_tracker.add("Wash the car")
    task_tracker.mark_complete(2)
    assert task_tracker.list_incomplete() == ["Walk the dog", "Stroke the cat"]

def test_mark_multiple_tasks_complete():
    task_tracker = TaskTracker()
    task_tracker.add("Walk the dog")
    task_tracker.add("Stroke the cat")
    task_tracker.add("Wash the car")
    task_tracker.mark_complete(0)
    task_tracker.mark_complete(0)
    assert task_tracker.list_incomplete() == ["Wash the car"]

def test_index_too_low_raises_Exception():
    task_tracker = TaskTracker()
    task_tracker.add("Walk the dog")
    task_tracker.add("Stroke the cat")
    task_tracker.add("Wash the car")
    with pytest.raises(Exception, match=r"No task exists at that index"):
        task_tracker.mark_complete(-4)
    assert task_tracker.list_incomplete() == ["Walk the dog", "Stroke the cat", "Wash the car"]

def test_index_too_high_raises_Exception():
    task_tracker = TaskTracker()
    task_tracker.add("Walk the dog")
    with pytest.raises(Exception, match=r"No task exists at that index"):
        task_tracker.mark_complete(1)
    assert task_tracker.list_incomplete() == ["Walk the dog"]
