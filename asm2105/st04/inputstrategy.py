from flask import request


class InputStrategy:
    @staticmethod
    def default(self, field):
        return request.form.get(field)
