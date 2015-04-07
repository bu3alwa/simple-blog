import sys
import os

from flask import render_template, request, session, redirect, session, Blueprint, abort, flash
from pyapp import app
from models import *
from pyapp import db
from jinja2 import TemplateNotFound

@app.route('/', methods=['GET'])
def index():
    posts = Post.query.order_by(Post.id).all()

    if not session.get('logged_in'):
        return render_template("index.html", posts=posts)
    else:
        user = session.get('user')
        return render_template("index.html", posts=posts, username=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form.get('username')
        password = request.form.get('password')
        try:
            if not session.get('logged_in'):
                user = User.query.filter_by(username=user_name).first()
                if user.verify_pass(password):
                    session['logged_in'] = True
                    session['user'] = user.username[0]
                    return redirect("/")
            else:
                return redirect("/")
        except:
            return render_template("login.html", error='login error')
        
    elif request.method == 'GET':
        if session.get("loggged_in"):
            redirect('/')
        else:
            return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if not session.get("logged_in"):
         return render_template("register.html", user=session.get('user'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        try:
            if user.username == username:
                return render_template("register.html", error="User already exists")

        except:
            try:
                 newuser = User(username, password)
                 db.session.add(newuser)
                 db.session.commit()
                 return redirect('/')
            except:
                return render_template("register.html", error="Register error")
                
@app.route('/add-post', methods=['GET', 'POST'])
def addpost():
    if request.method == 'GET':
        if not session.get('logged_in'):
            flash("Please login first")
            return redirect("/login")
        else:
            user = session.get("user")
            return render_template("add-post.html", username=user)

    if request.method == 'POST':
        try:
            title = request.form.get('title')
            body = request.form.get('content')
            newpost = Post(title, body)
            db.session.add(newpost)
            db.session.commit()
            return redirect("/")
        except:
            return render_template("add-post.html", error="error posting")

@app.route('/logout', methods=['GET'])
def logout():
    if session.get('logged_in'):
        session.pop('user', None)
        session.pop('logged_in', None)
        return redirect('/')
    else:
        flash("You are not logged in")
        return redirect('/')
