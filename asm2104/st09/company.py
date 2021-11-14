class Company:
    __array = []

    def __init__(self, array):
        self.__array = array

    def clearAllElements(self):
        return self.__array.clear()

    def addElements(self, strategy):
        return self.__array.extend(strategy.load())

    def getElements(self, strategy):
        return strategy.dump(self.__array)
