from taskmanager import TaskManager

def main():
    task_manager = TaskManager()
    print("Welcome to the task management system")
    while True:
        print("Please choose an option: 1. Add Task 2. Remove Task 3. View Tasks 4. Edit Task 5. Mark As Completed 6. Exit")
        choice = input()
        if choice == '1':
            task = input("Enter the task to add: ")
            task_manager.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            task_manager.remove_task(task)
        elif choice == '3':
            task_manager.view_tasks()
        elif choice == '4':
            new_name = input("Enter a new task name: ")
            task.edit_task(new_name)
        elif choice = '5'
            task.mark_completed()
        elif choice == '6'
            exit()
        else:
            print("Invalid choice, please try again.")
            

if __name__ == "__main__":
    main()
