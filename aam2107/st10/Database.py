from enum import IntEnum

class DatabaseType(IntEnum):
    FILE = 1
    POSTGRES = 2

class Database:
    def __init__(self) -> None:
        pass

    def write(self, members):
        raise RuntimeError("Try to call 'write' method from abstract class 'Database'")

    def load(self):
        raise RuntimeError("Try to call 'load' method from abstract class 'Database'")