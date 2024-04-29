from lib.multiclass.diary_entry import DiaryEntry

def test_diary_entry_init_with_text():
    diary_entry = DiaryEntry("Today I walked.")
    assert diary_entry.text == "Today I walked."
