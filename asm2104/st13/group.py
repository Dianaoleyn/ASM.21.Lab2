from HtmlController import HtmlController

class Group:
    def __init__(self, strategy=HtmlController, view=HtmlController(), list=[]):
        self.list = list
        self.strategy = strategy
        self.controllerStrategy = view

    def addElement(self):
        self.list.append(self.controllerStrategy.addElement())

    def clearList(self):
        self.list.clear()

    def changeStrategy(self):
        return self.controllerStrategy.changeStrategy()

    def dump(self):
        return self.strategy.dump(self.list)

    def load(self):
        self.list = self.strategy.load()

    def getMenu(self):
        return self.controllerStrategy.getMenu(self)
