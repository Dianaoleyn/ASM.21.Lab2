from schooler import Schooler

class Teacher(Schooler):
    def __init__(self):
        super(Teacher, self).__init__()
        self.education = input('Введите образование\n')
        self.subject = input('Введите предмет для преподавания\n')

    def __str__(self):
        return super(Teacher, self).__str__() + ' Образование:'+self.education+ ' Предмет:'+self.subject