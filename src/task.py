class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.id = id(self)
        self.status = "Pending"

    def __str__(self):
        return f"Tsk ID:{self.id}\nTitle: {self.title}\nStatus: {self.status}\nDue Date: {self.due_date}"


#override string method for printable

