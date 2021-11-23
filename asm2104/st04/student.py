from inputStrategy import InputStrategy

class Student:
    def __init__(self,__dict__):
        self.inputStrategy=InputStrategy
        self.inputForm(__dict__)   

    def inputProperties(self,name,surname,age,mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.mark = mark

    def inputForm(self,__dict__):
        self.inputStrategy.input(self, __dict__)


    def __str__(self):
        return 'Имя:'+self.name + ' Фамилия:'+ self.surname+' Средний балл:'+self.mark+' Возраст:'+self.age+' '