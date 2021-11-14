from Member import Member


class Player(Member):
    def __init__(self, id =1, status='Player', name=None, surname=None, age=None, position=None, ):
        super().__init__(id, status, name, surname, age)
        if position is None:
            self.position = input('Enter position\n')
        else:
            self.position = position

    def __str__(self):
        text = super().__str__()
        text += f'Position: {self.position}'
        return text
