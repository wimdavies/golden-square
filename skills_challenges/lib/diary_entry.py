import math

class DiaryEntry:
    def __init__(self, title, contents):
        if not title and not contents: raise Exception("Diary entries must contain a title or contents")
        self.title = title
        self.contents = contents
        self._chunk_bookmark = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.format().split(" "))

    def reading_time(self, wpm):
        contents_word_count = len(self._contents_words())
        return math.ceil(contents_word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        contents_words = self._contents_words()
        max_chunk_length = wpm * minutes
        if self._chunk_bookmark >= len(contents_words):
            self._chunk_bookmark = 0

        chunk_start = self._chunk_bookmark
        chunk_end = self._chunk_bookmark + max_chunk_length
        chunk = " ".join(contents_words[chunk_start:chunk_end])
        self._chunk_bookmark = chunk_end
        return chunk

    # private
    def _contents_words(self):
        return self.contents.split()
