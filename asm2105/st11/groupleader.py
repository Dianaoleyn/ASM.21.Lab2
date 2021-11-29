from asm2105.st11.student import Student


class GroupLeader(Student):
    def __init__(self, strategy, type='Староста'):
        super(GroupLeader, self).__init__(strategy, type)
        self.stipend = int()

    def __str__(self):
        return super(GroupLeader, self).__str__() + f'Стипендия: {self.stipend}\n'
