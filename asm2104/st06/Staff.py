from Member import Member


class Staff(Member):
    def __init__(self, id=2, status='Staff', name=None, surname=None, age=None, function=None, ):
        super().__init__(id, status, name, surname, age)
        if function is None:
            self.function = input('Enter function\n')
        else:
            self.function = function

    def __str__(self):
        text = super().__str__()
        text += f'Function: {self.function}'
        return text
