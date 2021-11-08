from student import Student

class Head(Student):
    def __init__(self,name,surname,age,mark,grant,number):
        self.inputProperties(name,surname,age,mark,grant,number)

    def inputProperties(self,name,surname,age,mark,grant,number):
        self.name = name
        self.surname = surname
        self.age = age
        self.mark = mark
        self.grant=grant
        self.number=number


    def __str__(self):
        return super(Head, self).__str__() + ' Стипендия:'+self.grant + ' Номер в списке:'+self.number

    def WebOutput(self):
        return self.name

        