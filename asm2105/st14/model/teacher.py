from .worker import worker, Types

class teacher(worker):
    def __init__(self, strategy):
        worker.__init__(self, strategy)
        self.subject=''
        self.type=Types.teacher

    def __str__(self):
        text=super().__str__()
        text+=f'Предмет: {self.subject}\n'
        return text