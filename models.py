from flask.ext.sqlalchemy import SQLAlchemy
from app import app
from werkzeug import check_password_hash, generate_password_hash
from datetime import datetime

SECRET_KEY = 'development key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(120))
    care_giver = db.Column(db.Integer) # whether its a nurse or a doctor
    care_taker = db.Column(db.Integer) # whether its a patient or not

    def __init__(self, username, password, email, care_giver, care_taker):
        self.username = username
        self.pw_hash = generate_password_hash(password)
        self.email = email
        self.care_giver = care_giver
        self.care_taker = care_taker

    @property
    def is_authenticated(self):
        return True
        
    def is_authenticated(self):
        # print "is_authenticated: True"
        return self.is_authenticated
        
    @property
    def is_active(self):
        return True

    def is_active(self):
        return self.is_active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username

class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    text = db.Column(db.String(140))
    pub_date = db.Column(db.DateTime)

    def __init__(self, author_id, text):
        self.author_id = author_id
        self.text = text
        self.pub_date = datetime.now()

    def __repr__(self):
        return '%s said %s' %(self.author_id, self.text)

db.create_all()
