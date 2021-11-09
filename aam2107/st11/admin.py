from pharman import Pharman
class Admin(Pharman):
    def __init__(self, name, salary, stake, level):
        super(Admin, self).__init__(name, salary, stake)
        self.level = level

    def __str__(self):
        return super(Admin, self).__str__() + f'Уровень: {self.level}'

    @staticmethod
    def newPharman():
        name = input('Введите ФИО\n')
        salary = input('Введите зп\n')
        stake = input('Введите ставку\n')
        level = input('Введите должность\n')
        return Admin(name, salary, stake, level)
