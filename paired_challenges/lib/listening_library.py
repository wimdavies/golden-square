class ListeningLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def all(self):
        return self.tracks
