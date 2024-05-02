from lib.listening_library import ListeningLibrary

"""
init with empty list
"""
def test_init_with_empty_list():
    listening_library = ListeningLibrary()
    assert listening_library.tracks == []

"""
all returns empty tracks when no tracks added
"""
def test_all_returns_empty_tracks_when_no_tracks_added():
    listening_library = ListeningLibrary()
    assert listening_library.all() == []

"""
add adds a single track to tracks
"""
def test_add_adds_a_single_track_to_tracks():
    listening_library = ListeningLibrary()
    listening_library.add({"title": "1999", "artist": "Prince"})
    assert listening_library.all() == [{"title": "1999", "artist": "Prince"}]

"""
add adds multiple tracks to tracks
"""
def test_add_adds_multiple_tracks_to_tracks():
    listening_library = ListeningLibrary()
    listening_library.add({"title": "1999", "artist": "Prince"})
    listening_library.add({"title": "Purple Rain", "artist": "Prince"})
    assert listening_library.all() == [{"title": "1999", "artist": "Prince"}, {"title": "Purple Rain", "artist": "Prince"}]
