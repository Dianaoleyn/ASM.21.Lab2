import pickle

from fileIO import FileIO
from consoleIO import ConsoleIO
from schooler import Schooler 
from teacher import Teacher 

class Group:
    def __init__(self):
        self.list = []

    def addNewPerson(self):
        ConsoleIO.load(self.list)
        

    def clearList(self):
        self.list.clear()

    def deleteOneElement(self):
        print('Какой объект удалить?')
        self.list.pop(int(input()))

    def dumpAllObjects(self):
        ConsoleIO.dump(self.list)

    def loadData(self):
        self.list=FileIO.load()

    def dumpData(self):
        FileIO.dump(self.list)