class TodoList:
    def __init__(self):
        self._storage = []

    def add(self, todo):
        self._storage.append(todo)

    def incomplete(self):
        return [todo for todo in self._storage if not todo.complete]

    def complete(self):
        return [todo for todo in self._storage if todo.complete]

    def give_up(self):
        for todo in self._storage:
            todo.mark_complete()
