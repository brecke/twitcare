from app import app
from flask_login import *
from werkzeug import check_password_hash, generate_password_hash
from models import User
from flask.ext.login import login_user, current_user

SECRET_KEY = 'development key'

login_manager = LoginManager()
login_manager.init_app(app)

# @login_manager.request_loader
def load_user_from_request(request):
    auth = request.authorization
    user = User.query.filter_by(username=auth.username).first()
    if user:
        return user
    return None

def check_auth(request):
    
    # in case there are no headers
    if not request.authorization:
        print "No authorization headers sent, returning false."
        return False
    
    # debug
    # print "LOGIN request coming in..."
    # print "request user: ", request.authorization.username
    # print "request password: ", request.authorization.password
        
    user = load_user_from_request(request)
    password = request.authorization.password
    
    # user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.pw_hash, password):
        login_user(user)
        current_user = user # this shoudn't be necessary...!?!
        return True
    else:
        return False
