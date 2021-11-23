

class item:
    def __init__(self, strategy):
        self.id=-1
        self.name=''
        self.age=int()
        self.gender=''

        self.strategy=strategy

    def __str__(self):
        text=f'Number: {self.id}\n' \
            f'Name: {self.name}\n' \
             f'Age: {self.age}\n' \
             f'Gender: {self.gender}\n'
        return text

    def Out(self):
        self.strategy.Out(self)

    def In(self):
        self.strategy.In(self)
