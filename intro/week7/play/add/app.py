# controller
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ["GET"])
def result():
    x = request.args.get("num1")
    y = request.args.get("num2")
    add = float(x) + float(y)
    return render_template("result.html", res=add, x=x, y=y)

@app.route("/php")
def php():
    return render_template("phpliteadmin.php")