class TaskFormatter:
    def __init__(self, task):
        self.task = task

    def format(self):
        return f"- [x] {self.task.title}" if  self.task.is_complete() else f"- [ ] {self.task.title}"
