from student import Student 
from head import Head 

class WebIO:
    def addOneElement(self,newElement,newList):
            newList.append(newElement)

    def output(self,newList):
        str=''
        for obj in newList:
            str+=obj.__str__()+'<br />'
        return str