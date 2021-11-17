from Lead import Lead
from Developer import Developer
from flask import render_template, request


class Html:

    @staticmethod
    def menu(company):
        return company.show_employee_list()

    @staticmethod
    def input(employee_list):
        try:
            new_id = max(employee_list.keys()) + 1
        except:
            new_id = 1
        if request.form.get('department'):
            st = Lead(new_id,
                      request.form.get('full_name'),
                      request.form.get('lead'),
                      request.form.get('salary'),
                      request.form.get('department'))
            employee_list[new_id] = st
        elif request.form.get('qualification'):
            st = Developer(new_id,
                           request.form.get('full_name'),
                           request.form.get('developer'),
                           request.form.get('salary'),
                           request.form.get('qualification'))
            employee_list[new_id] = st
        return employee_list

    @staticmethod
    def output(employee_list):
        return render_template('employee_list.html', employee_list=employee_list.values())

    @staticmethod
    def edit(employee_list, id):
        if request.form.get('department'):
            st = Lead(id,
                      request.form.get('full_name'),
                      request.form.get('lead'),
                      request.form.get('salary'),
                      request.form.get('department'))
        else:
            st = Developer(id,
                           request.form.get('full_name'),
                           request.form.get('developer'),
                           request.form.get('salary'),
                           request.form.get('qualification'))
        employee_list[id] = st
        return employee_list

    @staticmethod
    def delete(employee_list, id):
        del employee_list[id]
        return employee_list

    @staticmethod
    def clear(employee_list):
        employee_list.clear()
        return employee_list

    @staticmethod
    def change_strategy(strategy_type):
        # render_template('change_strategy.html', classes=strategy_type)
        for i in strategy_type:
            if i.get('title') == request.form.get('class'):
                strategy = i.get('class')
        return strategy
