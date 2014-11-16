from app import app
from flask_login import *
from werkzeug import check_password_hash, generate_password_hash
from models import User
from flask.ext.login import login_user, current_user

SECRET_KEY = 'development key'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.request_loader
def load_user_from_request(request):
    # try to login using Basic Auth
    auth = request.authorization
    user = User.query.filter_by(username=auth.username).first()
    print "DEBUG: loading user from request: ", user
    if user:
        return user

    # finally, return None if both methods did not login the user
    return None

def check_auth(request):
    user = load_user_from_request(request)
    password = request.authorization.password
    # user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.pw_hash, password):
        login_user(user)
        current_user = user # this shoudn't be necessary...!?!
        return True
    else:
        return False
