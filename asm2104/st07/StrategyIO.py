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
        with open('asm2104/st07/dataPickle.io','wb') as f:
            pickle.dump(card,f)

    def pickleOutput(self, card):
        with open('asm2104/st07/dataPickle.io','rb') as f:
            return pickle.load(f)
class Web():
    def print(self, card):
        str=''
        for i in range(0,card.__len__()):
            str=str+card[i].strWeb(i+1)
        return str
    
    def inputProperties(dict,el):
        el.name=dict['name']
        el.surname=dict['surname']
        el.age=dict['age']
        if(dict.__contains__('increasedScholarship')):
            el.increasedScholarship=dict['increasedScholarship']  

            
