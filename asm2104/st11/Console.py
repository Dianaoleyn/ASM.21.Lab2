from Lead import Lead
from Developer import Developer

employee_type = [
    {'title': 'Lead', 'class': Lead},
    {'title': 'Developer', 'class': Developer}
]


class Console:

    @staticmethod
    def menu(company):
        menu = [
            {'title': 'Add employee', 'method': company.add_employee},
            {'title': 'Edit employee', 'method': company.edit_employee},
            {'title': 'Delete employee', 'method': company.delete_employee},
            {'title': 'Clear', 'method': company.clear_employee_list},
            {'title': 'Show all employees', 'method': company.show_employee_list},
            {'title': 'Input data', 'method': company.input_employee_list},
            {'title': 'Output data', 'method': company.output_employee_list},
            {'title': 'Change strategy', 'method': company.change_strategy},
        ]
        while True:
            if company.strategy == Console:
                for i in range(len(menu)):
                    print('{0}. {1}'.format(i+1, menu[i]['title']))
                select = int(input()) - 1
                if 0 <= select < int(len(menu)):
                    menu[select]['method']()
                else:
                    print('This menu item does not exist')
            else:
                print('{0} is working now.'.format(company.strategy.__name__))
                input()

    @staticmethod
    def input(employee_list):
        print('Choose who to add:')
        for i in range(len(employee_type)):
            print('{0}. {1}'.format(i + 1, employee_type[i]['title']))
        select = int(input()) - 1
        if 0 <= select < len(employee_type):
            try:
                new_id = max(employee_list.keys()) + 1
            except:
                new_id = 1
            employee_list[new_id] = employee_type[select]['class'](new_id)
        else:
            print('This menu item does not exist')
        return employee_list

    @staticmethod
    def output(employee_list):
        for i in employee_list.keys():
            print(employee_list[i])

    @staticmethod
    def edit(employee_list, id):
        print('Choose employee ID to edit:')
        id_select = int(input())
        if id_select in employee_list.keys():
            for i in range(len(employee_type)):
                print('{0}. {1}'.format(i + 1, employee_type[i]['title']))
            type_select = int(input()) - 1
            if 0 <= type_select < len(employee_type):
                employee_list[id_select] = employee_type[type_select]['class'](id_select)
            else:
                print('This menu item does not exist')
        else:
            print('This menu item does not exist')
        return employee_list

    @staticmethod
    def delete(employee_list, id):
        print('Choose employee ID to delete:')
        id_select = int(input())
        if id_select in employee_list.keys():
            del employee_list[id_select]
        else:
            print('This menu item does not exist')
        return employee_list

    @staticmethod
    def clear(employee_list):
        print('Do you really want to clear the data?\nPress 9 to confirm or any button to cancel')
        select = input()
        if select == '9':
            employee_list.clear()
        else:
            pass
        return employee_list

    @staticmethod
    def change_strategy(strategy_type):
        print('Select strategy')
        for i in range(len(strategy_type)):
            print('{0}. {1}'.format(i + 1, strategy_type[i]['title']))
        select = int(input()) - 1
        if 0 <= select < len(strategy_type):
            strategy = strategy_type[select]['class']
        else:
            print('This menu item does not exist')
        return strategy
