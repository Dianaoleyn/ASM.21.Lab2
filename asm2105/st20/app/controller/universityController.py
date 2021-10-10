from asm2105.st20.app.controller.Controller import Controller
from asm2105.st20.app import get_university
from asm2105.st20.app.models.students.student import student
from asm2105.st20.app.models.students.headman import headman
from asm2105.st20.app.models.workers.worker import worker
from asm2105.st20.app.models.workers.teacher import teacher
from asm2105.st20.app.strategys.printStrategys import WebPrintStrategy
from asm2105.st20.app.strategys.setterStrategy import WebSetterStrategy

import json

class universityController(Controller):
    def index(self):
        return self._view('views/pages/university.html', {'university_name': get_university().name})

    def cardItemClassByTypeId(self, type):
        if int(type) == 1:
            return student
        elif int(type) == 2:
            return headman
        elif int(type) == 3:
            return worker
        elif int(type) == 4:
            return teacher
        else:
            raise Exception(f'type {type} dont exist')

    def get_obj_attribs(self, type):
        attr=self.cardItemClassByTypeId(type).get_attribs()

        attribs = {}
        for key, value in attr.items():
            attribs[key] = [value[0], str(value[1].__name__)]

        return json.dumps(attribs)

    def action(self, form):
        if form['action']=='append':
            obj=self.cardItemClassByTypeId(form['type'])(print=WebPrintStrategy, setter=WebSetterStrategy)
            obj.set_data(form)
            get_university().append_user(obj)
            get_university().save()
            return 'true'
