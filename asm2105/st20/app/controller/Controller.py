from flask import render_template

class Controller:
    def _view(self, template_file, args=None):
        return render_template(template_file, context=args)