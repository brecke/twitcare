from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless

from app import app
from models import *

from api import *
from views import *
# from database import *

if __name__ == '__main__':
    app.run()
