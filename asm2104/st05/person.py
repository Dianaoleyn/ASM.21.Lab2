class Student(object):
    first_name = ''
    last_name = ''
    age = None
    is_main = None

    def __init__(self, f_name='', l_name='', age=None):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.is_main = False

    def __str__(self):
        return f"Меня зовут {self.first_name} {self.last_name} Мне {self.age} лет. Роль: студент."


class MainStudent(Student):
    def __init__(self, f_name='', l_name='', age=None, scholarship=None):
        super().__init__(f_name, l_name, age)
        self.scholarship = scholarship
        self.is_main = True

    def __str__(self):
        return f"Меня зовут {self.first_name} {self.last_name} Мне {self.age} лет. Роль: староста."
