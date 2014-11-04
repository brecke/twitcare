# -*- coding: utf-8 -*-
"""
    A microblogging API application highly inspired by minitwit
"""

import time
from hashlib import md5
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import *
from utils import *

# configuration
DATABASE = 'db/development.db'
PER_PAGE = 30
DEBUG = True

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MINITWIT_SETTINGS', silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE

# add some filters to jinja
app.jinja_env.filters['datetimeformat'] = format_datetime
app.jinja_env.filters['gravatar'] = gravatar_url
