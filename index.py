import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def page0():
    greeting = random.choice(["Hi there!", "Hello!", "Greetings!"])
    return render_template("page0.html", greeting=greeting)

@app.route("/page1")
def page1():
    return render_template("page1.html")
