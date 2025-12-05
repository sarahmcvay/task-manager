
class TaskManager(): 
    def __init__(self):
        self.todo_list = []

    def add_todo(self, task):
        self.todo_list.append(task)

    def format_todo(self):
        return f"Tasks Still To Do: {", ".join(self.todo_list)}"