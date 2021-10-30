"""
Файл  стратегий хранения
"""

import pickle
from abc import ABC, abstractmethod
from typing import List


class Storage(ABC):
    def input(self):
        pass

    def output(self, data: List):
        pass


class InputOutPutFile(Storage):
    def input(self):
        with open('members.pickle', 'rb') as f:
            return pickle.load(f)

    def output(self, members: List):
        with open('members.pickle', 'wb') as f:
            pickle.dump(members, f)
