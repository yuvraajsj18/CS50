# this program generates an html page using python with the help of flask microframework 
# this is the controller of our web programming

from flask import Flask, render_template, request

app = Flask(__name__)   # this line initialises a flask application for our application.py

@app.route("/")     # this indicates that any request for "/"(root page) will be responded by the following function
def index():    # this is the function to handle "/" request conventionally called as index
    return "Hello, World"   # returning Hello World With Out HTML



