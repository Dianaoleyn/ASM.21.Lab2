from Student import Student
from Monitor import Monitor
from StrategyIO import Short, Full, PickleIO, Web

class CardFile:
    def __init__(self):
        self.strategy=Web()
        self.card = []
        self.chosen = 'Web'
    
    def setStrategy(self):
        if self.chosen=='Short':
            self.strategy=Short()
        if self.chosen=='Full':
            self.strategy=Full()
        if self.chosen=='Web':
          self.strategy=Web()
    
    def add(self):
        choice = int(input("0 - Студент, 1  - Староста: \n"))
        student = Monitor() if choice else Student()
        student.input()
        self.card.append(student)
    
    def add(self, student):
        self.card.append(student)

    def change(self):
        index = int(input("Введите номер студента"))
        self.card[index-1].input()

    def print(self):
        self.strategy = Web()
        return self.strategy.print(self.card)

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
        
    def delete(self, index):
        self.card.pop(index-1)
    
    def changeOutput(self):
        if self.chosen == 'Short':
            self.chosen = 'Full'
            self.setStrategy()
        else:
            self.chosen = 'Short'
            self.setStrategy()
