from .worker import worker, Types

class director(worker):
    def __init__(self, strategy):
        worker.__init__(self, strategy)
        self.phone=''
        self.type=Types.director

    def __str__(self):
        text=super().__str__()
        text+=f'Телефон: {self.phone}'