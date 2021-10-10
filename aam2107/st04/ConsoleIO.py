from flask import Flask, render_template, g


class ConsoleIO:
    @staticmethod
    def do_output(self):
        for key, val in self.__dict__.items():
            if key != "io":
                print(key[10:], val)

    @staticmethod
    def do_input(self):
        for key, val in self.__dict__.items():
            if key != "io":
                self.__dict__[key] = input(f"{ key[10:] }: ")


class WebIO:
    @staticmethod
    def do_output(self):
        return render_template('home.html', param=str(self), **self.__dict__)

    @staticmethod
    def do_input(self, form, maxid):
        self.__dict__['id'] = maxid
        self.__dict__['name'] = form.get('name')
        self.__dict__['surname'] = form.get('surname')
        self.__dict__['age'] = form.get('age')
        self.__dict__['salary'] = form.get('salary')
        self.__dict__['CountOfEmployees'] = form.get('coe')




