from uuid import uuid4


class Task:

    def __init__(self, name):

        self.id = str(uuid4())
        self.name = name
        self.is_checked = False

    def set_task_name(self, name):
        self.name = name

    def get_task_name(self):
        return self.name
    
    def get_is_checked(self):
        return self.is_checked
    
    def set_is_checked(self, new_value):
        self.is_checked = True