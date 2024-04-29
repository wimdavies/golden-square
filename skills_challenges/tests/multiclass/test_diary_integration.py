import pytest
from lib.multiclass.diary import Diary
from lib.multiclass.diary_entry import DiaryEntry

def test_diary_entries_returns_list_of_entry_instances():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Great day!")
    diary_entry_2 = DiaryEntry("Okay day")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.entries == [diary_entry_1, diary_entry_2]

def test_diary_entries_read_a_diary_entry_text():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Great day!")
    diary_entry_2 = DiaryEntry("Okay day")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    assert diary.entries[0].text == "Great day!"

def test_diary_entries_read_in_time_raises_if_no_entries():
    diary = Diary()
    with pytest.raises(Exception, match=r"This diary is currently empty"):
        diary.read_in_time(1, 1)

def test_diary_entries_read_in_time_returns_only_extant_entry_if_within_criteria():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Great day!")
    diary.add(diary_entry_1)
    assert diary.read_in_time(5, 1) == diary_entry_1

def test_diary_entries_read_in_time_returns_only_extant_entry_if_within_criteria():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Great day!")
    diary.add(diary_entry_1)
    assert diary.read_in_time(5, 1) == diary_entry_1

def test_diary_entries_read_in_time_returns_only_match_within_criteria():
    diary = Diary()
    diary_entry_1 = DiaryEntry("one two")
    diary_entry_2 = DiaryEntry("one two three")
    diary_entry_3 = DiaryEntry("one two three four!")
    diary.add(diary_entry_3)
    diary.add(diary_entry_2)
    diary.add(diary_entry_1)
    assert diary.read_in_time(2, 1) == diary_entry_1

def test_diary_entries_read_in_time_returns_longest_match_within_criteria():
    diary = Diary()
    diary_entry_1 = DiaryEntry("one two")
    diary_entry_2 = DiaryEntry("one two three")
    diary_entry_3 = DiaryEntry("one two three four!")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    diary.add(diary_entry_3)
    assert diary.read_in_time(3, 1) == diary_entry_2

def test_diary_entries_read_in_time_raises_if_no_entries_can_be_read_in_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Great day! And furthermore, other news.")
    diary.add(diary_entry_1)
    with pytest.raises(Exception, match=r"No entries can be read within this amount of time"):
        diary.read_in_time(1, 1)
