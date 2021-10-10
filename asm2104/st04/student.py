class Student:
    def __init__(self):
        self.inputProperties()
        

    def inputProperties(self):
        self.name = input('Введите имя\n')
        self.surname = input('Введите фамилию\n')
        self.age = input('Введите возраст\n')
        self.mark = input('Введите оценку\n')


    def __str__(self):
        return 'Имя:'+self.name + ' Фамилия:'+ self.surname+' Средний балл:'+self.mark+' Возраст:'+self.age