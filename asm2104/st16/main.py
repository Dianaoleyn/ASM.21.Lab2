from flask import Flask, url_for, request, render_template, Markup, redirect

app = Flask(__name__)




# @app.route('/')
# def main():
#     return render_template('main.html')
#
# @app.route('/show.html')
# def show_page():
#     return render_template('show.html')



# @app.route('/add_element')
# def add_member():
#     return render_template('add_element_form.html')
#
# @app.route('/add-new', methods=['POST'])
# def add_new():
#     print(request.form)
#     if request.form['add-name'] is None or request.form['add-name']=='' or request.form['add-age'] is None or request.form['add-age']=='':
#         return 'Invalid input form'
#
#     if request.form['add-group'] is not None and request.form['add-group']!='':
#         if request.form['add-email'] is not None and request.form['add-email']!='':
#             member=leader()
#         else:
#             member=student()
#     else:
#         if request.form['add-subject'] is not None and request.form['add-subject']!='':
#             member=teacher()
#         elif request.form['add-phone'] is not None and request.form['add-phone']!='' and request.form['add-cabinet'] is not None and request.form['add-cabinet']!='':
#             member=director()
#         else:
#             member=employe()
#
#     member.input(Web)
#     print(member.__dict__)
#     try:
#         fl.load(PickleStorage)
#     except:pass
#     fl.add_member(member)
#     fl.store(PickleStorage)
#
#     return redirect('/')
#
# @app.route('/clear')
# def clear():
#     fl.clr()
#     fl.store(PickleStorage)
#     return redirect('/')
#
# @app.route('/refactor/<int:id>', methods=['POST', 'GET'])
# def refactor(id):
#     try:
#         fl.load(PickleStorage)
#     except:
#         return "can't load file"
#     member = fl.get_member(int(id))
#
#     if request.method=='GET':
#         return render_template('refactor_element.html', context={'member':member})
#     else:
#         member.input(Web)
#         fl.store(PickleStorage)
#         return redirect('/')
#
# @app.route('/search')
# def search():
#     param=request.args['search-param']
#
#     try:
#         fl.load(PickleStorage)
#     except:
#         return "can't load file"
#     result=fl.get_member(param)
#     if type(result) is list:
#         context = [Markup(member.output(Web)) for member in result]
#
#     else:
#         context=[Markup(result.output(Web))]
#     return render_template('main.html', context={'members': context})

if __name__ == '__main__':
    app.run(debug=True)