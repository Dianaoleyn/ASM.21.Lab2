import json

from . import app, request
from . import controller

# @app.route('/')
# def main_page():
#     # return run_function_of_modeule('mainController', 'index')
#     return controller.mainController.mainController().start()
#
# @app.route('/university')
# def show_university_page():
#     return controller.universityController.universityController().index()
#
# @app.route('/getattribs', methods=['GET'])
# def get_attribs():
#     if request.args['type'] is not None and request.args['type'] != '0':
#         return controller.universityController.universityController().get_obj_attribs(request.args['type'])
#
# @app.route('/action', methods=['POST', 'GET'])
# def append_user():
#     # print(request.form['type'])
#     if request.method=='POST':
#         if request.form['type'] is not None and request.form['type']!='0':
#             return controller.universityController.universityController().action(request.form)
#     else:
#         return controller.universityController.universityController().action(request.args)
@app.route('/')
def main_page():
    return controller.mainController.mainController().index()

@app.route('/getattr')
def get_attr():
    return controller.cardItemController.cardItemController().get_attr_of_type(request.args['userType'])

@app.route('/add-user', methods=['POST'])
def add_user():
    # print(request.get_json(), type(request.get_json()))
    req_data=request.get_json()
    return controller.universityController.universityController().add_user(req_data)

@app.route('/change-user', methods=['POST'])
def change_user():
    req_data=request.get_json()
    return controller.universityController.universityController().change_user(req_data)

@app.route('/delete-user', methods=['POST'])
def delete_user():
    req_data=request.get_json()
    return controller.universityController.universityController().delete_user(int(req_data['id']))

