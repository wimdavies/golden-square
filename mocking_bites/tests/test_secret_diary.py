from lib.secret_diary import SecretDiary
from unittest.mock import Mock

def test_secret_diary_read_returns_go_away_initially():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    assert secret_diary.read() == "Go away!"

def test_secret_diary_read_returns_contents_once_unlocked():
    fake_diary = Mock()
    fake_diary.read.return_value = "Great day!"
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Great day!"
    fake_diary.read.assert_called_once()

def test_secret_diary_read_returns_go_away_when_relocked():
    fake_diary = Mock()
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.read() == "Go away!"
