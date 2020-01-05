from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        changed_text = text * 3
        return render_template("res.html", text = changed_text)
    else:
        return render_template("index.html")
