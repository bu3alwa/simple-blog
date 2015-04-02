import sys
import os

from flask import render_template, request, session, redirect
from . import app, db
from models import User, Post

SESSION_AGE = 600
INVALID_SESSION = ("Your session expired, pleade log in again", 403)

def forbidden():
    return("Access denied", 403)

@app.route('/')
def index():
    return render_template("show_entries.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/create-user')
def create_user():
    return render_template("create_user")

