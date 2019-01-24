from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route("/names")
def output_names():
    all_names = set(["Hassan", "Kasim"])
    return render_template("index.html", all_names=all_names)


notes = []

@app.route("/notes", methods = ["POST","GET"])
def output_names():
    return render_template("index.html", all_names=all_names)
