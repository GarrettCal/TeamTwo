from taskmanager import TaskManager

def main():
    task_manager = TaskManager()
    print("Welcome to the task management system")
    print("Please choose an option: 1. Add Task 2. Remove Task 3. View Tasks 4. Exit")
    choice = input()
    if choice == '1':
        task_manager.add_task()
    elif choice == '2':
        task_manager.remove_task()
    elif choice == '3':
        task_manager.view_tasks()
    elif choice == '4':
        exit()
    else:
        print("Invalid choice, please try again.")
        main()

if __name__ == "__main__":
    main()