from Student import Student


class Monitor(Student):
    def __init__(self, name='', surname='', age='', increasedScholarship=''):
        super().__init__(name, surname, age)
        self.increasedScholarship = increasedScholarship

    def strFull(self):
        return super().strFull() + f', Повышенная стипендия { self.increasedScholarship }'
    
    def strShort(self):
        return super().strShort()
    
    def input(self):
        self.name = input("Имя: ")
        self.surname = input("Фамилия: ")
        self.age = int(input("Возраст: "))
        self.increasedScholarship = int(input("Повышенная стипендия: "))
