class Task:
    def __init__(self, task):
        self.task = task
        self.id = id(self)
        self.status = "Pending"

    def edit_task(self, new_name):
        self.task = new_name

    def mark_complete(self):
        pass

    def __str__(self):
        return f"Tsk ID:{self.id}\nTask: {self.task}\nStatus: {self.status}"


#override string method for printable

