from lib.todo_checker import *

"""
Given "#TODO"
It returns True
"""
def test_todo_checker_with_only_the_target():
    result = todo_checker("#TODO")
    assert result == True

"""
Given "Hello #TODO"
It returns True
"""
def test_todo_checker_with_string_including_target():
    assert todo_checker("Hello #TODO") == True

"""
Given a string with multiple instances of the target
It returns True
"""
def test_todo_checker_with_string_including_target_twice():
    assert todo_checker("Hello #TODO #TODO") == True

"""
Given a string with no target
It returns False
"""
def test_todo_checker_with_string_excluding_target():
    assert todo_checker("Hello") == False

"""
Given an empty string
It returns False
"""
def test_todo_checker_with_empty_string():
    assert todo_checker("") == False

"""
Given a string containing an incomplete target
Return False
"""
def test_todo_checker_with_string_including_incomplete_target():
    assert todo_checker("hello TODO") == False

"""
Given a string containing an incomplete target
Return False
"""
def test_todo_checker_with_string_including_differently_incomplete_target():
    assert todo_checker("#TO: Do a barrel-roll") == False

"""
Given "ItWill#TODOTonight"
It returns True
"""
def test_todo_checker_with_unspaced_string_including_target():
    assert todo_checker("ItWill#TODOTonight") == True
