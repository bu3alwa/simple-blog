import os
import sys

from flask import Flask
from passlib.hash import sha256_crypt
from flask.ext.sqlalchemy import SQLAlchemy
from pyapp import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username.strip()
        self.password = password

    def verify_pass(self, password):
        return sha256_crypt.verify(password, self.password)
    
    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body
    
    def __repr__(self):
        return '<Post %r>' % self.body
