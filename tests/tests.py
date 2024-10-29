"""this will be a test file"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from taskmanager import TaskManager

task_manager = TaskManager()

#adding task test 1
task_manager.add_task("Task 1", "This is task 1", "Tomorrow")
if len(task_manager.tasks) == 1:
  print("Add task 1 Passed")
else:
  print("Add task 1 Failed")
task_manager.remove_task("Task 1")

#removing task test 1
task_manager.add_task("Remove Task", "This is Remove Task", "Tomorrow")
task_manager.remove_task("Remove Task")
if len(task_manager.tasks) == 0:
  print("Remove test 1 passed")
else:
  print("Remove test 1 failed")

#editting task test 1
task_manager.add_task("Edit task", "This is Edit Task", "Tomorrow")
task_manager.edit_task("Edit task", "New Edit Task", "This is the new edit task", "Never")
if task_manager.find_task("New Edit Task"):
  print("Edit task test 1 passed")
else:
  print("Edit task test 1 failed")
task_manager.remove_task("New Edit Task")

#mark complete test 1
task_manager.add_task("Edit task", "This is Edit Task", "Tomorrow")
task_manager.mark_complete("Edit task")
if task_manager.tasks[0].status == "Completed":
  print("Mark complete test 1 passed")
else:
  print("Mark complete test 1 failed")
