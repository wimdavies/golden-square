# Estimate reading time Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

>As a user
>So that I can manage my time
>I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def estimate_reading_time(text):
    """Estimates reading time for a string of words, assuming reading rate of 200wpm

    Parameters: (list all parameters and their types)
        text: a string of space-separated words (e.g. "one two three")

    Returns: (state the return value and its type)
        the time to read the text, in minutes. type: float

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
"""
Given 200 words
It returns 1.0
"""
estimate_reading_time("{200}") => 1.0

"""
Given empty string
It returns 0.0
"""
estimate_reading_time("") => 0.0

"""
Given 100 words
It returns 0.5
"""
estimate_reading_time("{100}") => 0.5

"""
Given 400 words
It returns 2.0
"""
estimate_reading_time("{400}") => 2.0

"""
Given 300 words
It returns 1.5
"""
estimate_reading_time("{300}") => 1.5

"""
Given a value other than a String
It throws an error
"""
estimate_reading_time(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python

from lib.estimate_reading_time import *

"""
Given 200 words
It returns 1.0
"""
estimate_reading_time("{200}") => 1.0
def test_estimate_reading_time_200_returns_1_as_float():
    result = estimate_reading_time("yo " * 200)
    assert result == 1.0
```

Ensure all test function names are unique, otherwise pytest will ignore them!
