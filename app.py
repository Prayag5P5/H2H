from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/")
def hello_world():
    return render_template("index.html")
    
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["uname"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html")

    else:
        return redirect(url_for("login"))

if __name__ == "main":
    app.run(debug=True)