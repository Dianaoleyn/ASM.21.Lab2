from abc import ABC, abstractmethod

from flask import request

class BaseGetSet(ABC):
    def __init__(self, obj):
        self.obj=obj

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def set(self):
        pass

class ConsoleGetSet(BaseGetSet):
    def print(self):
        for key, value in self.obj.__dict__.items():
            if key != "strategy":
                print(key,': ', value)

    def set(self):
        for key, value in self.obj.get_attribs().items():
            self.obj.__dict__[key] = input(value)

class WebGetSet(BaseGetSet):
    def print(self):
        text = '<div>'
        for key, value in self.obj.__dict__.items():
            if key != "strategy":
                text += f'<span>{key}: {value}</span><br>'
        text += '</div>'

        return text

    def set(self):
        for key, value in request.form.items():
            self.obj.__dict__[key] = value

