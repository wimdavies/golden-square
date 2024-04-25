# Task tracker Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

>As a user
>So that I can keep track of my tasks
>I want a program that I can add todo tasks to and see a list of them.

>As a user
>So that I can focus on tasks to complete
>I want to mark tasks as complete and have them disappear from the list.

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class TaskTracker:    
    def __init__(self):
        #   tasks: list of strings
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self tasks lists
        pass # No code here yet

    def list_tasks(self):
        # Returns:
        #   The list of tasks to do
        pass # No code here yet

    def mark_complete(index):
        # params:
        #   index of task to mark as complete
        #  returns:
        #   nothing
        # Side effects:
        #   removes the task at `index` from the self list of tasks
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
init with no tasks, list returns empty
"""
task_tracker = TaskTracker()
task_tracker.list_incomplete() # => []

"""
Adding task that is not a string
raises error
"""
task_tracker = TaskTracker()
task_tracker.add(42) # => raises TypeError "A valid task can only be a string"
task_tracker.add([]) # => raises TypeError "A valid task can only be a string"
task_tracker.add(None) # => raises TypeError "A valid task can only be a string"

"""
Adding a single task
list_incomplete returns list of that task
"""
task_tracker = TaskTracker()
task_tracker.add("Walk the dog")
task_tracker.list_incomplete() # => ["Walk the dog"]

"""
Adding multiple tasks
list_incomplete returns list of those tasks
"""
task_tracker = TaskTracker()
task_tracker.add("Walk the dog")
task_tracker.add("Stroke the cat")
task_tracker.list_incomplete() # => ["Walk the dog", "Stroke the cat"]

"""
With single task marked complete
list_incomplete returns list of remaining tasks
"""
task_tracker = TaskTracker()
task_tracker.add("Walk the dog")
task_tracker.add("Stroke the cat")
task_tracker.add("Wash the car")
task_tracker.mark_complete(1)
task_tracker.list_incomplete() # => ["Walk the dog", "Wash the car"]

"""
With multiple task marked complete
list_incomplete returns list of remaining tasks
"""
task_tracker = TaskTracker()
task_tracker.add("Walk the dog")
task_tracker.add("Stroke the cat")
task_tracker.add("Wash the car")
task_tracker.mark_complete(0)
task_tracker.mark_complete(0)
task_tracker.list_incomplete() # => ["Wash the car"]

"""
Attempting to mark index (too low) complete
raises error
"""
task_tracker = TaskTracker()
task_tracker.add("Walk the dog")
task_tracker.add("Stroke the cat")
task_tracker.add("Wash the car")
task_tracker.mark_complete(-4)  # => raises Exception "No task exists at that index"
task_tracker.list_incomplete() # => ["Walk the dog", "Stroke the cat", "Wash the car"]

"""
Attempting to mark index (too high) complete
raises error
"""
task_tracker = TaskTracker()
task_tracker.add("Walk the dog")
task_tracker.mark_complete(4) # => raises Exception "No task exists at that index"
task_tracker.list_incomplete() # => ["Walk the dog", "Stroke the cat", "Wash the car"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
