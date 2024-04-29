class Todo:
    def __init__(self, task):
        if type(task) is not str: raise TypeError("Task must be a string")
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True
