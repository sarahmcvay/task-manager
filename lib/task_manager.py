
class TaskManager(): 
    def __init__(self):
        self.todo_list = []
        self.completed_list = []

    def add_todo(self, task):
        if not isinstance(task, str):
            raise TypeError("Not a valid Task!")
        if task.strip() == "":
            raise ValueError("You have not added a Task!")

        self.todo_list.append(task)

    def completed_task(self, task):
        self.todo_list.remove(task)
        self.completed_list.append(task)

    def format_todo(self):
        return f"Tasks Still To Do: {", ".join(self.todo_list)}"

