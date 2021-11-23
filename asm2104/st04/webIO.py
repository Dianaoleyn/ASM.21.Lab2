from student import Student 
from head import Head 

class WebIO:
    def addOneElement(self,newElement,newList):
            newList.append(newElement)

    def output(self,newList):
        str=''
        for i in range(0, newList.__len__()):
            str+=newList[i].__str__() +'<a href="/deleteObj/'+i.__str__()+'">Удалить элемент</a><br>'
        return str