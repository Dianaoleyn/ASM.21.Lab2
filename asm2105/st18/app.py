from flask import Flask, request
app = Flask(__name__)

from models.university import university
from strategys.storage import PickleStorage

univer=university(PickleStorage)