from lib.track import Track

def test_track_init_with_title_and_artist():
    track = Track("1999", "Prince")
    assert track.title == "1999"
    assert track.artist == "Prince"

def test_track_matches_keyword_with_title_True():
    track = Track("1999", "Prince")
    assert track.matches("1999") == True

def test_track_matches_keyword_with_title_False():
    track = Track("1999", "Prince")
    assert track.matches("Purple Rain") == False

def test_track_matches_keyword_in_title_True():
    track = Track("Purple Rain (Donkey Remix)", "Prince")
    assert track.matches("Purple Rain") == True

def test_track_matches_keyword_with_artist_True():
    track = Track("1999", "Prince")
    assert track.matches("Prince") == True

def test_track_matches_keyword_with_artist_False():
    track = Track("1999", "Prince")
    assert track.matches("Radiohead") == False

def test_track_matches_keyword_in_artist_True():
    track = Track("Falconry", "Princely Pursuits")
    assert track.matches("Prince") == True

