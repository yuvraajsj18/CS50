# controller
from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods = ["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    dorm = request.form.get("dorm")
    if not name or not email or not dorm:
        return render_template("failure.html")
    message = "You are Registered " + name + dorm  # string to send in email
    server = smtplib.SMTP("smtp.gmail.com", 587)   # sets the server to use for sending email here gmail
    server.starttls()
    server.login("yuvraajsj18@gmail.com", "password")
    server.sendmail("yuvraajsj18@gmail.com", email, message)
    return render_template("success.html")