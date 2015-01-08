import flask.ext.sqlalchemy
from  flask.ext.restless import APIManager
from app import app
from models import User, Message, db
from stream_client import client
from flask.ext.login import current_user
from flask.ext.restless import ProcessingException
from authentication import check_auth
from flask import request, abort
import json
import requests
import pprint

# preprocessor
def auth_func(*args, **kwargs):
    # print "DEBUG: request.authorization, ", request.authorization
    if not check_auth(request):
        # return Response(status=401)
        raise ProcessingException(description='Not authenticated!', code=403)
    return True

# the user authenticates and we use the username to extract the author_id field for the message
def replace_username_for_author_id(data=None, **kw):
    user = User.query.filter_by(username=request.authorization.username).first()
    author_id = user.id
    data['author_id'] = author_id
    del data['username']
    print data

# postprocessor
def post_create_message(result, **kw):
    
    # get the feed for the message author
    author_id = result.get('author_id')
    author = User.query.filter_by(id=author_id).first()
    author_location = author.current_location
    user_feed = client.feed('user:'+str(author_id))
    
    tweet = result.get('text')
    message_id = result.get('message_id')
    
    # list of the given feed's followers
    author_followers = user_feed.followers()
    
    # debug printing
    # print "%s (from %s) is sending messages..." % (author.full_name, author_location)
    
    # send activity individually because of the costumized message
    for each_follower in author_followers.get('results'):
        
        # get the data from each follower
        follower_feed = each_follower.get('feed_id')
        follower_id = follower_feed.split(':')[-1]
        follower = User.query.filter_by(id=follower_id).first()
        follower_location = follower.current_location
        
        # use google distance API to get driving distance between care seeker and carer
        key = ''
        response = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?key=' + key + '+&origins=' + follower_location +'&destinations=' + author_location)
        data = response.json()
        
        if data.get('status') == 'OK':
            duration = data.get('rows')[0].get('elements')[0].get('duration')
            print "====> %s would take %s to rescue %s" % (follower.full_name, duration.get('text'), author.full_name)
        else:
            duration = -1
            print "Cannot contact Google to calculate distance... moving on with -1"
        
        followers = []
        followers.append(follower_feed)
        activity = {
            'actor': author_id, 
            'verb': 'tweet',
            'object':message_id,
            'foreign_id':message_id,
            'tweet': tweet, 
            'geolocation':author.current_location,
            'duration': duration.get('text'),
            'to':followers
        }
        
        # add specific "TO" notifications, one by one
        activity_response = user_feed.add_activity(activity)
        # print "Posting feedback: ", activity_response
    
# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
includes = ['id', 'username', 'email', 'full_name', 'followed_by_list', 'followed_by_list.followed_by_id', 'followed_list', 'followed_list.followed_id', 'current_location', 'avatar', 'care_type']
manager.create_api(User, methods=['GET'],
    collection_name='people',
    include_columns=includes,
    preprocessors=dict(GET_SINGLE=[auth_func],
            GET_MANY=[auth_func],
            PUT_SINGLE=[auth_func],
            PUT_MANY=[auth_func],
            POST=[auth_func],
            DELETE=[auth_func]))

includes = ['message_id', 'author_id', 'text', 'pub_date']
manager.create_api(Message, methods=['POST'],
    collection_name='messages',
    postprocessors={
        'POST': [post_create_message]
    },
    preprocessors=dict(GET_SINGLE=[auth_func],
        GET_MANY=[auth_func],
        PUT_SINGLE=[auth_func],
        PUT_MANY=[auth_func],
        POST=[auth_func, replace_username_for_author_id],
        DELETE=[auth_func]))
