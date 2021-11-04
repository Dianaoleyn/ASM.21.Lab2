from .student import student

class starosta(student):

    def __init__(self, strategy, type='starosta'):
        student.__init__(self, strategy, type)
        self.group_mail = ''

    def __str__(self):
        text=super().__str__()
        text+=f'Почта группа: {self.group_mail}\n'
        return text
