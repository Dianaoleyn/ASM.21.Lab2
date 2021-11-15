from asm2105.st20.app.controller.Controller import Controller
from asm2105.st20.app import get_university
from asm2105.st20.app.models.cardItem import cardItemTypes

class mainController(Controller):
    def start(self):
        return self._view('views/pages/start.html')

    def index(self):
        result = {}
        for key, user in get_university().get_users().items():
            result[key]=user.print()

        userTypes=[tp.value for tp in cardItemTypes if tp!=cardItemTypes.empty]

        return self._view('views/pages/main.html', args={'users':result, 'userTypes':userTypes})