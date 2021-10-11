from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py') and f.endswith('Controller.py')]

import importlib

for i in __all__:
    importlib.import_module(f'asm2105.st20.app.controller.{i}')