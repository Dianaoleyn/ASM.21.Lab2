import pickle


class FileStorage:
    def __init__(self):
        self.load()

    def dump(self):
        with open('asm2105/st17/storage.pickle', 'wb') as f:
            pickle.dump(self.__array, f)

    def load(self):
        try:
            with open('asm2105/st17/storage.pickle', 'rb') as f:
                self.__array = pickle.load(f)
        except FileNotFoundError:
            self.__array = []

    def get_all_elements(self):
        return self.__array

    def get_element(self, id):
        return self.__array[self.__find_index_by_id(id)]

    def delete_all_elements(self):
        self.__array.clear()

    def delete_element(self, id):
        self.__array.pop(self.__find_index_by_id(id))

    def add_element(self, element):
        try:
            element.id = max(i.id for i in self.__array) + 1
        except ValueError:
            element.id = 1
        self.__array.append(element)

    def edit_element(self, element):
        self.__array[self.__find_index_by_id(element.id)] = element

    def __find_index_by_id(self, id):
        for index in range(len(self.__array)):
            if self.__array[index].id == id:
                return index
