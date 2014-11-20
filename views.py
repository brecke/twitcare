from app import app
from stream_client import client
from flask import request, Response
from flask_login import *
from flask.ext.security import login_required, LoginForm
from authentication import SECRET_KEY, load_user_from_request, check_auth
from models import User
from flask.ext.login import current_user
from stream_client import client
import json
from collections import namedtuple

@app.route('/api/subscription', methods=['POST', 'DELETE'])
def follow():
    # first authenticate the follower, otherwise raise 401
    if not check_auth(request):
        return Response(status=401)

    care_taker_username = request.form.get('care_taker_username')
    care_taker = User.query.filter_by(username=care_taker_username).first()
    care_taker_id = care_taker.id
    care_giver_id = current_user.id

    my_feed = client.feed('flat:'+str(care_giver_id))
    if not care_taker_id:
        return Response(status=400)

    if request.method == 'POST':
        my_feed.follow('user:'+str(care_taker_id))
        return Response(status=201)
    else:
        my_feed.unfollow('user:'+str(care_taker_id))
        return Response(status=202)

@app.route("/login", methods=["POST"])
def login():
    if not check_auth(request):
        return Response(status=401)

    user = load_user_from_request(request) 
    user_feed = client.feed('user:'+str(user.id))
    # user.token = user_feed.token

    UserStruct = namedtuple('UserStruct', 'id, username, email, care_giver, care_taker, token')
    u = UserStruct(id=user.id, username=user.username, email=user.email, care_giver=user.care_giver, care_taker=user.care_taker, token=user_feed.token)
    
    # print json.dumps(json.dumps(u))
    return Response(json.dumps(u),  mimetype='application/json', status=200)

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return Response(status=200)
