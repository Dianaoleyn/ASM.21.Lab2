from Member import Member


class Manager(Member):
    def __init__(self, name=None, surname=None, age=None, role=None):
        super(Manager, self).__init__(name, surname, age)
        if role is None:
            self.role = input('Enter role\n')
        else:
            self.role = role

    def __str__(self):
        text = super().__str__()
        text += f'Role: {self.role}\n' \
                f'Member Type: Manager'
        return text
