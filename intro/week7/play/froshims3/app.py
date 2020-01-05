# controller
from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    with open("registered.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow((name, dorm))
    return render_template("success.html")

@app.route("/registered")
def registered():
    try:
        file = open("registered.csv", 'r')
    except:
        return "No Registration Yet"
    reader = csv.reader(file)
    students = list(reader)
    return render_template("registered.html", students = students)