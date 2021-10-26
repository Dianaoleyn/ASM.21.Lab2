from HtmlController import HtmlController
from file import File


class Shop:
    employeeList = []
    strategy = File()
    view = HtmlController()

    def addEmployee(self):
        self.employeeList.extend(self.view.getEmployees())
        self.strategy.showEmployees(self.employeeList)

    def clearEmployees(self):
        self.employeeList.clear()

    def showEmployees(self):
        return self.strategy.showEmployees(self.employeeList)

    def changeStrategy(self):
        return self.view.changeStrategy()

    def getEmployees(self):
        self.employeeList.extend(self.strategy.getEmployees())

    def getMenu(self):
        return self.view.getMenu(self, self.employeeList)
