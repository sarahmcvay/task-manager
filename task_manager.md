TASK MANAGER 

User Stories / The Challenge
As a user, 
    -- In order to keep track of to-do tasks
    Require a program that adds tasks to a list and shows the list to the user

    -- In order to focus on tasks still outstanding
    Require a program that marks tasks as complete and removes them from the list

Class Signature
```python
class TaskManager():
    def __init__(self):
        """ Parameters: none
        Returns: none
        Side effects: none
        Notes: stores an empty list on the internal state: self.tasks """
        pass 

    def add_task(self, task):
        """ Parameters: task, a string
        Returns: none
        Side effects: adds the task to self.tasks list
        Notes: raises a TypeError ("You have not added a Task!") if the string is empty """
        pass

    def generate_list(self):
        """ Parameters: none
        Returns: list of the tasks to do
        Side effects: none
        Notes: raises a TypeError ("Time to relax! You have no tasks to do right now.") if the list is empty""" 
        pass

    def mark_as_complete(self):
        """ Parameters
        Side effects: moves tasks into a completed list"""

Example Tests
"""
When the user creates a new TaskManager, 
it instntiates with an empty list 
"""
task_manager = TaskManager()
assert task_manager.todo_list == []

"""
When the user adds a new task, it is stored in the list
"""
task_manager = TaskManager()
task_manager.add_todo('Python Homework')
assert task_manager.todo_list == ['Python Homework']

"""
When the user adds multiple new task, it is stored in the list
"""
task_manager = TaskManager()
task_manager.add_todo('Python Homework')
task_manager.add_todo('Walk the dog')
assert task_manager.todo_list == ['Python Homework', 'Walk the dog']

"""
When the user requests the list, it is presented
"""
task_manager = TaskManager()
task_manager.add_todo('Python Homework')
task_manager.add_todo('Walk the dog')
assert task_manager.formatted_list == "Tasks Still To Do : Python Homework, Feed the fish"

```