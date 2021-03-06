from .Controller import Controller
from app import get_university
from ..models.students.student import student
from ..models.students.headman import headman
from ..models.workers.worker import worker
from ..models.workers.teacher import teacher
from ..strategys.printStrategys import WebPrintStrategy
from ..strategys.setterStrategy import WebSetterStrategy

from ..models.cardItem import cardItemTypes
from flask import request

import json

class universityController(Controller):
    def add_user(self, request_data):
        if request_data['userType']==cardItemTypes.student.value:
            obj=student(print=WebPrintStrategy, setter=WebSetterStrategy)
        elif request_data['userType']==cardItemTypes.worker.value:
            obj=worker(print=WebPrintStrategy, setter=WebSetterStrategy)
        elif request_data['userType']==cardItemTypes.headman.value:
            obj=headman(print=WebPrintStrategy,setter=WebSetterStrategy)
        elif request_data['userType']==cardItemTypes.teacher.value:
            obj=teacher(print=WebPrintStrategy, setter=WebSetterStrategy)

        try:
            obj.set()

            univer=get_university()
            # univer.load()
            univer.append_user(obj)
            univer.save()
            return '1'
        except Exception as err:
            print(err)
            return '0'

    def change_user(self, request_data):
        try:
            # print(request_data)
            univer=get_university()
            user_buffer=univer.get_user_or_none_by_id(int(request_data['id']))
            user_buffer.set()
            # for attr, value in request_data['attributes'].items():
            #     user_buffer.__setattr__(attr,value)

            univer.get_users()[user_buffer.id]=user_buffer
            univer.save()
            return '1'
        except Exception as err:
            print(err)
            return '0'

    def delete_user(self, id):
        try:
            univer=get_university()
            univer.get_users().pop(int(id))
            univer.save()
            return '1'
        except Exception as err:
            print(err)
            return '0'