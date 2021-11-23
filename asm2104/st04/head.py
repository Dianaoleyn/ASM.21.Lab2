from student import Student
from inputStrategy import InputStrategy

class Head(Student):
    def __init__(self,__dict__):
        self.inputStrategy=InputStrategy
        self.inputForm(__dict__)

    def inputProperties(self,name,surname,age,mark,grant,number):
        self.name = name
        self.surname = surname
        self.age = age
        self.mark = mark
        self.grant=grant
        self.number=number

    def inputForm(self,__dict__):
        self.inputStrategy.input(self, __dict__)


    def __str__(self):
        return super().__str__() + ' Стипендия:'+self.grant + ' Номер в списке:'+self.number+' '

        