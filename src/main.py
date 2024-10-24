from taskmanager import TaskManager

def main():
    task_manager = TaskManager()
    print("Welcome to the task management system")
    while True:
        print("Please choose an option: 1. Add Task 2. Remove Task 3. View Tasks 4. Exit")
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
            exit()
        else:
            print("Invalid choice, please try again.")
            

if __name__ == "__main__":
    main()