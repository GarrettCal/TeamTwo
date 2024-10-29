from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task, description, due_date):
        self.tasks.append(Task(task, description, due_date))

    def remove_task(self, task):
        for t in self.tasks:
            if t.title == task:
                self.tasks.remove(t)
                break

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def filter(self, task_status):
        filtered_array = []
        for i in range(len(self.tasks)):
            if self.tasks[i].status == task_status:
                filtered_array.append(self.tasks[i])
        for i in range(len(filtered_array)):
            print(filtered_array[i])
    
    def edit_task(self, task, new_name, new_description, new_due_date):
        for i in range(len(self.tasks)):
            if self.tasks[i].title == task:
                self.tasks[i].title = new_name
                self.tasks[i].description = new_description
                self.tasks[i].due_date = new_due_date
                
    def mark_complete(self, task):
        for i in range(len(self.tasks)):
            if self.tasks[i].title == task:
                self.tasks[i].status = "Completed"