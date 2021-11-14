class Member:

    def __init__(self, id=0, status='Member', name=None, surname=None, age=None, ):
        if name is None:
            self.id = id
            self.status = status
            self.name = input('Enter name\n')
            self.surname = input('Enter surname\n')
            self.age = input('Enter age\n')
        else:
            self.status = status
            self.id = id
            self.name = name
            self.surname = surname
            self.age = age

    def __str__(self):
        text = f'id: {self.id}\n' \
               f'status: {self.status}\n' \
               f'Name: {self.name}\n' \
               f'Surname: {self.surname}\n' \
               f'Age: {self.age}\n'
        return text
