class TaskTracker:
    def __init__(self) -> None:
        self._tasks = []

    def list_incomplete(self):
        return self._tasks
    
    def add(self, task):
        if type(task) is not str: raise TypeError("A valid task can only be a string")
        self._tasks.append(task)

    def mark_complete(self, index):
        if index < 0 or index >= len(self._tasks): raise Exception("No task exists at that index")
        del self._tasks[index]