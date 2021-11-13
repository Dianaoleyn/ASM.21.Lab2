from schooler import Schooler

class Teacher(Schooler):
    def __init__(self,name,surname,rating,characteristic,education,subject):
        self.name = name
        self.surname = surname
        self.rating = rating
        self.characteristic = characteristic
        self.education = education
        self.subject = subject

    def __str__(self):
        return super(Teacher, self).__str__() + ' Образование:'+self.education+ ' Предмет:'+self.subject