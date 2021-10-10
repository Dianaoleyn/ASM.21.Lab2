from student import Student

class Head(Student):
    def __init__(self):
        self.inputProperties()

    def inputProperties(self):
        super().inputProperties()
        self.grant = input('Введите стипендию\n')
        self.number = input('Введите номер в списке\n')

    def __str__(self):
        return super(Head, self).__str__() + ' Стипендия:'+self.grant + ' Номер в списке:'+self.number