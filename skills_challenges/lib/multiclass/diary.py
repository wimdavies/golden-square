import math

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, diary_entry):
        self.entries.append(diary_entry)

    def read_in_time(self, wpm, minutes):
        if not self.entries: raise Exception("This diary is currently empty")
        readable_entries = [entry for entry in self.entries if self._readable_in_time(entry, wpm, minutes)]
        if not readable_entries: 
            raise Exception("No entries can be read within this amount of time")
        else:
            return max(readable_entries, key=lambda entry: self._word_count(entry))

    def _readable_in_time(self, entry, wpm, minutes):
        return math.ceil(self._word_count(entry) / wpm) <= minutes
    
    def _word_count(self, entry):
        return len(entry.text.split(" "))