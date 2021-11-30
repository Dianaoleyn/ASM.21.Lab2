from Database import Database, DatabaseType
import pickle


class FileDatabase(Database):
    def __init__(self) -> None:
        super().__init__()

    def write(self, data):
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)

    def load(self):
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)