from flask import request
from dataclasses import dataclass
from asm2105.st04.groupleader import GroupLeader
from asm2105.st04.storage import LocalStorage
from asm2105.st04.strategy import WebStrategy
from asm2105.st04.student import Student


@dataclass
class Group:
    def __init__(self):
        self.group_members = []
        self.storage = LocalStorage()

        try:
            self.load()
        except:
            pass

    def add(self):
        type = request.form['type']
        student = Student(WebStrategy) if type == 'student' else GroupLeader(WebStrategy)
        student.id = len(self.group_members)
        student.set()
        self.group_members.append(student)

    def load(self):
        self.group_members = self.storage.load()

    def save(self):
        self.storage.save(self.group_members)

    def clear(self):
        self.group_members.clear()
