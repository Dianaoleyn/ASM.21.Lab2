from Member import Member


class Manager(Member):
    def __init__(self, id=3, status='Manager', name=None, surname=None, age=None, role=None):
        super().__init__(id, status, name, surname, age)
        if role is None:
            self.role = input('Enter role\n')
        else:
            self.role = role

    def __str__(self):
        text = super().__str__()
        text += f'Role: {self.role}'
        return text
