class Member:

    def __init__(self, name=None, surname=None, age=None):
        if name is None:
            self.name = input('Enter name\n')
            self.surname = input('Enter surname\n')
            self.age = input('Enter age\n')
        else:
            self.name = name
            self.surname = surname
            self.age = age

    def __str__(self):
        text = f'Name: {self.name}\n' \
               f'Surname: {self.surname}\n' \
               f'Age: {self.age}\n'
        return text
