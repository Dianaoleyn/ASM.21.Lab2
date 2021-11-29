from Student import Student


class Monitor(Student):
    def __init__(self, name='', surname='', age='', increasedScholarship=''):
        super().__init__(name, surname, age)
        self.increasedScholarship = increasedScholarship

    def strFull(self):
        return super().strFull() + f', Повышенная стипендия { self.increasedScholarship }'
    
    def strShort(self):
        return super().strShort()
    
    def strWeb(self,index):
        urlDelete='/delete/index/'+index.__str__()
        urlUpdate='/updateMonitor/'+index.__str__()
        return self.name+"<br />"+self.surname+"<br />"+self.age +"<br />"+ self.increasedScholarship+"<br />"+'<a href="'+urlDelete+'">Удалить</a><br>'+'<a href="'+urlUpdate+'">Изменить</a><br>'"<br />"
    
    def input(self):
        self.name = input("Имя: ")
        self.surname = input("Фамилия: ")
        self.age = int(input("Возраст: "))
        self.increasedScholarship = int(input("Повышенная стипендия: "))
