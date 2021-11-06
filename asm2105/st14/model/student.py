from .listEntry import listEntry, Types

class student(listEntry):
    def __init__(self, strategy):
        listEntry.__init__(self, strategy)
        self.Class=int()
        self.type=Types.student

    def __str__(self):
        text=super().__str__()
        text+=f'Класс: {self.Class}\n'
        return text