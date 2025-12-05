from lib.task_manager import *

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
When the user requests the list, it is presented
"""
def test_formatted_list_is_provided_to_user():
    task_manager = TaskManager()
    task_manager.add_todo('Python Homework')
    task_manager.add_todo('Feed the fish')
    assert task_manager.format_todo() == "Tasks Still To Do: Python Homework, Feed the fish"