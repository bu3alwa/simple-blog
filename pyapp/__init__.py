from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import sys
import yaml
import argparse

parser = argparse.ArgumentParser(prog='pyapp')
parser.add_argument("-c", "--config", help="path to config file", type=str, required=True)
args = parser.parse_args()

f = open(args.config)

conf = yaml.load(f)
DB_HOST = conf['db-host']
DB_USER = conf['db-user']
DB_PASS = conf['db-pass']
DB_PORT = conf['db-port']
DB_TYPE = conf['db-type']
DB_NAME = conf['db-name']
PORT = conf['port']
SECRET_KEY = 'test'

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DB_TYPE + '://' + DB_USER + ":" + DB_PASS + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME
db = SQLAlchemy(app)

from pyapp import models, views
db.create_all()

app.debug = True
