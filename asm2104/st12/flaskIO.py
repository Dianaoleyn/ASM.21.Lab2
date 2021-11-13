from schooler import Schooler 
from teacher import Teacher 


class FlaskIO:
    
    @staticmethod
    def dump(mass):
        s=''
        for o in mass:
            s=s+o.__str__()+'<br />'
        return s