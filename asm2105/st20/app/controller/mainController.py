from asm2105.st20.app.controller.Controller import Controller

class mainController(Controller):
    def start(self):
        return self._view('views/pages/start.html')