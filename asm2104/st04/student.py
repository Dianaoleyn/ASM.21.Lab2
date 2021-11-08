class Student:
    def __init__(self,name,surname,age,mark):
        self.inputProperties(name,surname,age,mark)
        

    def inputProperties(self,name,surname,age,mark):
        self.name = name
        self.surname = surname
        self.age = age
        self.mark = mark


    def __str__(self):
        return 'Имя:'+self.name + ' Фамилия:'+ self.surname+' Средний балл:'+self.mark+' Возраст:'+self.age