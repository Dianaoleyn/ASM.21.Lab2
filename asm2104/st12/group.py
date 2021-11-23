import pickle

from fileIO import FileIO
from flaskIO import FlaskIO
from schooler import Schooler 
from teacher import Teacher 

class Group:
    def __init__(self):
        self.list = []
        self.strategy=FlaskIO     

    def add(self,el,dict):
        el.name=dict['name']
        el.surname=dict['surname']
        el.rating=dict['rating']
        el.characteristic=dict['characteristic']
        if(dict.__contains__('education')):
            el.education=dict['education']
        if(dict.__contains__('subject')):
            el.subject=dict['subject']      
        self.list.append(el)

    def clearList(self):
        self.list.clear()

    def deleteOneElement(self,number):
        self.list.pop(int(number))

    # def dumpAllObjects(self):
    #     return FlaskIO.dump(self.list)

    def loadData(self):
        self.list=FileIO.load()

    def dumpData(self):
        return self.strategy.dump(self.list)