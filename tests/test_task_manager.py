from lib.task_manager import *
import pytest

"""
When the user creates a new TaskManager, 
it instntiates with an empty list 
"""
def test_task_manager_instantiates(): 
    task_manager = TaskManager()
    assert task_manager.todo_list == []

"""
When the user adds a new task, it is stored in the list
"""
def test_adds_new_task_to_todo_list():
    task_manager = TaskManager()
    task_manager.add_todo('Python Homework')
    assert task_manager.todo_list == ['Python Homework']

"""
When the user adds multiple new task, it is stored in the list
"""
def test_adds_multiple_new_tasks_to_todo_list():
    task_manager = TaskManager()
    task_manager.add_todo('Python Homework')
    task_manager.add_todo('Feed the fish')
    assert task_manager.todo_list == ['Python Homework', 'Feed the fish']

"""
If user trys to add an empty task, 
raises a error "You have not added a Task!"
"""
def test_empty_task_raises_error():
    task_manager = TaskManager()
    with pytest.raises(ValueError) as e:
        task_manager.add_todo("")
    assert str(e.value) == "You have not added a Task!"

"""
If user trys to add an integer, 
raises a error "You have not added a Task!"
"""
def test_empty_task_raises_error():
    task_manager = TaskManager()
    with pytest.raises(TypeError) as e:
        task_manager.add_todo(1234)
    assert str(e.value) == "Not a valid Task!"

"""
When the user requests the list, it is presented
"""
def test_formatted_list_is_provided_to_user():
    task_manager = TaskManager()
    task_manager.add_todo('Python Homework')
    task_manager.add_todo('Feed the fish')
    assert task_manager.format_todo() == "Tasks Still To Do: Python Homework, Feed the fish"

"""
When the user completes a task, 
it is removed from the todo list
"""

def test_remove_completed_task_from_to_do():
    task_manager = TaskManager()
    task_manager.add_todo('Python Homework')
    task_manager.add_todo('Feed the fish')
    task_manager.completed_task("Python Homework")
    assert task_manager.format_todo() == "Tasks Still To Do: Feed the fish"

"""
When the user completes a task
it is added to completed list
"""

def test_completed_task_is_added_to_completed_list():
    pass

