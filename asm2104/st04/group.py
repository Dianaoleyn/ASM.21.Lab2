import pickle

from fileIO import FileIO
from webIO import WebIO
from student import Student 
from head import Head 

class Group:
    def __init__(self):
        self.list = []
        self.strategy=WebIO()

    # def addElement(self):
    #     self.inputList(ConsoleIO())
        
    def addElement(self,newElement,newStrategy):
        self.strategy=newStrategy
        self.strategy.addOneElement(newElement,self.list)

    def clearList(self):
        self.list.clear()

    def deleteObject(self,n):
        if(len(self.list)!=0):
            # print('Введите индекс объекта, который нужно удалить')
            # n=int(input())
            if(len(self.list)>int(n)):
                # print('В списке нет элемента')
                self.list.pop(int(n))
    
    # def editObject(self):
    #     if(len(self.list)==0):
    #         print('Список пуст')
    #     else:
    #         print('Введите индекс объекта, который нужно изменить')
    #         n=int(input())
    #         if(len(self.list)<=n):
    #             print('В списке нет элемента')
    #         else:
    #             self.list[n].inputProperties()

    def outputList(self):
        return self.strategy.output(self.list)

    def inputList(self):
        return self.strategy.input(self.list)

    def outputWeb(self):
        self.strategy=WebIO
        if(len(self.list)==0):
            return 'Список пуст'
        else:
            self.changeStrategy(WebIO())
            printList=self.outputList()
            return printList

    def changeStrategy(self,newStrategy):
        self.strategy=newStrategy       

    def outputFile(self):
        self.changeStrategy(FileIO())
        return self.outputList()

    def inputFile(self):
        self.changeStrategy(FileIO())
        self.list=self.inputList()