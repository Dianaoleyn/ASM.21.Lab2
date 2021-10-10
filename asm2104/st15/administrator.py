from salesman import Salesman


class Administrator(Salesman):
    def __init__(self, name, salary, stake, level):
        super(Administrator, self).__init__(name, salary, stake)
        self.level = level

    def __str__(self):
        return super(Administrator, self).__str__() + f'Уровень: {self.level}'

    @staticmethod
    def newSalesman():
        name = input('Введите ФИО\n')
        salary = input('Введите зарплату\n')
        stake = input('Введите ставку\n')
        level = input('Введите уровень\n')
        return Administrator(name, salary, stake, level)
