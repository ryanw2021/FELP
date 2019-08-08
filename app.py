'''
This is the backend!
'''
from flask import Flask, jsonify, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime as date

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'caponeses',
    'db': 'postgres',
    'host': 'hackathon-test.cqnlo7waapcg.us-east-1.rds.amazonaws.com',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    fundraisers = db.relationship('Fundraiser', backref='organization', lazy=True)

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    location = db.Column(db.String(), unique=True, nullable=False)
    business = db.relationship('Fundraiser', backref='business', lazy=True)

class Fundraiser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    start_date = db.Column(db.Datetime)
    end_date = db.Column(db.Datetime)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

if __name__=='__main__':
    app.run(debug=True)