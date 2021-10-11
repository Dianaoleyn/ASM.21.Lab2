from schooler import Schooler 
from teacher import Teacher 


class ConsoleIO:
    
    @staticmethod
    def dump(mass):
        for o in mass:
            print(o)

    @staticmethod
    def load(mass):
        classes = {
            0:(Schooler),
            1:(Teacher),
            }
        print('0-Добавить ученика:\n1-Добавить учителя:')
        selectedItem=int(input())
        mass.append(classes[selectedItem]()) 