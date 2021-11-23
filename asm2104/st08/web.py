from flask import request

class Web:
    def __init__(self, obj):
        self.obj=obj

    def output(self):
        text = '<div>'
        text += f'<h3>ID №{self.obj.id}</h3>'
        for key, value in self.obj.__dict__.items():
            if key != "id":
                text += f'<span>{key}: {value}</span><br>'
        text += f'<a href="/refactor/{self.obj.id}">Refactor</a>' \
                '</div>'

        return text

    def input(self):
        for key in self.obj.__dict__.keys():
            if key!='id':
                self.obj.__dict__[key]=request.form['add-'+str(key)]
