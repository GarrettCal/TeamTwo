"""this will be a test file"""
from src.task import Task
from src.taskmanager import TaskManager

task_manager = TaskManager()

#adding task test 1
task_manager.add("Task 1", "This is task 1", "Tomorrow")
if len(task_manager.tasks) == 1:
  print("Add task 1 Passed")
else:
  print("Add task 1 Failed")
task_manager.remove("Task 1")

#removing task test 1
task_manager.add("Remove Task", "This is Remove Task", "Tomorrow")
task_manager.remove("Remove Task")
if len(task_manager.tasks) == 0:
  print("Remove test 1 passed")
else:
  print("Remove test 1 failed")

#editting task test 1
task_manager.add("Edit task", "This is Edit Task", "Tomorrow")
