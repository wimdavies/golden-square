from unittest.mock import Mock
from lib.task_list import TaskList

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []

def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_task_list_all_returns_list_of_all_tasks():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_2 = Mock()
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    assert task_list.all() == [fake_task_1, fake_task_2]

def test_task_list_all_returns_list_of_all_tasks():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_2 = Mock()
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    assert task_list.all() == [fake_task_1, fake_task_2]

def test_task_list_all_complete_returns_false_for_no_completed_tasks():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_1.is_complete.return_value = False
    task_list.add(fake_task_1)
    assert task_list.all_complete() == False
    fake_task_1.is_complete.assert_called_once()

def test_task_list_all_complete_returns_false_for_partial_completed_tasks():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_2 = Mock()
    fake_task_3 = Mock()
    fake_task_1.is_complete.return_value = True
    fake_task_2.is_complete.return_value = True
    fake_task_3.is_complete.return_value = False
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    task_list.add(fake_task_3)
    assert task_list.all_complete() == False

def test_task_list_all_complete_returns_true_for_all_completed_tasks():
    task_list = TaskList()
    fake_task_1 = Mock()
    fake_task_2 = Mock()
    fake_task_3 = Mock()
    fake_task_1.is_complete.return_value = True
    fake_task_2.is_complete.return_value = True
    fake_task_3.is_complete.return_value = True
    task_list.add(fake_task_1)
    task_list.add(fake_task_2)
    task_list.add(fake_task_3)
    assert task_list.all_complete() == True
