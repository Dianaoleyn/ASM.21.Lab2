from inp_out import StrategyIO
from storage import Storage


class Group:
	members = []

	def __init__(self, strategy_io: StrategyIO, strategy_storage: Storage):
		self._strategy_io = strategy_io
		self._strategy_storage = strategy_storage

	@property
	def strategy_io(self) -> StrategyIO:
		"""
		Cообщит класс стратегии ввода вывода
		:return:
		"""
		return self._strategy_io

	@property
	def strategy_storage(self) -> Storage:
		"""
		Cообщит класс стратегии хранения
		:return:
		"""
		return self._strategy_storage

	@strategy_io.setter
	def strategy_io(self, strategy: StrategyIO) -> None:
		"""
		Поменять стратегию ввода/вывода в интерактивном режиме
		:param strategy:
		:return:
		"""
		self._strategy_io = strategy

	@strategy_storage.setter
	def strategy_storage(self, strategy: Storage) -> None:
		"""
		Поменять стратегию хранения в интерактивном режиме
		:param strategy:
		:return:
		"""
		self._strategy_storage = strategy

	def add(self, person, request):
		"""
		Заполнить участника в соответствии со стратегией
		:param person:
		:return:
		"""
		self._strategy_io.enter(person, request)
		self.members.append(person)

	def members_show(self):
		"""
		Выведет всех участников
		:return:
		"""
		self._strategy_io.output(self.members)

	def members_from_file(self):
		"""
		Загрузит участников с файла
		:return:
		"""
		self.members = self._strategy_storage.input()

	def members_in_file(self):
		"""
		Запишет участников в файл
		:return:
		"""
		self._strategy_storage.output(self.members)

	def delete_members(self):
		"""
		Почистить список участников
		:return:
		"""
		del self.members[:]

