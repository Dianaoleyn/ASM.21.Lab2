import pickle

from fileIO import FileIO
from consoleIO import ConsoleIO
from student import Student 
from head import Head 

class Group:
    def __init__(self):
        self.list = []

    def addElement(self):
        self.inputList(ConsoleIO())
        

    def clearList(self):
        self.list.clear()

    def deleteObject(self):
        if(len(self.list)==0):
            print('Список пуст')
        else:
            print('Введите индекс объекта, который нужно удалить')
            n=int(input())
            if(len(self.list)<=n):
                print('В списке нет элемента')
            else:
                self.list.pop(n)
    
    def editObject(self):
        if(len(self.list)==0):
            print('Список пуст')
        else:
            print('Введите индекс объекта, который нужно изменить')
            n=int(input())
            if(len(self.list)<=n):
                print('В списке нет элемента')
            else:
                self.list[n].inputProperties()

    def outputList(self,strategy):
        strategy.output(self.list)

    def inputList(self,strategy):
        return strategy.input(self.list)

    def outputConsole(self):
        self.strategy=ConsoleIO
        if(len(self.list)==0):
            print('Список пуст')
        else:
            self.outputList(ConsoleIO())

    def outputFile(self):
        self.outputList(FileIO())

    def inputFile(self):
        self.list=self.inputList(FileIO())