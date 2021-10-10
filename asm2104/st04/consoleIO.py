from student import Student 
from head import Head 

class ConsoleIO:
    def output(self,newList):
        for obj in newList:
            print(obj)

    def input(self,newList):
        print('0-Добавить студента:\n1-Добавить старосту:')
        selectedInput=int(input())
        if (selectedInput==0 or selectedInput==1):
            print('Сколько обучающихся добавить?')
            n=int(input())
            if(selectedInput==0):
                for _ in range(n):
                    newList.append(Student())
            elif (selectedInput==1):
                for _ in range(n):
                    newList.append(Head())  
        else:
            print('Неправильный ввод')