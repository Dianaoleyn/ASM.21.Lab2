from Student import Student
from Monitor import Monitor
from StrategyIO import Short, Full, PickleIO

class CardFile:
    def __init__(self):
        self.strategy=Full()
        self.card = []
        self.chosen = 'Full'
    
    def setStrategy(self):
        if self.chosen=='Short':
            self.strategy=Short()
        else:
            if self.chosen=='Full':
                self.strategy=Full()
    
    def add(self):
        choice = int(input("0 - Студент, 1  - Староста: \n"))
        student = Monitor() if choice else Student()
        student.input()
        self.card.append(student)

    def change(self):
        index = int(input("Введите номер студента"))
        self.card[index-1].input()

    def print(self):
        self.strategy.print(self.card)

    def file_read(self):
        self.strategy=PickleIO()
        self.card=self.strategy.pickleOutput(self.card)
        self.setStrategy()

    def file_write(self):
        self.strategy = PickleIO()
        self.strategy.pickleInput(self.card)
        self.setStrategy()

    def clear(self):
        self.card.clear()
    
    def changeOutput(self):
        if self.chosen == 'Short':
            self.chosen = 'Full'
            self.setStrategy()
        else:
            self.chosen = 'Short'
            self.setStrategy()
