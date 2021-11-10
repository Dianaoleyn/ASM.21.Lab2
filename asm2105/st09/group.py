import cgitb
import codecs
import sys
import time

from flask import request

from dataclasses import dataclass, field
from typing import List
import pickle

from asm2105.st04.groupleader import GroupLeader
from asm2105.st04.member import Member
from asm2105.st04.student import Student

pathToFile = './asm2105/st09/group.dat'

cgitb.enable()
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

student_types = [
    {'value': 'student', 'class': Student},
    {'value': 'groupLeader', 'class': GroupLeader}
]


@dataclass
class Group:
    name = ''
    group_members: List[Member] = field(default_factory=list)

    def generateId(self):
        if not self.group_members:
            return 0
        else:
            max_index = 0
            for i in self.group_members:
                if i.id > max_index:
                    max_index = i.id
            return max_index + 1

    def addStudent(self):
        type = request.form['type']
        el = [x for x in student_types if x['value'] == type][0]
        member = el['class']()
        member.getData(self.generateId())
        self.group_members.append(member)

    def getMemberById(self, id):
        member = [x for x in self.group_members if x.id == id][0]
        return member

    def editStudent(self, id):
        member = [x for x in self.group_members if x.id == id][0]
        self.group_members.remove(member)
        type = request.form['type']
        el = [x for x in student_types if x['value'] == type][0]
        member = el['class']()
        member.getData(id)
        self.group_members.append(member)

    def deleteStudent(self, id):
        member = [x for x in self.group_members if x.id == id][0]
        self.group_members.remove(member)

    def saveGroup(self):
        with open(pathToFile, 'wb') as f:
            pickle.dump({'name': self.name, 'data': self.group_members}, f)

    def loadGroup(self):
        with open(pathToFile, 'rb') as f:
            try:
                tmp = pickle.load(f)
                self.name = tmp['name']
                self.group_members = tmp['data']
            except EOFError:
                pass

    def clearStudents(self):
        self.group_members.clear()
