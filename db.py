import os
from flask import Flask
from passlib.hash import sha256_crypt
from flaskkext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor@localhost/blog'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Table('users', db.Column(db.Integer, primary_key=True))
    username = db.Table('users', db.Column(db.String(80), unique=True))
    password = db.Table('users', db.Column(db.String(255), unique=True))

    def __init__(self, username, password)
        self.username = username
        self.password = password

    def verify_pass(self, password):
        return sha256_crypt.verify(password, self.password)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)

    def __init__(self, title, body)
        self.title = title
        self.body = body
    
    def __repr__(self):
        return '<Post %r>' % self.title

