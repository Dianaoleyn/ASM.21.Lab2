from Member import Member


class Staff(Member):
    def __init__(self, name=None, surname=None, age=None, function=None):
        super(Staff, self).__init__(name, surname, age)
        if function is None:
            self.function = input('Enter function\n')
        else:
            self.function = function

    def __str__(self):
        text = super().__str__()
        text += f'Function: {self.function}\n' \
                f'Member Type: Staff'
        return text
