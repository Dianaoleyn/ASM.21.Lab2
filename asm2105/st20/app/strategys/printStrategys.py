from abc import ABC, abstractmethod

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
        pass