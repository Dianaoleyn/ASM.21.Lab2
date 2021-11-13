import pickle

from fileIO import FileIO
from flaskIO import FlaskIO
from schooler import Schooler 
from teacher import Teacher 

class Group:
    def __init__(self):
        self.list = []
        self.strategy=FlaskIO     

    def clearList(self):
        self.list.clear()

    def deleteOneElement(self,number):
        self.list.pop(int(number)-1)

    # def dumpAllObjects(self):
    #     return FlaskIO.dump(self.list)

    def loadData(self):
        self.list=FileIO.load()

    def dumpData(self):
        return self.strategy.dump(self.list)