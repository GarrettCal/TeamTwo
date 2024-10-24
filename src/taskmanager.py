from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task, description, due_date):
        self.tasks.append(Task(task, description, due_date))

    def remove_task(self, task):
        for t in self.tasks:
            if t.id == task:
                self.tasks.remove(t)
                break

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def filter(self, task_status):
        for t in self.tasks:
            if t.status == task_status:
                print(t)

    def find_task(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                return t
        return None