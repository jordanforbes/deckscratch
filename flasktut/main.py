import re
from flask import Flask, template_rendered, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",content="it works")

@app.route("/<usr>")
def usr(usr):
    return render_template("user.html", usr=usr)

if __name__=="__main__":
    app.run(debug=True)