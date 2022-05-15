from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",content="it works")

@app.route("/login/", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["usrname"]
        return redirect(url_for("usr", usr = user))
    return render_template("form.html")

@app.route("/<usr>")
def usr(usr):
    return render_template("user.html", usr=usr)

if __name__=="__main__":
    app.run(debug=True)