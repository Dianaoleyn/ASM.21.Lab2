from flask import Flask, render_template, g


class ConsoleIO:
    def Input(self, field):
        return input(field)

    def Output(self, o):
        print(o)

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
        self.__dict__['experience'] = form.get('exp')





