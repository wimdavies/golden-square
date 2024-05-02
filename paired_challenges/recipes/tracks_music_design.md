# Tracks / Music listening Class Design Recipe

## 1. Describe the Problem

>As a user
>So that I can *keep track* of my **music listening**
>I want to add **tracks** I've listened to and *see* a **list** of them.

Verbs: keep track, add, see
Nouns: tracks, list (of tracks), music listening

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class ListeningLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        # track is a dictionary with keys "title" and "artist"
        # no return
        # side effect: adds track to tracks

    def all(self):
        # returns tracks
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
init with empty list
"""
listening_library = ListeningLibrary()
listening_library.tracks == []

"""
all returns empty tracks when no tracks added
"""
listening_library = ListeningLibrary()
listening_library.all() == []

"""
add adds a single track to tracks
"""
listening_library = ListeningLibrary()
listening_library.add({"title": "1999", "artist": "Prince"})
listening_library.all() == [{"title": "1999", "artist": "Prince"}]

"""
add adds multiple tracks to tracks
"""
listening_library = ListeningLibrary()
listening_library.add({"title": "1999", "artist": "Prince"})
listening_library.add({"title": "Purple Rain", "artist": "Prince"})
listening_library.all() == [{"title": "1999", "artist": "Prince"}, {"title": "Purple Rain", "artist": "Prince"}]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
