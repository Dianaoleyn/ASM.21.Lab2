from Assistant import Assistant
from Teacher import Teacher
from FileDatabase import FileDatabase

from flask import render_template

class GroupIndex:
    def __init__(self) -> None:
        self.__strategies = {}
        self.__strategies[Assistant.type()] = Assistant
        self.__strategies[Teacher.type()] = Teacher
        self.__index = []
        self.__database = FileDatabase()

    def add(self, member_type, name, age):
        self.__index.append(self.__strategies[member_type](len(self.__index), name, age))
    
    def show(self):
        header = render_template('mainpage_top.html')
        for member in self.__index:
            header += member.print()
        
        return header + render_template('mainpage_bottom.html')

    def clear(self):
        self.__index.clear()

    def save(self):
        members = []
        for member in self.__index:
            members.append( (member.type(), member.serialize()) )
        self.__database.write(members)

    def load(self):
        self.clear()
        for member_type, serialized_member in self.__database.load():
            self.__index.append(self.__strategies[member_type].get_instance(serialized_member))

        


