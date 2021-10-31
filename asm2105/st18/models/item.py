

class item:
    def __init__(self, interactive, type='item'):
        self.id=-1
        self.name=''
        self.age=int()
        self.interactive=interactive()
        self.type=type

    def __str__(self):
        text=f'Номер: {self.id}\n' \
             f'Имя: {self.name}\n' \
             f'Возраст: {self.age}\n'
        return text

    def Print(self):
        return self.interactive.Print(self)

    def Enter(self):
        return self.interactive.Enter(self)