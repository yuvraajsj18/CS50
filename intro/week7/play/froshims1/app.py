# controller

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# registered students
students = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods = ["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    else:
        students.append(f"{name} from {dorm}")
        return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", students = students)

