# Diary Multi-Class Planned Design

## 1. Describe the Problem

>As a user
>So that I can *record* my **experiences**
>I want to *keep* a regular **diary**
>
>As a user
>So that I can *reflect* on my experiences
>I want to *read* my past **diary entries**
>
>As a user
>So that I can *reflect* on my experiences in my busy day
>I want to *select* **diary entries** to *read* based on how much **time** I have and my **reading speed**
>
>As a user
>So that I can *keep track* of my **tasks**
>I want to *keep* a **todo list** along with my **diary**
>
>As a user
>So that I can *keep track* of my **contacts**
>I want to *see* a **list** of all of the mobile **phone numbers** in all my **diary entries**

- add todos, read from list of todos, mark todos as complete, see complete and incomplete todos
- add diary entries, select a diary entry to read, return the longest entry that can be read within the time@wpm 
- search diary entries for strings matching phone numbers (11 digits, starting 0), view list of these. Unique only?

## 2. Design the Class System

```text
 ┌────────────────────┐                    ┌───────────────────────┐
 │Phonebook(diary)    │                    │TodoList               │
 │                    │                    │                       │
 │-diary              │                    │-tasks                 │
 │                    │                    │                       │
 │-numbers()          │                    │-add(todo)             │
 │  => list of unique │                    │                       │
 │  numbers extracted │                    │-all                   │
 │  from diary entries│                    │ => list of todo       │
 └──┬─────────────────┘                    │    instances          │
    │has one Diary                         │                       │
    │                                      │-complete              │
 ┌──▼──────────────────────┐               │ => list of completed  │
 │ Diary                   │               │                       │
 │                         │               │-incomplete            │
 │ -entries                │               │ => list of incomplete │
 │                         │               └─┬─────────────────────┘
 │ -add(diary_entry)       │                 │has list of           
 │                         │                 │                      
 │ -list                   │               ┌─▼────────────────────┐ 
 │   => list of diary_entry│               │Todo                  │ 
 │       instances         │               │                      │ 
 │                         │               │-task                 │ 
 │ -read_in_time(wpm, time)│               │-status               │ 
 │   => the diary_entry    │               │                      │ 
 │    readable in the time │               │-mark_complete        │ 
 └──┬──────────────────────┘               │  sets status to True │ 
    │has list of                           └──────────────────────┘ 
    │                                                               
 ┌──▼────────┐                                                      
 │DiaryEntry │                                                      
 │           │                                                      
 │-text      │                                                      
 └───────────┘    
```

```python
class Phonebook:
    def __init__(diary):
        # diary is a diary instance

    def numbers(self):
        # returns: a list of unique valid phone numbers
        #    extracted from the diary_entries of diary
        pass # No code here yet

class Diary:


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
