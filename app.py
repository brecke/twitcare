# -*- coding: utf-8 -*-
import time
from hashlib import md5
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import *
from utils import *
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
PER_PAGE = 30
DEBUG = True

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/development.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MINITWIT_SETTINGS', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.secret_key = 'badjouras'
