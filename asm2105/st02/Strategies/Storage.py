from abc import ABC, abstractmethod
import pickle

class BaseStorage(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self, data):
        pass

class PickleStorage(BaseStorage):
    def load(self):
        with open('file.db', 'rb') as file:
            # print('load', pickle.load(file))
            return pickle.load(file)

    def save(self, data):
        with open('file.db', 'wb') as file:
            # print('save', data)
            pickle.dump(data, file)

