from app import app
from flask import request, Response
from flask_login import *
from flask.ext.security import login_required, LoginForm
from authentication import SECRET_KEY, load_user_from_request, check_auth
from models import User, Message
from flask.ext.login import current_user
from stream_client import client
import json
from collections import namedtuple
from flask_cors import *

@app.route('/api/follow/<int:seeker_id>', methods=['PUT'])
def follow():
    if not check_auth(request):
        return Response(status=403)
    
    # get the carer profile
    user = load_user_from_request(request)
    user_feed = client.feed('notification:'+str(user.id))
    user_feed.follow('user', str(seeker_id))

@app.route('/api/unfollow/<int:seeker_id>', methods=['PUT'])
def follow():
    if not check_auth(request):
        return Response(status=403)

    # get the carer profile
    user = load_user_from_request(request)
    user_feed = client.feed('notification:'+str(user.id))
    user_feed.unfollow('user', str(seeker_id))

@app.route('/api/following', methods=['GET'])
def following():
    
    if not check_auth(request):
        return Response(status=403)
    
    # get the carer profile
    user = load_user_from_request(request)
    
    # get the care seekers that I am following
    user_feed = client.feed('notification:'+str(user.id))
    care_seekers = user_feed.following()
    
    return Response(json.dumps(care_seekers),  mimetype='application/json', status=200)  
    

@app.route('/api/subscription', methods=['POST', 'DELETE'])
def follow():
    # first authenticate the follower, otherwise raise 401
    if not check_auth(request):
        return Response(status=403)

    care_seeker_username = request.form.get('care_seeker_username')
    care_seeker = User.query.filter_by(username=care_seeker_username).first()
    care_seeker_id = care_seeker.id
    care_giver_id = current_user.id

    my_feed = client.feed('notification:'+str(care_giver_id))
    if not care_seeker_id:
        return Response(status=400)

    if request.method == 'POST':
        my_feed.follow('user:'+str(care_seeker_id))
        return Response(status=201)
    else:
        my_feed.unfollow('user:'+str(care_seeker_id))
        return Response(status=202)
        
'''
Claiming a request by a carer consists of marking the request claimed on database
as well as sending a message to the other carers that you'll be the one taking 
the request
'''
@app.route('/api/claims/<int:message_id>', methods=['POST'])
# @app.route('/post/<int:message_id>')
def claim(message_id):
    
    if not check_auth(request):
        return Response(status=403)
    
    # get the carer profile
    user = load_user_from_request(request)
    
    # get the message
    message = Message.query.filter_by(message_id=message_id).first()
    
    # debug printing
    print "User %s is claiming message from %s saying %s!" %(user.full_name, message.author.full_name, message.text)
    
    # TODO: patch the message and set the claimed flag
    
    # Sending a message to every other carer besides self that I claimed the request
    user_feed = client.feed('user:'+str(message.author_id))
    author_followers = user_feed.followers()
    for each_follower in author_followers.get('results'):
        follower_feed = each_follower.get('feed_id')
        follower_id = follower_feed.split(':')[-1]
        notification_feed = client.feed(follower_feed)
        
        if str(follower_id) == str(user.id):
            continue
        else:
            followers = []
            followers.append(follower_feed)
            activity = {
                'actor': user.id, 
                'verb': 'claimed', 
                'object':message.text,
                'foreign_id':message_id,
                'geolocation':user.current_location,
                'to':followers
            }
            
            # add specific "TO" notifications, one by one
            # print "Adding activity to ", followers
            activity_response = notification_feed.add_activity(activity)
    
    return Response(status=201)

@app.route("/login", methods=["POST", "GET", "OPTIONS"])
@cross_origin()
def login():

    if not check_auth(request):
        return Response(status=403)

    user = load_user_from_request(request)
    user_feed = client.feed('user:'+str(user.id))
    # user.token = user_feed.token

    UserStruct = namedtuple('UserStruct', 'id, username, email, care_giver, care_seeker, token')
    u = UserStruct(id=user.id, username=user.username, email=user.email, care_giver=user.care_giver, care_seeker=user.care_seeker, token=user_feed.token)

    # print json.dumps(json.dumps(u))
    return Response(json.dumps(u),  mimetype='application/json', status=200)

@app.route("/logout", methods=["POST"])
@cross_origin()
@login_required
def logout():
    logout_user()
    # flash("Logged out successfully.")
    return Response(status=200)
