from student import Student
from Student_VUC import Student_VUC
from StrategyFileIO import StrategyFileIO
from StrategyIO import StrategyIO


class Group:
	cartoteka = []

	def __init__(self, strategyFile : StrategyFileIO , strategyIO : StrategyIO):
		self._strategyIO = strategyIO
		self._strategyFile = strategyFile

	@property
	def strategyIO(self) -> StrategyIO:
		return self._strategyIO

	@property
	def strategyFile(self) -> StrategyFileIO:
		return self._strategyFile

	@strategyIO.setter
	def strategyIO(self, strategy: StrategyIO) ->None:
		self._strategyIO = strategy

	@strategyFile.setter
	def strategyFile(self, strategy: StrategyFileIO) ->None:
		self._strategyFile = strategy

	def addStudent(self, person, request):
		self._strategyIO.enter(person,request)
		self.cartoteka.append(person)

	def print_cartoteka(self):   #распечатает всех из картотеки
		self._strategyIO.printout(self.cartoteka)

	def cartoteka_from_file(self): #загрузит с файла в картотеку
		self.cartoteka = self._strategyFile.input()

	def cartoteka_in_file(self): #выгрузит картотеку в файл
		self._strategyFile.output(self.cartoteka)

	def clear_kartoteka(self):
		del self.cartoteka[:]

	def cartoteka_edit_person(self):
		index = int(input(f"Id персонажа(целое положительное): "))
		try:
			person = self.cartoteka[index]
		except IndexError:
			print(f"Такого персонажа нет в картотеке")
			'''self.fill_in_console(person)'''






