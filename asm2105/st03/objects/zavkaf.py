from .worker import worker

class zavkaf(worker):

    def __init__(self, strategy, type='zavkaf'):
        worker.__init__(self, strategy, type)
        self.phone=''

    def __str__(self):
        text=super().__str__()
        text+=f'Телефон: {self.phone}\n'
        return text
