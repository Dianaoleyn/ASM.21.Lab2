from abc import ABC, abstractmethod
from typing import List
import pickle


class StrategyFileIO(ABC):
    def input(self):
        pass

    def output(self, data: List):
        pass


class FileIO(StrategyFileIO):
    def input(self):
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)

    def output(self, members: List):
        with open('data.pickle', 'wb') as f:
            pickle.dump(members, f)