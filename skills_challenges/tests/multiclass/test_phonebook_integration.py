from lib.multiclass.phonebook import Phonebook
from lib.multiclass.diary import Diary
from lib.multiclass.diary_entry import DiaryEntry

def test_phonebook_get_numbers_returns_empty_list_when_no_entries_in_diary():
    phonebook = Phonebook(Diary())
    assert phonebook.get_numbers() == []

def test_phonebook_get_numbers_returns_empty_list_when_no_numbers_in_entries_in_diary():
    diary = Diary()
    diary.add(DiaryEntry("Great day!"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == []

def test_phonebook_get_numbers_returns_empty_list_when_invalid_number_in_entries_in_diary():
    diary = Diary()
    diary.add(DiaryEntry("not a valid number 1234567891"))
    diary.add(DiaryEntry("no number here"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == []

def test_phonebook_get_numbers_returns_list_with_number_when_one_number_in_one_entry_in_diary():
    diary = Diary()
    diary.add(DiaryEntry("01234567891"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == ["01234567891"]

def test_phonebook_get_numbers_returns_list_with_number_when_one_number_and_other_text_in_one_entry_in_diary():
    diary = Diary()
    diary.add(DiaryEntry("Friend's number is: 01234567891"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == ["01234567891"]

def test_phonebook_get_numbers_returns_list_with_numbers_when_two_numbers_in_one_entry_in_diary():
    diary = Diary()
    diary.add(DiaryEntry("01234567891, 02234567891"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == ["01234567891", "02234567891"]

def test_phonebook_get_numbers_returns_list_with_numbers_when_two_numbers_across_two_entries_in_diary():
    diary = Diary()
    diary.add(DiaryEntry("01234567891"))
    diary.add(DiaryEntry("02234567891"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == ["01234567891", "02234567891"]

def test_phonebook_get_numbers_returns_list_with_numbers_when_mishmash_entries_in_diary():
    diary = Diary()
    diary.add(DiaryEntry("0123fdsdsffd4567891"))
    diary.add(DiaryEntry("0123456789102234567891"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == ["01234567891", "02234567891"]

def test_phonebook_get_numbers_returns_list_with_unique_number_when_number_repeated_in_one_entry_diary():
    diary = Diary()
    diary.add(DiaryEntry("Friend's number is: 01234567891. I repeat: 01234567891"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == ["01234567891"]

def test_phonebook_get_numbers_returns_list_with_unique_number_when_number_repeated_across_entries_diary():
    diary = Diary()
    diary.add(DiaryEntry("Friend's number is: 01234567891"))
    diary.add(DiaryEntry("Friend's number is still: 01234567891"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == ["01234567891"]

def test_phonebook_get_numbers_returns_list_with_unique_numbers_when_number_repeated_across_entries_diary():
    diary = Diary()
    diary.add(DiaryEntry("Friend's number is: 01234567891. Other friend's number: 02234567891"))
    diary.add(DiaryEntry("Still 01234567891 and 02234567891"))
    phonebook = Phonebook(diary)
    assert phonebook.get_numbers() == ["01234567891", "02234567891"]