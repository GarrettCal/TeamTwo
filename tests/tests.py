"""Test file for TaskManager functionality"""
import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from taskmanager import TaskManager

@pytest.fixture
def task_manager():
    """Fixture to create a fresh TaskManager instance for each test"""
    return TaskManager()

def test_add_task(task_manager):
    """Test adding a task"""
    task_manager.add_task("Task 1", "This is task 1", "Tomorrow")
    assert len(task_manager.tasks) == 1

def test_remove_task(task_manager):
    """Test removing a task"""
    task_manager.add_task("Remove Task", "This is Remove Task", "Tomorrow")
    task_manager.remove_task("Remove Task")
    assert len(task_manager.tasks) == 0

def test_edit_task(task_manager):
    """Test editing a task"""
    task_manager.add_task("Edit task", "This is Edit Task", "Tomorrow")
    task_manager.edit_task("Edit task", "New Edit Task", "This is the new edit task", "Never")
    assert any(task.title == "New Edit Task" for task in task_manager.tasks)

def test_mark_complete(task_manager):
    """Test marking a task as complete"""
    task_manager.add_task("Edit task", "This is Edit Task", "Tomorrow")
    task_manager.mark_complete("Edit task")
    assert task_manager.tasks[0].status == "Completed"

def test_task_lifecycle(task_manager):
    """Test the complete lifecycle of a task: add, edit, and remove"""
    task_manager.add_task("Task 1", "Initial description", "Tomorrow")
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Task 1"
    
    task_manager.edit_task("Task 1", "Updated Task", "New description", "Next week")
    assert any(task.title == "Updated Task" for task in task_manager.tasks)
    assert task_manager.tasks[0].description == "New description"
    assert task_manager.tasks[0].due_date == "Next week"
    
    task_manager.remove_task("Updated Task")
    assert len(task_manager.tasks) == 0
