from asm2105.st20.app import app, request
from asm2105.st20.app import controller

@app.route('/')
def main_page():
    # return run_function_of_modeule('mainController', 'index')
    return controller.mainController.mainController().start()

@app.route('/university')
def show_university_page():
    return controller.universityController.universityController().index()

@app.route('/getattribs', methods=['GET'])
def get_attribs():
    if request.args['type'] is not None and request.args['type'] != '0':
        return controller.universityController.universityController().get_obj_attribs(request.args['type'])

@app.route('/action', methods=['POST', 'GET'])
def append_user():
    # print(request.form['type'])
    if request.form['type'] is not None and request.form['type']!='0':
        return controller.universityController.universityController().action(request.form)