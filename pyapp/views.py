import sys
import os

from flask import render_template, request, session, redirect, session, Blueprint, abort
from pyapp import app
from models import *
from pyapp import db
from jinja2 import TemplateNotFound

SESSION_AGE = 600
INVALID_SESSION = ("Your session expired, pleade log in again", 403)

page = Blueprint('page', __name__, template_folder='templates')
app.register_blueprint(page)

def forbidden():
    return("Access denied", 403)

@app.route('/', methods=['GET'])
def index():
    posts = User.query.order_by(User.id).all()
    return render_template("index.html", posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.args.get('username')
        password = request.args.get('password')
        try:
            user = User.query.filter_by(username=user_name).first()
            if user.verify_pass(password):
                return "logged in"
            else:
                return render_template("login.html")
        except:
            return render_template("login.html", error='login error')
        
    elif request.method == 'GET':
         return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
         return render_template("register.html")

    if request.method == 'POST':
        username = request.args.get('username')
        password = request.args.get('password')
        try:
            newuser = User(username, password)
            db.session.add(newuser)
            db.session.commit()
        except:
            return render_template("register.html", error='registration failed')
            
