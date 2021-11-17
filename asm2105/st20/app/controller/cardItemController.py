from .Controller import Controller
from ..models.cardItem import cardItemTypes

from ..strategys.printStrategys import WebPrintStrategy
from ..strategys.setterStrategy import WebSetterStrategy


from ..models.workers.worker import worker
from ..models.students.student import student
from ..models.workers.teacher import teacher
from ..models.students.headman import headman

import json


class cardItemController(Controller):
    def get_attr_of_type(self, type):
        if type==cardItemTypes.worker.value:
            obj=worker
        elif type==cardItemTypes.student.value:
            obj=student
        elif type==cardItemTypes.teacher.value:
            obj=teacher
        elif type==cardItemTypes.headman.value:
            obj=headman

        attribs = obj.get_attribs()
        result = {}
        for attr, value in attribs.items():
            if attr!='type':
                result[attr] = {
                    'attr':attr,
                    'attrName': value[0],
                    'attrType': str(value[1].__name__)}

        result=json.dumps(result)

        return result



