from student import student

class proforg(student):
    def __init__(self, type='proforg'):
        student.__init__(self, type)
        self.profileTicketNumber = int()

    def __str__(self):
        result = super().__str__()
        result += f'Profile ticket number: {self.profileTicketNumber}'
        return result
