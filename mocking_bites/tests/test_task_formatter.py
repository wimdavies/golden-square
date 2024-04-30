from lib.task_formatter import TaskFormatter
from unittest.mock import Mock

def test_task_formatter_init_with_task():
    fake_task = Mock()
    task_formatter = TaskFormatter(fake_task)
    assert task_formatter.task == fake_task

def test_task_formatter_format_returns_correct_format_for_incomplete_task():
    fake_task = Mock()
    fake_task.title = "Walk the dog"
    fake_task.is_complete.return_value = False
    task_formatter = TaskFormatter(fake_task)
    assert task_formatter.format() == "- [ ] Walk the dog"
    fake_task.is_complete.assert_called()

def test_task_formatter_format_returns_correct_format_for_complete_task():
    fake_task = Mock()
    fake_task.title = "Wash the car"
    fake_task.is_complete.return_value = True
    task_formatter = TaskFormatter(fake_task)
    assert task_formatter.format() == "- [x] Wash the car"
    fake_task.is_complete.assert_called()
