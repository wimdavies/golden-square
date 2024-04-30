class SecretDiary:
    def __init__(self, diary):
        self.diary = diary
        self.locked = True

    def read(self):
        return "Go away!" if self.locked else self.diary.read()

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False
