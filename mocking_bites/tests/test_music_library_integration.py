from lib.music_library import MusicLibrary
from lib.track import Track

def test_music_library_adds_track_to_tracks():
    music_library = MusicLibrary()
    track_1 = Track("1999", "Prince")
    music_library.add(track_1)
    assert music_library.tracks == [track_1]

def test_music_library_adds_multiple_tracks_to_tracks():
    music_library = MusicLibrary()
    track_1 = Track("1999", "Prince")
    track_2 = Track("Creep", "Radiohead")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.tracks == [track_1, track_2]

def test_music_library_adds_multiple_tracks_to_tracks():
    music_library = MusicLibrary()
    track_1 = Track("1999", "Prince")
    track_2 = Track("Creep", "Radiohead")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.tracks == [track_1, track_2]

def test_music_library_search_returns_empty_list_for_no_matches():
    music_library = MusicLibrary()
    track_1 = Track("1999", "Prince")
    track_2 = Track("Creep", "Radiohead")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search("Spice Girls") == []

def test_music_library_search_returns_single_track_that_matches_artist():
    music_library = MusicLibrary()
    track_1 = Track("1999", "Prince")
    track_2 = Track("Creep", "Radiohead")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search("Prince") == [track_1]

def test_music_library_search_returns_all_tracks_that_match_artist():
    music_library = MusicLibrary()
    track_1 = Track("1999", "Prince")
    track_2 = Track("Purple Rain", "Prince")
    track_3 = Track("Creep", "Radiohead")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("Prince") == [track_1, track_2]

def test_music_library_search_returns_all_tracks_that_match_title():
    music_library = MusicLibrary()
    track_1 = Track("1999", "Prince")
    track_2 = Track("Purple Rain", "Prince")
    track_3 = Track("Purple Rain", "Radiohead")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("Purple Rain") == [track_2, track_3]

def test_music_library_search_returns_tracks_that_match_title_or_artist():
    music_library = MusicLibrary()
    track_1 = Track("1999", "Prince")
    track_2 = Track("I love years", "1999")
    track_3 = Track("Purple Rain", "Radiohead")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("1999") == [track_1, track_2]

def test_music_library_search_returns_tracks_that_match_partials():
    music_library = MusicLibrary()
    track_1 = Track("1999", "Prince")
    track_2 = Track("Falconry", "Princely Pursuits")
    track_3 = Track("Purple Rain", "Radiohead")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("Prince") == [track_1, track_2]
