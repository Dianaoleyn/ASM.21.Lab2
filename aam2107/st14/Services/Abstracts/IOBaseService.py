from abc import ABC, abstractmethod


class IOBaseService(ABC):

    @abstractmethod
    def input(self, obj):
        """Ввод"""
        pass

    @abstractmethod
    def output(self, obj):
        """Вывод"""
        pass
