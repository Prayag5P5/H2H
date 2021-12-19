from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:////mnt/c/Users/<username>/Documents/login_example/login.db'
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

# @app.route('/')
# def index():
#     user = User.query.filter_by(username='Prayag').first()
#     login_user(user)
#     return 'You are now logged in!'


# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return 'You are now logged out!'


# @app.route('/home')
# @login_required
# def home():
#     return 'The current user is ' + current_user.username

if __name__ == "main":
    app.run(debug=True)