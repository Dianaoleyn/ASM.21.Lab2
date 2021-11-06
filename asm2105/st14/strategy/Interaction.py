from abc import ABC, abstractmethod
from flask import request

class BaseInteraction(ABC):
    def __init__(self, obj):
        self.obj=obj

    @abstractmethod
    def Out(self):
        pass

    @abstractmethod
    def In(self):
        pass

class ConsoleInteraction(BaseInteraction):
    def Out(self):
        if self.obj.__str__ is not object.__str__:
            print(str(self.obj))
        else:
            for key, value in self.obj.__dict__.items():
                if key != "strategy":
                    print(key, ': ', value)


    def In(self):
        for key in self.obj.__dict__.keys():
            if key!= 'id' and key != "strategy":
                self.obj.__dict__[key] = input(f'Введите {key}\n')


class BrowserInteraction(BaseInteraction):
    def Out(self):
        text = '<div>'

        if self.obj.type==1:
            type='Ученик'
        elif self.obj.type==2:
            type='Староста'
        elif self.obj.type==3:
            type='Сотрудник'
        elif self.obj.type==4:
            type='Учитель'
        elif self.obj.type==5:
            type='Директор'

        text += f'<h3>№{self.obj.id}</h3>'
        for key, value in self.obj.__dict__.items():
            if key != "strategy" and key != "id":
                if key == 'type':
                    text += f'<span>{key}: {type}</span><br>'
                else:
                    text += f'<span>{key}: {value}</span><br>'

        text += '</div>'

        return text

    def In(self):
        for key, value in request.form.items():
            self.obj.__dict__[key]=value