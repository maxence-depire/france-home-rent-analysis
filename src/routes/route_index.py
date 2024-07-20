from src import app
from flask import render_template


@app.route("/")
def route_basic_main():
    return render_template('index.html')