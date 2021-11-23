from abc import ABC, abstractmethod


class BaseContainer(ABC):

    @abstractmethod
    def store_to_file(self):
        """Запись в файл"""
        pass

    @abstractmethod
    def load_from_file(self):
        """Чтение из файла"""
        pass

    @abstractmethod
    def clear_file(self):
        """Очистить файл"""
        pass
