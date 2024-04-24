# todo_checker Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

> As a user
> So that I can keep track of my tasks
> I want to check if a text includes the string `#TODO`.

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def todo_checker(text):
    """Checks a string includes the string #TODO

    Parameters: (list all parameters and their types)
        text: a string containing words (e.g. "hello #TODO")

    Returns: (state the return value and its type)
        a Boolean, e.g. `True`

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Given "#TODO"
It returns True
"""
todo_checker("#TODO") => True

"""
Given "Hello #TODO"
It returns True
"""
todo_checker("Hello #TODO") => True

"""
Given a string with multiple instances of the target
It returns True
"""
todo_checker("Hello #TODO #TODO") => True

"""
Given a string with no target
It returns False
"""
todo_checker("hello WoRLD") => False

"""
Given an empty string
It returns False
"""
todo_checker("") => False

"""
Given a string containing an incomplete target
Return False
"""
todo_checker("hello TODO") => False

"""
Given a string containing an incomplete target
Return False
"""
todo_checker("#TO: Do a barrel-roll") => False

"""
Given "ItWill#TODOTonight"
It returns True
"""
todo_checker("ItWill#TODOTonight") => True
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
from lib.todo_checker import *

"""
Given "#TODO"
It returns True
"""

def test_todo_checker_with_only_the_target():
    result = todo_checker("#TODO")
    assert result == True
```

Ensure all test function names are unique, otherwise pytest will ignore them!
