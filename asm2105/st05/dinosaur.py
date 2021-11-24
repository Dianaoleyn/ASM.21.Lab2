class Dinosaur:
    def __init__(self, strategy, type='Simple'):
        self.id = 0
        self.name = ''
        self.strategy = strategy()
        self.type = type

    def set(self):
        return self.strategy.set(self)

    def get(self):
        return self.strategy.get(self)

    def __str__(self):
        return f'ID: {self.id}\nТип: {self.type}\nИмя: {self.name}\n'
