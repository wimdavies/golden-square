import pytest
from unittest.mock import Mock
from lib.music_library import MusicLibrary

def test_music_library_init_with_empty_tracks():
    assert MusicLibrary().tracks == []

def test_unit_music_library_search_returns_empty_when_no_tracks():
    assert MusicLibrary().search("Prince") == []

def test_unit_music_library_search_raises_for_empty_string():
    music_library = MusicLibrary()
    with pytest.raises(ValueError, match=r"Search string cannot be empty"):
        music_library.search("")

def test_unit_music_library_search_calls_track_matches_with_keyword():
    music_library = MusicLibrary()
    fake_track = Mock()
    music_library.add(fake_track)
    music_library.search("Prince")
    fake_track.matches.assert_called_with("Prince")

def test_unit_music_library_search_returns_single_track_that_matches_artist():
    music_library = MusicLibrary()
    fake_track = Mock()
    fake_track.matches.return_value = True
    music_library.add(fake_track)
    assert music_library.search("Prince") == [fake_track]

def test_unit_music_library_search_returns_empty_when_no_matches_artist():
    music_library = MusicLibrary()
    fake_track_1 = Mock()
    fake_track_1.matches.return_value = False
    fake_track_2 = Mock()
    fake_track_2.matches.return_value = False
    music_library.add(fake_track_1)
    music_library.add(fake_track_2)
    assert music_library.search("Prince") == []

def test_unit_music_library_search_returns_multiple_tracks_when_multiple_matches():
    music_library = MusicLibrary()
    fake_track_1 = Mock()
    fake_track_1.matches.return_value = True
    fake_track_2 = Mock()
    fake_track_2.matches.return_value = True
    fake_track_3 = Mock()
    fake_track_3.matches.return_value = True
    music_library.add(fake_track_1)
    music_library.add(fake_track_2)
    music_library.add(fake_track_3)
    assert music_library.search("Prince") == [fake_track_1, fake_track_2, fake_track_3]