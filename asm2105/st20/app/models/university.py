
class university:
    def __init__(self, storage, db_name='university', name='Оксфорд'):
        self._name=name
        self._users={}

        self.db_name=db_name
        self._storage = storage
        try:
            self.load()
        except:pass

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> None:
        self._name = name

    def load(self):
        data=self._storage.load(self.db_name)
        # print(data)
        self._users=data['users']
        self._name=data['name']

    def save(self):
        data = {
            'users': self._users,
            'name': self._name
        }
        # print(data)
        self._storage.save(data, self.db_name)

    def append_user(self, user):
        user.id=len(self._users)
        self._users[user.id]=user

    def get_users(self):
        return self._users

    def get_user_or_none_by_name(self, name):
        result=[]
        for user in self._users.values():
            if user.name==name:
                result.append(user)
        if len(result)!=0:
            return result
        else:
            return None

    def get_user_or_none_by_id(self, id):
        if int(id) in self._users:
            return self._users[int(id)]
        else:
            return None

    def clear(self):
        self._users.clear()