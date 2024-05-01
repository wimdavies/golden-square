# Car / Tyre Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

>As a car owner
>So that I can keep a record of details about my tyres
>I want to keep track of the tyres individually, by their position on my car
>
>As a car owner
>So that I have the two important pieces of data for a tyre
>I want to be able to record both tyre pressure and tyre tread depth
>
>As a car owner
>So that I have a history of tyre readings
>I want to be able to keep a record of historical readings, when those were, as well as current readings
>
>As a car owner
>So that I can see the details of my car at a glance
>I want to list the tyres' positions, latest readings and when those were

Verbs: keep track; keep a record; record (data); see details; list (readings)
Nouns: tyres; car; tyre position; tyre pressure and tyre tread depth; tyre readings; history of readings; current readings

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class Tyre:
    def __init__(self, pressure, tread_depth):
        self.pressure = pressure # INT
        self.tread_depth = tread_depth # INT

class Car:
    def __init__(self, tyre_front_left, tyre_front_right, tyre_back_left, tyre_back_right):
        self.front_left = # a Tyre instance
        self.front_right = # a Tyre instance
        self.back_left = # a Tyre instance
        self.back_right = # a Tyre instance
        self.readings_history = []

    def add(self, tyre, position):
        # Parameters:
        #   tyre: Tyre instance
        #   position: Car position attribute
        # Returns:
        #   Nothing
        # Side-effects
        #   Sets position attribute to new tyre
        pass # No code here yet

    def generate_tyre_report():

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
