from enum import IntEnum

class MemberType(IntEnum):
    ASSISTANT = 1
    TEACHER = 2

class Member:
    def __init__(self) -> None:
        pass

    def print(self):
        raise RuntimeError("Try to call 'print' method from abstract class 'Member'")

    def type(self):
        raise RuntimeError("Try to call 'type' method from abstract class 'Member'")

    @staticmethod
    def serialize():
        raise RuntimeError("Try to call 'serialize' method from abstract class 'Member'")

    @staticmethod
    def get_instance(serialized_member):
        raise RuntimeError("Try to call 'get_instance' method from abstract class 'Member'")
