from .listEntry import listEntry, Types

class worker(listEntry):
    def __init__(self, strategy):
        listEntry.__init__(self, strategy)
        self.salary=int()
        self.type=Types.worker

    def __str__(self):
        text=super().__str__()
        text+=f'Зарплата: {self.salary}\n'
        return text
