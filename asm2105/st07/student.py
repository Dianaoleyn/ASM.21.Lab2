class Student:
    def __init__(self, strategy, type='Студент'):
        self.id = -1
        self.name = ''
        self.second_name = ''
        self.strategy = strategy()
        self.type = type

    def set(self):
        return self.strategy.set(self)

    def get(self):
        return self.strategy.get(self)

    def __str__(self):
        return f'Идентификатор: {self.id}\nТип: {self.type}\nИмя: {self.name}\nФамилия: {self.second_name}\n'
