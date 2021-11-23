from abc import ABC, abstractmethod
from flask import request

class BaseSetterStrategy(ABC):
    @abstractmethod
    def to_dict(self, data):
        pass

    @abstractmethod
    def set(self, obj):
        pass

class ConsoleSetterStrategy(BaseSetterStrategy):
    def to_dict(self, data):
        input_dict = {}
        for key, attrib in data.items():
            if isinstance(attrib, str):
                input_dict[key] = input(f'Введите: {attrib}\n')
            elif isinstance(attrib, list):
                while True:
                    buff = input(f'Введите: {attrib[0]}\n')
                    try:
                        input_dict[key] = attrib[1](buff)
                        break
                    except Exception as err:
                        if buff == '\quit':
                            return
                        print('Произошла ошибка. Попробуйте еще раз\n'
                              f'Ошибка: {err}')
        return input_dict

    def set(self, obj):
        pass

class WebSetterStrategy(BaseSetterStrategy):
    def to_dict(self, data):
        return data.to_dict()

    def set(self, obj):
        # print(request.get_json()['attributes'])
        for attr, value in request.get_json()['attributes'].items():
            obj.__setattr__(attr, value)