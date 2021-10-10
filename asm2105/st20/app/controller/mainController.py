from ..controller.Controller import Controller

class mainController(Controller):
    def start(self):
        return self._view('views/pages/start.html')