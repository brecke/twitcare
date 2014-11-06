import flask.ext.sqlalchemy
from  flask.ext.restless import APIManager
from app import app
from models import User, Message, UserFollow, db

# postprocessors
def post_post_message(result, **kw): 
    author = User.query.filter_by(id=result.get('author_id')).first() 
    # debug
    print "The tweet saying '%s' is going to be pushed to the following users: %r" % (result.get('text'), author.followed_by_list)
    #TODO

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
includes = ['id', 'username', 'email', 'followed_by_list', 'followed_by_list.followed_by_id', 'followed_list', 'followed_list.followed_id']
manager.create_api(User, methods=['GET', 'POST', 'DELETE'], 
    collection_name='people', 
    include_columns=includes)

# manager.create_api(UserFollow, methods=['GET', 'POST'],
    # collection_name='followers',
    # exclude_columns=['pw_hash'])

includes = ['message_id', 'author_id', 'text']
manager.create_api(Message, methods=['GET', 'POST'], 
    collection_name='messages',
    postprocessors={
        'POST': [post_post_message]
    })
