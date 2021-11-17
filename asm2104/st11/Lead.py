from Employee import Employee


class Lead(Employee):
    def __init__(self, id, full_name=None, position=None, salary=None, department=None):
        Employee.__init__(self, id, full_name, position, salary)
        self.position = 'lead'
        if department is None:
            self.department = input('Input department: ')
        else:
            self.department = department

    def __str__(self):
        text = super().__str__()
        text += 'Department: {0}'.format(self.department) + '\n\n'
        return text
