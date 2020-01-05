# controller
from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")   # create database for registrants using cs50 SQL lib

# CREATE TABLE registrants(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name VARCHAR(255) NOT NULL,
# dorm VARCHAR(255));

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods = ["GET"])
def register():
    name = request.args.get('name')
    dorm = request.args.get('dorm')
    if not name or not dorm:
        return render_template("failure.html")
    db.execute("INSERT INTO registrants (name, dorm) values (:name, :dorm);", name = name, dorm = dorm)
    return render_template("success.html")

@app.route("/registered")
def registered():
    rows = db.execute("SELECT * FROM registrants;")
    return render_template("registrants.html", rows = rows)
    
    