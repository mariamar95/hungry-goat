from flask import render_template
from hungrygoat import app, db


@app.route("/")
def home():
    return render_template("home.html")