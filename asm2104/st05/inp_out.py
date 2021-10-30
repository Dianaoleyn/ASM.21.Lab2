"""
Файл  стратегий ввода вывода
"""
from abc import ABC, abstractmethod
from typing import List
from person import Student, MainStudent
from flask import Flask, render_template


class StrategyIO(ABC):
    @abstractmethod
    def enter(self, person: Student, request=None):
        pass

    def output(self, data: List):
        pass


class InputOutPutConsole(StrategyIO):
    def enter(self, person: Student, request=None):
        for key, val in person.__dict__.items():
            if key != 'is_main':
                person.__dict__[key] = input(f"{ key }: ")

    def output(self, data: List):
        print('-------Участники группы----------')
        for person in data:
            for key, val in person.__dict__.items():
                print(f"{key} : {val}")
            print("\n")
        print('---------------------------------')


class InputOutputWeb(StrategyIO):
    def enter(self, person: Student, request=None):
        if person.is_main:
            person.first_name = request.form['first_name']
            person.last_name = request.form['last_name']
            person.age = request.form['age']
            person.scholarship = request.form['scholarship']
        else:
            person.first_name = request.form['first_name']
            person.last_name = request.form['last_name']
            person.age = request.form['age']

    def output(self, data: List):
        return
