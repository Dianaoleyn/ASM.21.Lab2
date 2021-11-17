class Employee:

    def __init__(self, id, full_name=None, position=None, salary=None):
        if full_name is None:
            self.id = id
            self.full_name = input('Input full name: ')
            self.position = None
            self.salary = input('Input salary: ')
        else:
            self.id = id
            self.full_name = full_name
            self.position = position
            self.salary = salary

    def __str__(self):
        text = 'ID: {0}'.format(self.id) + '\n' \
               'Full name: {0}'.format(self.full_name) + '\n' \
               'Position: {0}'.format(self.position) + '\n' \
               'Salary: {0}'.format(self.salary) + '\n'
        return text