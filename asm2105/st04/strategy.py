from flask import request


class Strategy:
    def set(self, obj):
        pass

    def get(self, obj):
        pass


class ConsoleStrategy(Strategy):
    def set(self, obj):
        for key in obj.__dict__.keys():
            if key != 'id' and key != "strategy" and key != 'type':
                obj.__dict__[key] = input(f'Введите {key}\n')

    def get(self, obj):
        if obj.__str__ is not object.__str__:
            print(str(obj))
        else:
            for key, value in obj.__dict__.items():
                if key != "strategy":
                    print(key, ': ', value)


class WebStrategy(Strategy):
    def set(self, obj):
        for key in obj.__dict__.keys():
            if key != 'id' and key != "strategy" and key != 'type':
                obj.__dict__[key] = request.form[key]

    def get(self, obj):
        text = ''
        for key, value in obj.__dict__.items():
            if key != "strategy":
                text += f'{key}: {value} | '
        return text