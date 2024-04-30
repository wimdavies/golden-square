class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def search(self, keyword):
        if not keyword: raise ValueError("Search string cannot be empty")
        return [track for track in self.tracks if track.matches(keyword)]
