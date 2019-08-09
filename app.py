from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

import datetime as date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'

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
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    following = db.relationship('Follows', backref='user', lazy = True)

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    fundraisers = db.relationship('Fundraiser', backref='organization', lazy=True)
    followers = db.relationship('Follows', backref='organization', lazy = True)

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), unique=True, nullable=False)
    address = db.Column(db.String(), unique=True, nullable=False)
    fundraisers = db.relationship('Fundraiser', backref='business', lazy=True)

class Fundraiser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    description = db.Column(db.String(), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    
class Follows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def index():
    fundraisers = Fundraiser.query.order_by(Fundraiser.start_date).all()
    lib = {}
    for fund in fundraisers:
        lib[fund.business.title] = fund.business.address

    print(lib)

    return render_template("index.html", fundraisers = fundraisers, addresses=lib)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def login2():
    info = request.form
    print(info['password'])
    user = User.query.filter_by(email=info['email']).first()
    if user is None:
        return render_template("login.html", message="This email is not in our system!")
    elif user and user.password != info['password']:
        return render_template("login.html", message="Incorrect password")
    else:
        login_user(user)
        return redirect(url_for("customerProfile"))


@app.route("/newAccount")
def newAccount():
    return render_template("newAccount.html")

@app.route("/newAccount", methods = ["POST"])
def newAccount2():
    info = request.form
    if User.query.filter_by(email=info['email']).first() == None:
        print("User is able to create an account!")
        newUser = User(email=info['email'], password=info['password'], name=info['fname'] + ' ' + info['lname'] )
        db.session.add(newUser)
        db.session.commit()
        print("Added New User")
        return render_template("login.html", message="Account has been created!")
    else:
        return render_template("newAccount.html", message="You already have an account!")

@app.route("/customerProfile")
@login_required
def customerProfile():
    organizations = Organization.query.order_by(Organization.title).all()
    follows = Follows.query.filter_by(user_id=current_user.id).order_by(Follows.organization_id).all()
    return render_template("customerProfile.html", organizations=organizations, follows=follows)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

if __name__=='__main__':
    app.run(debug=True)