import flask

app = flask.Flask(__name__, template_folder='../templates')

from src.routes import *