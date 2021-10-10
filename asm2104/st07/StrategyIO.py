from Student import Student
from Monitor import Monitor
import pickle

class Full():
    def print(self, card):
        for i in card:
            print(i.strFull())
            
class Short():
    def print(self, card):
        for i in card:
            print(i.strShort())
            
class PickleIO():
    def pickleInput(self, card):
        with open('dataPickle.io','wb') as f:
            pickle.dump(card,f)

    def pickleOutput(self, card):
        with open('dataPickle.io','rb') as f:
            return pickle.load(f)


            
