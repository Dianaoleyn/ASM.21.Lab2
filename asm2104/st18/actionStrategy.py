class Console:
    def __init__(self, obj):
        self.obj=obj

    def output(self):
        for key, value in self.obj.__dict__.items():
            print(key, ': ', value)

    def input(self):
        for key in self.obj.__dict__.keys():
            if key!='id':
                self.obj.__dict__[key] = input(f'Input {key}\n')



from flask import request

class Web:
    def __init__(self, obj):
        self.obj=obj

    def output(self):
        text=''
        for key, value in self.obj.__dict__.items():
            text+=f'{key}: {value}<br>'
        return text

    def input(self):
        for key, value in request.form.items():
            self.obj.__dict__[key] = value
