class Task:
    def __init__(self, task):
        self.task = task
        self.id = id(self)
        self.status = "Pending"

    def edit_task(self, new_name):
        pass

    def mark_complete(self):
        pass

