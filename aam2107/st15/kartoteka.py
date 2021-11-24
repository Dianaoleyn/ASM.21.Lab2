from FileIO import FileOutputPickle
from Student import Student as St
from Captain import Captain as Cap
from flask import request, render_template


class MenuCartoteka:
	def __init__(self, maxid=0, strategy=FileOutputPickle()):
		self.__cart = []
		self.__strategy = strategy
		self.maxid = maxid

	def add(self, case):
		if int(request.form.get('id', 0)) <= 0:
			self.maxid += 1
			student = Cap() if case is not None else St()
			student.input(request.form, self.maxid)
			self.__cart.append(student)
			return self.print()
		else:
			student = self.__cart[int(request.form.get('id', 0))-1]
			student.input(request.form, self.maxid)
			return self.print()

	def change(self):
		index = int(input("Введите номер студента, которого нужно изменить"))
		self.__cart[index - 1].input()

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
			return St().form_print()
		return self.__cart[index-1].form_print()

	def file_read(self):
		return self.__strategy.do_output(self.__cart)

	def file_write(self):
		self.__cart = self.__strategy.do_input()
		return

	def clear(self):
		self.maxid = 0
		return self.__cart.clear()

