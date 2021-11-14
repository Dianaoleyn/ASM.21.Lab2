class Student(object):
    name = ''
    surname = ''
    age = None
    rating = None  #средний балл
    is_VUC = False

    def __init__(self, name = '', surname = '' , age = None , rating = None):
        self.name = name
        self.surname = surname
        self.age = age
        self.rating = rating
        self.is_VUC = False

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}, Средний балл: {self.rating}"