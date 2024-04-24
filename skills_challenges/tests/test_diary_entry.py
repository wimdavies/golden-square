import pytest
from lib.diary_entry import DiaryEntry

@pytest.fixture
def basic_diary_entry():
    return DiaryEntry("Another day in Paradise", "Dear Diary, today I went to the zoo. It was mega.")

def test_init_with_title_and_contents(basic_diary_entry):
    assert basic_diary_entry.title == "Another day in Paradise"
    assert basic_diary_entry.contents == "Dear Diary, today I went to the zoo. It was mega."

def test_count_words_raises_for_empty_strings_diary_entry():
    with pytest.raises(Exception, match=r"Diary entries must contain a title or contents"):
        DiaryEntry("", "")

def test_format_returns_formatted_string_of_title_and_contents(basic_diary_entry):
    assert basic_diary_entry.format() == "Another day in Paradise: Dear Diary, today I went to the zoo. It was mega."

def test_count_words_returns_15_for_the_basic_diary_entry_example(basic_diary_entry):
    assert basic_diary_entry.count_words() == 15

def test_reading_time_for_200_word_contents_given_200_wpm_returns_1():
    diary_entry = DiaryEntry("yo", ("yo " * 200))
    assert diary_entry.reading_time(200) == 1

def test_reading_time_for_200_word_contents_given_100_wpm_returns_2():
    diary_entry = DiaryEntry("yo", ("yo " * 200))
    assert diary_entry.reading_time(100) == 2

def test_reading_time_for_150_word_contents_given_100_wpm__ceils_result_and_returns_2():
    diary_entry = DiaryEntry("yo", ("yo " * 150))
    assert diary_entry.reading_time(100) == 2

def test_reading_chunk_given_10_wpm_and_1_minute_and_contents_10_returns_whole_contents():
    contents = "one two three four five six seven eight nine ten"
    diary_entry = DiaryEntry("yo", (contents))
    chunk = diary_entry.reading_chunk(10, 1)
    assert chunk == contents

def test_reading_chunk_given_5_wpm_and_1_minute_and_contents_10_returns_chunk_of_first_five_contents():
    contents = "one two three four five six seven eight nine ten"
    diary_entry = DiaryEntry("yo", (contents))
    chunk = diary_entry.reading_chunk(5, 1)
    assert chunk == "one two three four five"

def test_reading_chunk_next_call_given_5_wpm_and_1_minute_and_contents_10_returns_chunk_of_remaining_five_contents():
    contents = "one two three four five six seven eight nine ten"
    diary_entry = DiaryEntry("yo", (contents))
    first_chunk = diary_entry.reading_chunk(5, 1)
    next_chunk = diary_entry.reading_chunk(5, 1)
    assert first_chunk == "one two three four five"
    assert next_chunk == "six seven eight nine ten"

def test_reading_chunk_next_call_given_5_wpm_and_1_minute_and_contents_12_returns_chunk_of_next_five_contents():
    contents = "one two three four five six seven eight nine ten eleven twelve"
    diary_entry = DiaryEntry("yo", (contents))
    first_chunk = diary_entry.reading_chunk(5, 1)
    next_chunk = diary_entry.reading_chunk(5, 1)
    assert first_chunk == "one two three four five"
    assert next_chunk == "six seven eight nine ten"

def test_reading_chunk_next_call_given_5_wpm_and_1_minute_and_contents_8_returns_chunk_of_remaining_three_contents():
    contents = "one two three four five six seven eight"
    diary_entry = DiaryEntry("yo", (contents))
    first_chunk = diary_entry.reading_chunk(5, 1)
    next_chunk = diary_entry.reading_chunk(5, 1)
    assert first_chunk == "one two three four five"
    assert next_chunk == "six seven eight"

def test_reading_chunk_subsequent_calls_given_2_wpm_and_1_minute_and_contents_10_returns_each_chunk_of_two_contents():
    contents = "one two three four five six seven eight nine ten"
    diary_entry = DiaryEntry("yo", (contents))
    assert diary_entry.reading_chunk(2, 1) == "one two"
    assert diary_entry.reading_chunk(2, 1) == "three four"
    assert diary_entry.reading_chunk(2, 1) == "five six"
    assert diary_entry.reading_chunk(2, 1) == "seven eight"
    assert diary_entry.reading_chunk(2, 1) == "nine ten"

def test_reading_chunk_subsequent_call_given_5_wpm_and_1_minute_and_contents_10_restarts_and_returns_first_chunk_contents():
    contents = "one two three four five six seven eight nine ten"
    diary_entry = DiaryEntry("yo", (contents))
    diary_entry.reading_chunk(5, 1)
    diary_entry.reading_chunk(5, 1)
    subsequent_chunk = diary_entry.reading_chunk(5, 1)
    assert subsequent_chunk == "one two three four five"

def test_reading_chunk_restart_behaviour_handles_variable_wpm_and_time():
    contents = "one two three four five six seven eight nine ten"
    diary_entry = DiaryEntry("yo", (contents))
    assert diary_entry.reading_chunk(2, 2) == "one two three four"
    assert diary_entry.reading_chunk(5, 1) == "five six seven eight nine"
    assert diary_entry.reading_chunk(3, 1) ==  "ten"
    assert diary_entry.reading_chunk(2, 1) == "one two"
