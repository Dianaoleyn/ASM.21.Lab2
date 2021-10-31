import pickle
from abc import ABC, abstractmethod

class BaseStorage(ABC):
    @abstractmethod
    def dump(self, data):
        pass

    @abstractmethod
    def load(self):
        pass

class PickleStorage(BaseStorage):
    def dump(self, data):
        with open('out.pickle', 'wb') as file:
            pickle.dump(data, file)

    def load(self):
        with open('out.pickle', 'rb') as file:
            return pickle.load(file)