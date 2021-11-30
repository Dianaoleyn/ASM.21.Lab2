from Member import Member, MemberType

from flask import render_template

class Teacher(Member):
    def __init__(self, id = None, name = None, age = None) -> None:
        super().__init__()
        self.__id = id
        self.__name = name
        self.__age = age

    def print(self):
        return render_template('member_render.html', member=f'Teacher {self.__name}, age: {self.__age}')

    @staticmethod
    def type():
        return MemberType.TEACHER

    def serialize(self):
        return {"id": self.__id, "name": self.__name, "age": self.__age}

    @staticmethod
    def get_instance(serialized_member):
        return Teacher(serialized_member["id"], serialized_member["name"], serialized_member["age"])