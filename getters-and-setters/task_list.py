from uuid import uuid4


class TaskList:

    def __init__(self, list_name):

        self.tasks = {}
        self.id = str(uuid4())
        self.list_name = list_name
    
    def get_task_list_name(self):
        return self.list_name
    
    def get_task_list(self):
        return self.tasks

    def add_task_to_list(self, task):
        self.tasks[task.id] = task
    
    def remove_task_from_list(self, task_id):
        self.tasks.pop(task_id)
    
    def check_off_task(self, task_id):
        task = self.tasks[task_id]
        task.set_is_checked(True)
    
    def uncheck_task(self, task_id):
        task = self.tasks[task_id]
        task.set_is_checked(False)
