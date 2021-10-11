import os
from .models.university import university
from .strategys.storageStrategys import PickleStorageStrategy

FLASK_APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Flask
from flask import Flask, url_for, request
app = Flask(__name__)

# Config
app.config.from_object('app.config.DevelopmentConfig')

def get_university():
    return university(PickleStorageStrategy())