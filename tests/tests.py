"""Test file for TaskManager functionality"""
import sys
import os
import pytest
from unittest.mock import patch

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from main import main
from taskmanager import TaskManager

@pytest.fixture
def task_manager():
    """Fixture to create a fresh TaskManager instance for each test"""
    return TaskManager()
  
def test_task_manager_tasks_creation(task_manager):
    assert len(task_manager.tasks) == 0

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

def test_main_menu_flows():
    """Test different flows through the main menu"""
    test_scenarios = [
        # Test add task flow
        {
            'inputs': ['1', 'Test Task', 'Test Description', 'Tomorrow', '7'],
            'expected_tasks': 1
        },
        # Test add and remove flow
        {
            'inputs': [
                '1', 'Task1', 'Description1', 'Tomorrow',  # Add task
                '2', 'Task1',                             # Remove task
                '7'                                       # Exit
            ],
            'expected_tasks': 0
        },
        # Test add multiple tasks
        {
            'inputs': [
                '1', 'Task1', 'Description1', 'Tomorrow',  # Add first task
                '1', 'Task2', 'Description2', 'Next Week', # Add second task
                '7'                                        # Exit
            ],
            'expected_tasks': 2
        },
        # Test add and mark complete
        {
            'inputs': [
                '1', 'Task1', 'Description1', 'Tomorrow',  # Add task
                '5', 'Task1',                             # Mark complete
                '7'                                       # Exit
            ],
            'expected_tasks': 1,
            'check_status': 'Completed'
        },
        # Test add and edit
        {
            'inputs': [
                '1', 'Task1', 'Description1', 'Tomorrow',           # Add task
                '4', 'Task1', 'EditedTask', 'NewDesc', 'NextWeek', # Edit task
                '7'                                                 # Exit
            ],
            'expected_tasks': 1,
            'check_title': 'EditedTask'
        },
        # Test view tasks (just verifying it doesn't crash)
        {
            'inputs': [
                '1', 'Task1', 'Description1', 'Tomorrow',  # Add task
                '3',                                      # View tasks
                '7'                                       # Exit
            ],
            'expected_tasks': 1
        },
        # Test filter tasks
        {
            'inputs': [
                '1', 'Task1', 'Description1', 'Tomorrow',  # Add task
                '6', 'Pending',                           # Filter by pending
                '7'                                       # Exit
            ],
            'expected_tasks': 1
        },
        # Test invalid input handling
        {
            'inputs': [
                'invalid',                                # Invalid choice
                '1', 'Task1', 'Description1', 'Tomorrow', # Add valid task
                '7'                                       # Exit
            ],
            'expected_tasks': 1,
            'expect_error': True
        }
    ]

    for scenario in test_scenarios:
        # Create a TaskManager instance
        task_manager = TaskManager()
        
        # Mock both the TaskManager creation and the input
        with patch('main.TaskManager', return_value=task_manager), \
             patch('builtins.input', side_effect=scenario['inputs']), \
             patch('builtins.print') as mock_print:
            try:
                main()
            except SystemExit:
                pass  # Expected exit

            if 'expected_tasks' in scenario:
                assert len(task_manager.tasks) == scenario['expected_tasks']
            
            if 'check_status' in scenario:
                assert task_manager.tasks[0].status == scenario['check_status']
            
            if 'check_title' in scenario:
                assert task_manager.tasks[0].title == scenario['check_title']
            
            if 'expect_error' in scenario and scenario['expect_error']:
                mock_print.assert_any_call("Invalid choice, please try again.")