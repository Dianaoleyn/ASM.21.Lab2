from Employee import Employee


class Developer(Employee):
    def __init__(self, id, full_name=None, position=None, salary=None, qualification=None):
        Employee.__init__(self, id, full_name, position, salary)
        self.position = 'developer'
        if qualification is None:
            self.qualification = input('Input qualification: ')
        else:
            self.qualification = qualification

    def __str__(self):
        text = super().__str__()
        text += 'Qualification: {0}'.format(self.qualification) + '\n\n'
        return text
