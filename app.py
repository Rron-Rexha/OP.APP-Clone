import re
from datetime import datetime

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/champions")
def  champions():
     return render_template('champions.html')

@app.route("/sign_in")
def sign_in():
     return render_template('sign_in.html')


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
     return render_template("hello_there.html", name=name, date=datetime.now())


if __name__ == "__main__":
     app.run(debug=True)