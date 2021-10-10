from abc import ABC, abstractmethod
import pickle

class BaseStorageStrategy(ABC):
    @abstractmethod
    def load(self, db_name):
        pass

    @abstractmethod
    def save(self, data, db_name):
        pass


class PickleStorageStrategy(BaseStorageStrategy):
    def load(self, db_name):
        with open(f'{db_name}.pickle', 'rb') as file:
            return pickle.load(file)

    def save(self, data, db_name):
        with open(f'{db_name}.pickle', 'wb') as file:
            pickle.dump(data, file)