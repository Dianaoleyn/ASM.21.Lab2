from asm2104.st03.student import Student

class Student_VUC(Student):
    def __init__(self , name = '', surname = '' , age = None , rating = None):
        super().__init__(name , surname , age , rating)
        self.is_VUC = True

    def __str__(self):
        return f"Имя: {self.name}; Фамилия: {self.surname}; Возраст: {self.age}; Средний балл: {self.rating}; Студент обучается в ВУЦ"
