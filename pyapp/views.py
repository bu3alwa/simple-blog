import sys
import os

from flask import render_template, request, session, redirect, session, Blueprint, abort
from pyapp import app
from models import *
from pyapp import db
#from jinja2 import TemplateNotFound

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

@app.route('/login')
def login():
    return app.root_path

@app.route('/create-user')
def create_user():
    return render_template("create_user")

