from abc import ABC, abstractmethod
import pickle


class FileOutputInterface(ABC):
    @abstractmethod
    def do_input(self):
        pass

    @abstractmethod
    def do_output(self, data):
        pass


class FileOutputPickle(FileOutputInterface):
    def do_input(self):
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)

    def do_output(self, data):
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)


class FileOutputShelve(FileOutputInterface):
    def do_input(self):
        pass

    def do_output(self, data):
        pass

