
class item:
    def __init__(self, strategy, type='item'):
        self.id = -1
        self.name = ''
        self.age = int()
        self.strategy=strategy()
        self.type=type

    def __str__(self):
        text=f'Номер: {self.id}\n' \
             f'Тип: {self.type}\n' \
             f'Имя: {self.name}\n' \
             f'Возраст: {self.age}\n'
        return text

    def set(self):
        self.strategy.set(self)

    def get(self):
        return self.strategy.get(self)

