from schooler import Schooler 
from teacher import Teacher 


class FlaskIO:
    
    @staticmethod
    def dump(mass):
        s=''
        for i in range(0,mass.__len__()):
            s=s+mass[i].strWeb(i)
        return s