from Html import Html
from Console import Console
from File import File

strategy_type = [
    {'title': 'File', 'class': File},
    {'title': 'Console', 'class': Console},
    {'title': 'HTML5', 'class': Html}
]


class Company:
    def __init__(self):
        self.strategy = Html
        self.employee_list = dict()

    def get_menu(self):
        return self.strategy.menu(self)  # return?

    def add_employee(self):
        self.strategy.input(self.employee_list)

    def edit_employee(self, id=0):
        self.strategy.edit(self.employee_list, id)

    def delete_employee(self, id=0):
        self.strategy.delete(self.employee_list, id)

    def clear_employee_list(self):
        self.strategy.clear(self.employee_list)

    def show_employee_list(self):
        return self.strategy.output(self.employee_list)

    def input_employee_list(self):
        previous_strategy = self.strategy
        self.strategy = self.strategy.change_strategy(strategy_type)
        self.employee_list = self.strategy.input(self.employee_list)
        self.strategy = previous_strategy

    def output_employee_list(self):
        previous_strategy = self.strategy
        self.strategy = self.strategy.change_strategy(strategy_type)
        self.strategy.output(self.employee_list)
        self.strategy = previous_strategy

    def change_strategy(self):
        self.strategy = self.strategy.change_strategy(strategy_type[1:])
