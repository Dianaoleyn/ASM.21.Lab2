from abc import ABC, abstractmethod
from flask import request
import json

class BaseInteractive(ABC):
    @abstractmethod
    def Enter(self, obj):
        pass

    @abstractmethod
    def Print(self, obj):
        pass


class ConsoleInteractive(BaseInteractive):
    def Enter(self, obj):
        for key in obj.__dict__.keys():
            if key!= 'id' and key != "interactive" and key!='type':
                obj.__dict__[key] = input(f'Введите {key}\n')

    def Print(self, obj):
        if obj.__str__ is not object.__str__:
            print(str(obj))
        else:
            for key, value in obj.__dict__.items():
                if key != "interactive":
                    print(key, ': ', value)

class BrowserInteractive(BaseInteractive):
    def Enter(self, obj):
        data = json.loads(request.form['data'])
        for key, value in data['attribs'].items():
            obj.__dict__[key] = value


    def Print(self, obj):
        text='<div>'
        text+=f'<h3>Объект №{obj.id}</h3>'
        for key, value in obj.__dict__.items():
            if key != "interactive" and key != "id":
                text+=f'<span>{key}: {value}</span><br>'
        text+='</div>'

        return text

