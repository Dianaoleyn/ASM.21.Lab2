from FileIO import FileOutputPickle
from Employee import Employee
from Chief import Chief
from flask import request, render_template


class MenuKartoteka:
	def __init__(self, maxid=0, strategy=FileOutputPickle()):
		try:
			self.__cart = strategy.do_input()
			self.maxid = len(self.__cart)
		except (EOFError, FileNotFoundError):
			self.__cart = []
			self.maxid = maxid
		self.__strategy = strategy

	def add(self, case):
		if int(request.form.get('id', 0)) <= 0:
			self.maxid += 1
			employee = Chief() if case is not None else Employee()
			employee.input(request.form, self.maxid)
			self.__cart.append(employee)
			return self.print()
		else:
			employee = self.__cart[int(request.form.get('id', 0))-1]
			employee.input(request.form, self.maxid)
			return self.print()

	def print(self):
		if not self.__cart:
			return render_template('head.html') +\
				render_template('bottom.html')
		ret = ""
		for st in self.__cart:
			ret += st.output()
		return render_template('head.html') + \
			ret + render_template('bottom.html')

	def form_print(self, index):
		if index <= 0:
			return Employee().form_print()
		return self.__cart[index-1].form_print()

	def file_read(self):
		return self.__strategy.do_output(self.__cart)

	def file_write(self):
		self.__cart = self.__strategy.do_input()
		self.maxid = len(self.__cart)
		return

	def clear(self):
		self.maxid = 0
		return self.__cart.clear()

