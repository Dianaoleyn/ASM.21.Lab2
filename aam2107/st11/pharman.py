class Pharman:
    def __init__(self, name, salary, stake):
        self.name = name
        self.salary = salary
        self.stake = stake

    @staticmethod
    def newPharman():
        name = input('Введите ФИО\n')
        salary = input('Введите зарплату\n')
        stake = input('Введите ставку\n')
        return Pharman(name, salary, stake)

    def __str__(self):
        return 'ФИО: {}, З/П: {}, Ставка: {}, '.format(self.name, self.salary, self.stake)
