from abc import ABC, abstractmethod

import json

class BasePrintStrategy(ABC):
    def __init__(self, obj):
        self.obj = obj

    @abstractmethod
    def print(self):
        pass

class ConsolePrintStrategy(BasePrintStrategy):
    def print(self):
        if self.obj.__str__ is not object.__str__:
            print(str(self.obj))
        else:
            text=''
            for key, value in self.obj.__dict__.items():
                text+=f'{key}: {value}\n'

            print(text)

class WebPrintStrategy(BasePrintStrategy):
    def print(self):
        attribs = self.obj.__class__.get_attribs()

        result={}
        for attr, value in attribs.items():
            result[attr] = {'value':self.obj.__getattribute__(attr),
                            'attrName':value[0],
                            'attrType':str(value[1].__name__)}
        return result

