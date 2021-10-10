from HtmlController import HtmlController
from Console import Console


class Shop:
    employeeList = []
    strategy = Console()
    view = HtmlController()

    def addEmployee(self):
        self.employeeList.append(self.view.getEmployees())

    def clearEmployees(self):
        self.employeeList.clear()

    def showEmployees(self):
        return self.strategy.showEmployees(self.employeeList)

    def changeStrategy(self):
        return self.view.changeStrategy()

    def getEmployees(self):
        self.employeeList = self.strategy.getEmployees()

    def getMenu(self):
        return self.view.getMenu(self)
