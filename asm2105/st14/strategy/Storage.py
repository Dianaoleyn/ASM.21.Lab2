from abc import ABC, abstractmethod
import pickle

class BaseStorage(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self, data):
        pass


class Pickle(BaseStorage):
    def load(self):
        with open('storage.db', 'rb') as file:
            return pickle.load(file)

    def save(self, data):
        with open('storage.db', 'wb') as file:
            pickle.dump(data, file)