'''
This is the backend!
'''
from flask import Flask, jsonify, render_template, request, url_for
from models import User

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

if __name__=='__main__':
    app.run()