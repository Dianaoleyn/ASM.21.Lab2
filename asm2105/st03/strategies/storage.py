from abc import ABC, abstractmethod
import pickle

class BaseStorage(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self):
        pass

class PickleStorage(BaseStorage):
    def save(self, data):
        with open('bogdanova_storage.db', 'wb') as file:
            pickle.dump(data, file)

    def load(self):
        with open('bogdanova_storage.db', 'rb') as file:
            return pickle.load(file)