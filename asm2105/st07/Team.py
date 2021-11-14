from .Player import Player
from .Captain import Captain
from flask import request, render_template
import pickle


class Team:
    def __init__(self, maxid=0):
		self.teamMember = []
		self.id_max = maxid

	def add(self, case):
		if int(request.form.get('id', 0)) <= 0:
			self.id_max += 1
			player = Captain() if case is not None else Player()
			player.input(request.form, self.id_max)
			self.teamMember.append(player)
			return self.print()
		else:
			player = self.teamMember[int(request.form.get('id', 0)) - 1]
			player.input(request.form, self.id_max)
			return self.print()

	def change(self):
		index = int(input("Введите номер студента, которого нужно изменить"))
		self.teamMember[index - 1].input()

	def print(self):
		if not self.teamMember:
			return render_template('head.html') +\
				render_template('bottom.html')
		ret = ""
		for st in self.teamMember:
			ret += st.output()
		return render_template('head.html') + \
			ret + render_template('bottom.html')

	def form_print(self, index):
		if index <= 0:
			return Player().form_print()
		return self.teamMember[index - 1].form_print()

	def read_file(self):
		f = open('team.dat', 'rb')
		self.teamMember = pickle.load(f)
		self.id_max = len(self.teamMember)
		return self.teamMember

	def write_file(self):
		f = open('team.dat', 'wb')
		pickle.dump(self.teamMember, f)
		return

	def clear(self):
		self.id_max = 0
		return self.teamMember.clear()