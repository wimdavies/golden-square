# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

>As a user
>So I don't forget the details
>I want to **keep a record** of friends' *names* and *birthdates*
>
>As a user
>So I can make edits when I've got dates wrong
>I want to be able to **update** a record by passing in a *name* and *new date*
>
>As a user
>So I can make edits when people change their name
>I want to be able to **update** a record by passing in an *old* and a *new name*
>
>As a user
>So I can remember to send *birthday cards* at the right time
>I want to be able to **list** *friends* whose *birthdays* are *coming up soon* and to whom I need to send a card
>
>As a user
>So I can buy age-appropriate birthday cards
>I want to **calculate** the *upcoming* *ages* for friends with birthdays
>
>As a user
>So I can **keep track** of cards sent and to be sent
>I want to be able to **mark** a birthday card for a *year* as "*done*"

Verbs: keep a record; update (1 and 2); list; calculate; keep track; mark (as done)
Nouns: names, birthdays (of friends); old & new names; new (birth)date; birthday card; upcoming birthday; upcoming age (of friend, at next birthday); birthday card being "done" for the year (sent?);

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class Friend:
    def __init__(self, name, birthdate):
        # name = string
        # birthdate = string, parsed in datetime object
        # card_sent = Boolean, default False
        self.name = name
        self.birthdate = birthdate
        self.card_sent = False


class BirthdayCalendar:
    # User-facing properties:
    #   friends: list of Friend object

    def __init__(self):
        self.friends = []

    def add(self, friend):
        # Parameters:
        #   friend: Friend instance
        # Returns:
        #   Nothing
        # Side-effects
        #   Appends friend to list
        pass # No code here yet

    def update_friend_name(self, old_name, new_name):
        # side effect: updates name of friend(old_name) to new name

    def update_friend_birthday(self, name, new_birthday):
        # side effect: updates birthday of friend(name) to new birthday

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
