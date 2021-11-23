
class member:
    def __init__(self):
        self.id=int()
        self.name=str()
        self.age=int()

    def output(self, strategy):
        return strategy(self).output()

    def input(self, strategy):
        strategy(self).input()

    def __str__(self):
        return f'ID: {self.id}\n' \
               f'Name: {self.name}\n' \
               f'Age: {self.age}\n'
