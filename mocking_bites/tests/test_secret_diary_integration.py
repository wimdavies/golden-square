from lib.secret_diary import SecretDiary
from lib.diary import Diary

def test_secret_diary_read_returns_go_away_initially():
    diary = Diary("Great day!")
    secret_diary = SecretDiary(diary)
    assert secret_diary.read() == "Go away!"

def test_secret_diary_read_returns_contents_once_unlocked():
    diary = Diary("Great day!")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Great day!"

def test_secret_diary_read_returns_go_away_when_relocked():
    diary = Diary("Great day!")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.read() == "Go away!"
