from schooler import Schooler

class Teacher(Schooler):
    # def __init__(self,name,surname,rating,characteristic,education,subject):
    #     self.name = name
    #     self.surname = surname
    #     self.rating = rating
    #     self.characteristic = characteristic
    #     self.education = education
    #     self.subject = subject

    def strWeb(self,index):
        href='/delete/index/'+index.__str__()
        return super().__str__() + ' Образование:'+self.education+ ' Предмет:'+self.subject+'<a href="'+href+'">Удалить</a><br>'

    def __str__(self):
        return super().__str__() + ' Образование:'+self.education+ ' Предмет:'+self.subject