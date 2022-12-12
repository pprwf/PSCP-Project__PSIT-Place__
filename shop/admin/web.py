from flask import Flask, render_template, request, redirect, url_for, flash
from shop import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///psit.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("keyboard.html")

@app.route('/type')
def category():
    return render_template("category.html")

@app.route("/info")
def profile():
    name = ""
    return render_template("profile.html", name=name)

@app.route("/favorite")
def fav():
    return render_template("fav.html")

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
