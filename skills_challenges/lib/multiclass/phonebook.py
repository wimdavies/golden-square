import re

class Phonebook:
    UK_PHONE_REGEX = r"0\d{10}"

    def __init__(self, diary):
        self.diary = diary

    def get_numbers(self):
        all_numbers =  [number for entry in self.diary.entries for number in re.findall(self.UK_PHONE_REGEX, entry.text)]
        unique_numbers = list(dict.fromkeys(all_numbers))
        return unique_numbers
