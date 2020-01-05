# controller
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

WORDS = []
with open("large", 'r') as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods = ["GET"])
def search():
    query = request.args.get("q")
    words = [word for word in WORDS if query and word.startswith(query)]
    return jsonify(words)

