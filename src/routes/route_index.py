from src import app
from flask import jsonify

@app.route("/")
def route_basic_main():
    return jsonify("hey !")