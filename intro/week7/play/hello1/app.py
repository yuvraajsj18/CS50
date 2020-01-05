# controller
# this file improves on hello0 by returning a template instead of directly returning a string so it indeed returns an actual html
# also this will say hello 'name' instead of just hello world

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name = request.args.get("name", "world"))