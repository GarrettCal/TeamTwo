from taskmanager import TaskManager
from task import Task

def main():
    task_manager = TaskManager()
    print("Welcome to the task management system")
    while True:
        print("Please choose an option: 1. Add Task 2. Remove Task 3. View Tasks 4. Edit Task 5. Mark As Completed 6. Filter 7. Quit")
        choice = input()
        
        if choice == '1':
            task = input("Enter the task to add: ")
            description = input("Enter a description: ")
            due_date = input("Enter a due date: ")
            task_manager.add_task(task, description, due_date)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            task_manager.remove_task(task)
        elif choice == '3':
            task_manager.view_tasks()
        elif choice == '4':
            task = input("Enter task to change: ")
            new_name = input("Enter a new task name: ")
            new_description = input("Enter a new description: ")
            new_due_date = input("Enter a new due date: ")
            task_manager.edit_task(task, new_name, new_description, new_due_date)
        elif choice == '5':
            task = input("Enter completed task name: ")
            task_manager.mark_complete(task)
        elif choice == '6':
            status = input("Status to filter by (Pending or Completed): ")
            task_manager.filter(status)
        elif choice == '7':
            exit()
        else:
            print("Invalid choice, please try again.")
            

if __name__ == "__main__":
    main()
