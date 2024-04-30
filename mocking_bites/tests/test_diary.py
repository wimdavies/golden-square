from lib.diary import Diary

def test_diary_read_returns_contents():
    diary = Diary("Great day!")
    assert diary.read() == "Great day!"
