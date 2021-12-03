from flask import Flask, render_template
from datetime import datetime
import re
import csv


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/boats/")
def boats():
    return render_template("boats.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/data/")
def data():
    return render_template("data.html")
