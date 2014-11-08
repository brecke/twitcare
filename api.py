import flask.ext.sqlalchemy
from  flask.ext.restless import APIManager
from app import app
from models import User, Message, db
from stream_client import client

# postprocessors
def post_create_message(result, **kw):
    # get the feed for the message author
    author_id = result.get('author_id')
    print "author_id", author_id
    user_feed = client.feed('user:'+str(author_id))
    activity_data = {'actor': author_id, 'verb': 'tweet', 'object': result.get('message_id'), 'tweet': result.get('text')}
    activity_response = user_feed.add_activity(activity_data)

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
includes = ['id', 'username', 'email', 'followed_by_list', 'followed_by_list.followed_by_id', 'followed_list', 'followed_list.followed_id']
manager.create_api(User, methods=['GET'], 
    collection_name='people', 
    include_columns=includes)

includes = ['message_id', 'author_id', 'text']
manager.create_api(Message, methods=['POST'], 
    collection_name='messages',
    postprocessors={
        'POST': [post_create_message]
    })
