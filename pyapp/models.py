import os
import sys
import datetime

from flask import Flask
from passlib.hash import sha256_crypt
from flask.ext.sqlalchemy import SQLAlchemy
from pyapp import db, SECRET_KEY

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    remember_token = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, username, password, remember=False):
        self.username = username.strip()
        self.password = sha256_crypt.encrypt(password, salt=SECRET_KEY, rounds=110000)
	self.remember_token = remember
	self.created_at = False
	self.updated_at = False

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
