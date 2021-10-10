from .Employee import Employee


class Chief(Employee):
    def __init__(self, name='', surname='', age='', salary='', coe=''):
        super().__init__(name, surname, age, salary)
        self.CountOfEmployees = coe

    def __str__(self):
        return super().__str__() + f', Колличество подчинённых { self.CountOfEmployees }'

