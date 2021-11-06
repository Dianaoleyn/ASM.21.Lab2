from .student import student, Types

class starosta(student):
    def __init__(self, strategy):
        student.__init__(self, strategy)
        self.email=''
        self.type=Types.starosta

    def __str__(self):
        text=super().__str__()
        text+=f'Почта группы: {self.email}\n'
        return text