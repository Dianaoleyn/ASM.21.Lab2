
class Console:
    def __init__(self, obj):
        self.obj=obj

    def output(self):
        for key, value in self.obj.__dict__.items():
            print(key, ': ', value)

    def input(self):
        for key in self.obj.__dict__.keys():
            if key!='id':
                self.obj.__dict__[key] = input(f'Введите {key}\n')